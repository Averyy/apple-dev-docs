---
url: "https://docs.swift.org/latest/documentation/diagnostics/trailing-closure-matching"
framework: "Swift-Org/diagnostics"
---

# Argument matching for trailing closures (TrailingClosureMatching)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Where trailing closures are used to pass one or more arguments to a function, the argument label for the first trailing closure is always omitted:

```swift
func animate(
  withDuration duration: Double,
  animations: () -> Void,
  completion: (() -> Void)? = nil
) { /* ... */ }

animate(withDuration: 0.3) /* `animations:` is unwritten. */ {
  // Animate something.
} completion: {
  // Completion handler.
}
```

Sometimes, an unlabeled trailing closure argument can be matched to more than one function parameter. Before Swift 5.3, the compiler would use a **backward scanning rule** to match the unlabeled trailing closure, scanning backwards from the end of the parameter list until finding a parameter that can accept a closure argument (a function type, unconstrained generic type, `Any`, etc.):

```swift
animate(withDuration: 0.3) {
  // Animate something?
  // The compiler matches this to the `completion` parameter.
}
// error: missing argument for parameter 'animations' in call
```

We encounter a compiler error in this example because the backward scanning rule matches the trailing closure to the `completion` parameter instead of the `animations` parameter, even though `completion` has a default value while `animations` does not.

Swift 5.3 introduces a new **forward scanning rule**, which matches trailing closures to function parameters from left to right (after matching non-trailing arguments). This leads to more predictable and easy-to-understand behavior in many situations. With the new rule, the unlabeled closure in the example above is matched to the `animations` parameter, just as most users would expect:

```swift
animate(withDuration: 0.3) {
  // Animate something.
} // `completion` has the default value `nil`.
```

When scanning forwards to match an unlabeled trailing closure argument, the compiler will skip any parameter that does not **structurally resemble** a function type and also apply a **heuristic** to skip parameters that do not require an argument in favor of a subsequent parameter that does (see below). These rules make possible the ergonomic use of a modified version of the API given in the example above, where `withDuration` has a default value:

```swift
func animate(
  withDuration duration: Double = 1.0,
  animations: () -> Void,
  completion: (() -> Void)? = nil
) { /* ... */ }

animate {
  // Animate something.
  //
  // The closure is not matched to `withDuration` but to `animations` because
  // the first parameter doesn't structurally resemble a function type.
  //
  // If, in place of `withDuration`, there is a parameter with a default value
  // that does structurally resemble a function type, the closure would still be
  // matched to `animations` because it requires an argument while the first
  // parameter does not.
}
```

For source compatibility in Swift 5, the compiler will attempt to apply *both* the new forward scanning rule and the old backward scanning rule when it encounters a function call with a single trailing closure. If the forward and backward scans produce *different valid* matches of arguments to parameters, the compiler will prefer the result of the backward scanning rule and produce a warning. To silence this warning, rewrite the function call to label the argument explicitly without using trailing closure syntax.

#### Structural resemblance to a function type

A parameter structurally resembles a function type if both of the following are true:

- the parameter is not `inout`, and
- the **adjusted type** of the parameter is a function type.

The adjusted type of the parameter is the parameter’s type as it appears in the function declaration, looking through any type aliases, and performing three additional adjustments:

1. If the parameter is an `@autoclosure`, use the result type of the parameter’s declared (function) type before performing the second adjustment.
2. If the parameter is variadic, look at the base element type.
3. Remove all outer “optional” types.

#### Heuristic for skipping parameters

To maintain source compatibility, the forward scanning rule applies an additional heuristic when matching trailing closure arguments. If:

- the parameter that would match an unlabeled trailing closure argument according to the forward scanning rule does not require an argument (because it is variadic or has a default argument), *and*
- there are parameters *following* that parameter that *do* require an argument, which appear before the first parameter whose label matches that of the *next* trailing closure (if any),

then the compiler does not match the unlabeled trailing closure to that parameter. Instead, it examines the next parameter to see if that should be matched to the unlabeled trailing closure, as in the following example:

```swift
func showAlert(
  message: String,
  onPresentation: (() ->  Void)? = nil,
  onDismissal: () -> Void
) { /* ... */ }

// `onPresentation` does not require an argument, but `onDismissal` does, and
// there is no subsequent trailing closure labeled `onDismissal`.
// Therefore, the unlabeled trailing closure is matched to `onDismissal`.
showAlert(message: "Hello, World!") {
  // On dismissal action.
}

// Although `onPresentation` does not require an argument, there are no
// subsequent parameters that require an argument before the parameter whose
// label matches the next trailing closure (`onDismissal`).
// Therefore, the unlabeled trailing closure is matched to `onPresentation`.
showAlert(message: "Hello, World!") {
  // On presentation action.
} onDismissal: {
  // On dismissal action.
}
```

## See Also

### Related Documentation
- [SE-0279: Multiple trailing closures](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0279-multiple-trailing-closures.md)
- [SE-0286: Forward-scan matching for trailing closures](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0286-forward-scan-trailing-closures.md)
- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
  Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.
- [Calling a mutating async actor-isolated method (ActorIsolatedMutatingAsync)](./actor-isolated-mutating-async.md)
- [Calling an actor-isolated method from a synchronous nonisolated context (ActorIsolatedCall)](./actor-isolated-call.md)
- [Captures in a `@Sendable` closure (SendableClosureCaptures)](./sendable-closure-captures.md)
- [Compilation caching (CompilationCaching)](./compilation-caching.md)
  Errors and warnings related to the compiler’s CAS compilation caching.
- [Conforming to `StringInterpolationProtocol` (StringInterpolationConformance)](./string-interpolation-conformance.md)
- [Conversion from `@isolated(any)` function type to synchronous function type (ConversionFromIsolatedAnyToSynchronous)](./conversion-from-isolated-any-to-synchronous.md)
- [Deprecated declaration warnings (DeprecatedDeclaration)](./deprecated-declaration.md)
  Warnings related to deprecated APIs that may be removed in future versions and should be replaced with more current alternatives.
- [Deprecated implementation-only imports (ImplementationOnlyDeprecated)](./implementation-only-deprecated.md)
  Warnings that identify `import` declarations with the `@_implementationOnly` attribute.
- [Dynamic exclusivity (DynamicExclusivity)](./dynamic-exclusivity.md)
  Experimental
- [Embedded Swift language restrictions (EmbeddedRestrictions)](./embedded-restrictions.md)
  Embedded Swift is a subset of the Swift language that that introduces some restrictions on the use of language features to eliminate the need for the Swift runtime. These restrictions are captured by the `EmbeddedRestrictions` diagnostic group.
- [Existential Types and Performance (ExistentialType)](./existential-type.md)
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/trailing-closure-matching)*