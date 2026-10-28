---
url: "https://docs.swift.org/latest/documentation/diagnostics/non-sendable-values-in-async-conformances-and-overrides"
framework: "Swift-Org/diagnostics"
---

# Non-Sendable values in async conformances and overrides (NonSendableInAsyncConformanceOrOverride)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

An `async` method that satisfies a protocol requirement (or overrides a superclass method) may be isolated to a different actor than the requirement it fulfills. This is allowed because calling an `async` method suspends the caller, letting the implementation resume in its specified isolation. (The same applies to `get async` accessors.)

When the two isolations differ, the method’s parameters and results have to cross between them. That crossing is only safe for `Sendable` values, so the compiler rejects it for non-Sendable ones.

For example:

```swift
class Plant {
    var height = 0
}

protocol PlantJournal {
    func record(plant: Plant) async
}

@MainActor
class GardenJournal: PlantJournal {
    func record(plant: Plant) async { // error: non-Sendable parameter type 'Plant' cannot be sent from caller of protocol requirement 'record(plant:)' into main actor-isolated implementation
        print("Recorded plant at \(plant.height) cm tall")
    }
}
```

Here, the `GardenJournal` implementation is isolated to the main actor, while the `PlantJournal` requirement is not. A caller in a different isolation that invokes `record(plant:)` would pass a non-Sendable `Plant` into the main-actor-isolated implementation. Since that value can’t safely cross, the compiler diagnoses the implementation under complete concurrency checking. This is an error in the Swift 6 language mode.

There are a few possible ways to address this issue.

## Use an isolated conformance

If you only need the conformance to be used from within a specific global actor isolation, you can write an isolated conformance. This means the protocol methods can only be called from that isolation, so non-Sendable values won’t need to cross between isolations. This may be especially natural when the type already has a global actor isolation.

```swift
class Plant {
    var height = 0
}

protocol PlantJournal {
    func record(plant: Plant) async
}

@MainActor
class GardenJournal: @MainActor PlantJournal {
    func record(plant: Plant) async { // OK, any caller of `record` is already on MainActor.
        print("Recorded plant at \(plant.height) cm tall")
    }
}
```

The upcoming feature `InferIsolatedConformances` will automatically infer an isolated conformance like the one above for a global-actor-isolated type, without needing to write `@MainActor` on the conformance itself.

## Make all parameters and results `Sendable`

If all the parameters and result types of the function are `Sendable`, it’s safe to send them between any isolations. Often, using a value type like a `struct` or an `enum` is the simplest choice, because they are implicitly `Sendable`. Having a different isolation in the implementation is no longer a problem:

```swift
struct Plant {
    var height = 0
}

protocol PlantJournal {
    func record(plant: Plant) async
}

@MainActor
class GardenJournal: PlantJournal {
    func record(plant: Plant) async { // OK, sending `Plant` from another isolation is safe.
        print("Recorded plant at \(plant.height) cm tall")
    }
}
```

Reference types can be made `Sendable` by an explicit `Sendable` conformance, a global actor annotation like `@MainActor`, or with `@unchecked Sendable` when the type has been made thread safe by a different synchronization mechanism like a lock or a queue.

## Match the isolation of both the protocol and the implementation

Of course, making all parameters and results `Sendable` may not always be possible. Since the problem arises when the protocol or superclass method and its implementation have different isolations, another solution is to annotate either the protocol or the implementation to use the same isolation:

```swift
class Plant {
    var height = 0
}

@MainActor
protocol PlantJournal {
    func record(plant: Plant) async
}

@MainActor
class GardenJournal: PlantJournal {
    func record(plant: Plant) async { // OK
        print("Recorded plant at \(plant.height) cm tall")
    }
}
```

This means any callers of these methods will also need to be in the same isolation. For the example above, calls to `journal.record(plant: plant)` need to be performed from a main-actor-isolated context.

## Make non-Sendable parameters or results `sending`

If the parameters or results can’t be made `Sendable`, and the implementation needs a different isolation than the protocol or superclass, it may still be possible to make those parameters or results `sending`. The compiler will ensure that crossings of a non-Sendable value into a different isolation using `sending` are safe, by making those values unavailable in their original isolation after being sent. However, since `sending` has to be declared on the requirement, it’s part of the protocol’s contract for every conformance, even ones whose isolation already matches and wouldn’t otherwise have needed it.

```swift
class Plant {
    var height = 0
}

protocol PlantJournal {
    func record(plant: sending Plant) async
}

@MainActor
class GardenJournal: PlantJournal {
    func record(plant: sending Plant) async { // OK
        print("Recorded plant at \(plant.height) cm tall")
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/non-sendable-values-in-async-conformances-and-overrides)*