---
url: "https://docs.swift.org/latest/documentation/diagnostics/isolated-conformances"
framework: "Swift-Org/diagnostics"
---

# Isolated conformances (IsolatedConformances)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

Using an isolated conformance from outside the actor can cause data races in your program. Resolve these errors by only using isolated conformances within the actor.

A protocol conformance can be isolated to a specific global actor, meaning that the conformance can only be used by code running on that actor. Isolated conformances are expressed by specifying the global actor on the conformance itself:

```swift
protocol P {
  func f()
}

@MainActor
class MyType: @MainActor P {
  /*@MainActor*/ func f() {
    // must be called on the main actor
  }
}
```

Swift will produce diagnostics if the conformance is directly accessed in code that isn’t guaranteed to execute in the same global actor. For example:

```swift
func acceptP<T: P>(_ value: T) { }

/*nonisolated*/ func useIsolatedConformance(myType: MyType) {
  acceptP(myType) // error: main actor-isolated conformance of 'MyType' to 'P' cannot be used in nonisolated context
}
```

To address this issue, mark the code as having the same global actor as the conformance it is trying to use. In this case, mark `useIsolatedConformance` as `@MainActor` so that the code is guaranteed to execute on the main actor.

An isolated conformance cannot be used together with a `Sendable` requirement, because doing so would allow the conformance to cross isolation boundaries and be used from outside the global actor. For example:

```swift
func acceptSendableP<T: P & Sendable>(_ value: T) { }

@MainActor func useIsolatedConformanceOnMainActor(myType: MyType) {
  acceptSendableP(myType) // error: main-actor-isolated conformance of 'MyType' to 'P' cannot satisfy conformance requirement for 'Sendable' type parameter 'T'
}
```

These errors can be addressed by either making the conformance itself `nonisolated` or making the generic function not require `Sendable`.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/isolated-conformances)*