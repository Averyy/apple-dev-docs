---
url: "https://docs.swift.org/latest/documentation/diagnostics/variable-never-mutated"
framework: "Swift-Org/diagnostics"
---

# Variable never mutated (VariableNeverMutated)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

Warnings that identify local `var` bindings which are never mutated after initialization and could instead be declared with `let`.

#### Overview

When a variable is introduced with `var` but never reassigned or otherwise mutated, it can be declared with `let` instead to explicitly indicate that the variable is constant.

#### Example

```swift
func swap(_ a: inout Int, _ b: inout Int) {
  var temp = a // warning: variable 'temp' was never mutated; consider changing to 'let' constant
  a = b
  b = temp
}
```

The fix is to change `var` to `let`:

```swift
func swap(_ a: inout Int, _ b: inout Int) {
  let temp = a
  a = b
  b = temp
}
```

#### Sub-groups

The `VariableNeverMutated` group contains the following sub-group, which can also be enabled or controlled independently:

- doc:weak-mutability: Warns when a `weak var` binding is never mutated and could be a `weak let` instead.

## See Also

- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
  Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.
- [Argument matching for trailing closures (TrailingClosureMatching)](./trailing-closure-matching.md)
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


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/variable-never-mutated)*