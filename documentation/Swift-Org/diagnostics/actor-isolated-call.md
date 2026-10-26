---
url: "https://docs.swift.org/latest/documentation/diagnostics/actor-isolated-call"
framework: "Swift-Org/diagnostics"
---

# Calling an actor-isolated method from a synchronous nonisolated context (ActorIsolatedCall)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Accessing actor-isolated state from outside the actor can cause data races in your program. Resolve this error by calling actor-isolated functions on the actor.

Calls to actor-isolated methods from outside the actor must be done asynchronously. Otherwise, access to actor state can happen concurrently and lead to data races. These rules also apply to global actors like the main actor.

For example:

```swift
@MainActor
class MyModel {
  func update() { ... }
}

func runUpdate(model: MyModel) {
  model.update()
}
```

Building the above code produces an error about calling a main actor isolated method from outside the actor:

```
| func runUpdate(model: MyModel) {
|   model.update()
|         `- error: call to main actor-isolated instance method 'update()' in a synchronous nonisolated context
| }
```

The `runUpdate` function doesn’t specify any actor isolation, so it is `nonisolated` by default. `nonisolated` methods can be called from any concurrency domain. To prevent data races, `nonisolated` methods cannot access actor isolated state in their implementation. If `runUpdate` is called from off the main actor, calling `model.update()` could mutate main actor state at the same time as another task running on the main actor.

To resolve the error, `runUpdate` has to make sure the call to `model.update()` is on the main actor. One way to do that is to add main actor isolation to the `runUpdate` function:

```swift
@MainActor
func runUpdate(model: MyModel) {
  model.update()
}
```

Alternatively, if the `runUpdate` function is meant to be called from arbitrary concurrent contexts, create a task isolated to the main actor to call `model.update()`:

```swift
func runUpdate(model: MyModel) {
  Task { @MainActor in
    model.update()
  }
}
```

## See Also

- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
  Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.
- [Argument matching for trailing closures (TrailingClosureMatching)](./trailing-closure-matching.md)
- [Calling a mutating async actor-isolated method (ActorIsolatedMutatingAsync)](./actor-isolated-mutating-async.md)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/actor-isolated-call)*