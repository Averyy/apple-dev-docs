---
url: "https://docs.swift.org/latest/documentation/diagnostics/conversion-from-isolated-any-to-synchronous"
framework: "Swift-Org/diagnostics"
---

# Conversion from `@isolated(any)` function type to synchronous function type (ConversionFromIsolatedAnyToSynchronous)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

A function value with type `@isolated(any)` carries its actor isolation dynamically. Calling such a function from a context that does not share its isolation requires hopping to the function’s actor, which can only be done from an asynchronous context. As a result, an `@isolated(any)` function value cannot be converted to a synchronous, non-`@isolated(any)` function type.

```swift
@MainActor func updateUI() { /* ... */ }

func runInBackground(_ work: @escaping @Sendable () -> ()) {
  DispatchQueue.global().async { work() }
}

func schedule(_ work: @escaping @isolated(any) @Sendable () -> ()) {
  runInBackground(work) // warning: converting @isolated(any) function of type '@isolated(any) @Sendable () -> ()' to synchronous function type '@Sendable () -> ()' is not allowed
}

schedule(updateUI)
```

In the example, `updateUI()` would run on a background thread instead of the main actor which could result in a data race.

This conversion is currently diagnosed as a warning that will become an error in a future Swift language mode. To opt in to treating it as an error today, pass `-Werror ConversionFromIsolatedAnyToSynchronous`.

To resolve the diagnostic, convert the function value to an `async` function type and use `await` when invoking the function, or remove the `@isolated(any)` attribute from the source type if it is not needed.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/conversion-from-isolated-any-to-synchronous)*