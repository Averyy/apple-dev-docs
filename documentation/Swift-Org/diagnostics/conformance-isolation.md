---
url: "https://docs.swift.org/latest/documentation/diagnostics/conformance-isolation"
framework: "Swift-Org/diagnostics"
---

# Protocol conformances crossing into actor-isolated code (ConformanceIsolation)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

Protocol conformances crossing into actor-isolated code can cause data races in your program. Resolve this error by ensuring access to isolated state is always done within the actor.

When a type conforms to a protocol, any generic code can perform operations on that type through the protocol. If the operations that the type used to satisfy the protocol requirements are actor-isolated, this may result in a diagnostic indicating that the conformance crosses into actor-isolated code. For example:

```swift
protocol P {
  func f()
}

@MainActor
struct MyData: P {
  func f() { }
}
```

This code will produce an error similar to:

```swift
@MainActor
struct MyData: P {
            // |- error: conformance of 'MyData' to protocol 'P' crosses into main actor-isolated code and can cause data races
            // |- note: isolate this conformance to the main actor with '@MainActor'
            // `- note: turn data races into runtime errors with '@preconcurrency'
  func f() { }
    // |- note: main actor-isolated instance method 'f()' cannot satisfy nonisolated requirement
    // `- note: mark instance method 'f()' 'nonisolated'
}
```

There are several options for resolving this error, as indicated by the notes:

- If all of the operations used to satisfy the protocol’s requirements are on the same global actor (such as the main actor), the conformance itself can be isolated to that global actor. This allows the conformance to be used inside code running on that actor, but it cannot be used concurrently. A conformance can be isolated to a global actor the same way as anything else in the language, e.g.,

  ```swift
  @MainActor
  struct MyData: @MainActor P {
    func f() { }
  }
  ```
- If the protocol requirements themselves are meant to always be used from the correct isolation domain (for example, the main actor) but the protocol itself did not describe that requirement, the conformance can be marked with `@preconcurrency`. This approach moves isolation checking into a run-time assertion, which will produce a fatal error if an operation is called without already being on the right actor. A `@preconcurrency` conformance can be written as follows:

  ```swift
  @MainActor
  struct MyData: @preconcurrency P {
    func f() { }
  }
  ```
- If the conformance needs to be usable anywhere, then each of the operations used to satisfy its requirements must be marked `nonisolated`. This means that they will not have access to any actor-specific operations or state, because these operations can be called concurrently from anywhere. The result would look like this:

  ```swift
  @MainActor
  struct MyData: P {
    nonisolated func f() { }
  }
  ```

## Stored Properties

When conforming to a protocol that has read only properties, there is an additional option; defining properties as `nonisolated let`. This makes them immutable and concurrently accessible. For example:

```swift
@MainActor
class MyModel: ObservableObject, Identifiable {
  var id = UUID()
   // |- note: main actor-isolated property 'id' cannot satisfy nonisolated requirement
   // `- note: change property 'id' to a 'nonisolated let' constant
  var count = 0
}
```

By changing `id` from `var` to `nonisolated let`, any generic code that works with `Identifiable` can safely read `id` from any isolation region:

```swift
@MainActor
class MyModel: ObservableObject, Identifiable {
  nonisolated let id = UUID()
  var count = 0
}
```

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/conformance-isolation)*