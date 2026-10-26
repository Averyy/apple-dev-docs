---
url: "https://docs.swift.org/latest/documentation/diagnostics/unnecessary-effect-marker"
framework: "Swift-Org/diagnostics"
---

# Unnecessary effect markers (UnnecessaryEffectMarker)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

These warnings are emitted when an effect marker — `try`, `await`, or `unsafe` — appears on an expression that contains no operation requiring it. The marker may have been added preemptively, the operation it was needed for may have been removed, or the resolved expression may not contain the operation that was expected to carry the effect.

The `UnnecessaryEffectMarker` group covers:

- `try` on an expression that calls no throwing functions
- `await` on an expression that performs no `async` operations
- `unsafe` on an expression that contains no unsafe operations
- `unsafe` on a `for`-`in` loop whose `Sequence` has a safe conformance

#### Example

```swift
func greet(_ name: String) {
  print("Hello, \(name)")  // not throwing, not async, not unsafe
}

func caller() async throws {
  try greet("Ada")    // warning: no calls to throwing functions occur within 'try' expression
  await greet("Ada")  // warning: no 'async' operations occur within 'await' expression
  unsafe greet("Ada") // warning: no unsafe operations occur within 'unsafe' expression
}
```

#### How to fix

Remove the marker:

```swift
func caller() async throws {
  greet("Ada")
}
```

## See Also

### Related Documentation
- [Unnecessary unsafe (UnnecessaryUnsafe)](./unnecessary-unsafe.md)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/unnecessary-effect-marker)*