---
url: "https://docs.swift.org/latest/documentation/diagnostics/getting-non-sendable-values-out-of-actors"
framework: "Swift-Org/diagnostics"
---

# Getting non-Sendable values out of actors (NonSendableExitingActor)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

When an actor is used to protect a non-Sendable value, the compiler will enforce that the non-Sendable value remains in the actor instance’s isolation. Accessing an actor’s property of non-Sendable type from a different isolation will be diagnosed when complete concurrency checking is enabled. This is an error in the Swift 6 language mode.

For example:

```swift
class Plant {
    var height = 0
}

actor Terrarium {
    var label = "Yarrow"
    let plant = Plant()
}

nonisolated func growAndReport(in terrarium: Terrarium, by amount: Int) async {
    let label = await terrarium.label // Fine, `label` is Sendable.
    let plant = await terrarium.plant // error: non-Sendable type 'Plant' of property 'plant' cannot exit actor-isolated context
    plant.height += amount
    print("\(label) is now \(plant.height) cm tall")
}
```

Non-Sendable types in actor-isolated properties can’t be safely accessed concurrently, even when declared with `let`. This is because a `let` declaration can hold a type with internal mutable state, like `Plant`‘s `height` in the above example. Letting a `Plant` reference exit the `Terrarium` instance’s isolation would allow concurrent mutation, which is a data race.

A useful pattern when working with actors is to only use `Sendable` types to get information in and out of the actor. You may be able to achieve this by writing the functions directly in the actor:

```swift
class Plant {
    var height = 0
}

actor Terrarium {
    var label = "Yarrow"
    let plant = Plant()

    func growAndReport(by amount: Int) { // amount is an Int, which is Sendable
        plant.height += amount // OK
        print("\(label) is now \(plant.height) cm tall")
    }
}
```

Or, if using a global actor like `@MainActor`, by isolating the functions that access the non-Sendable values to that global actor, so those values never have to leave their isolation:

```swift
class Plant {
    var height = 0
}

@MainActor
final class Terrarium {
    var label = "Yarrow"
    let plant = Plant()
}

@MainActor
func growAndReport(in terrarium: Terrarium, by amount: Int) {
    let plant = terrarium.plant // OK
    plant.height += amount
    print("\(terrarium.label) is now \(plant.height) cm tall")
}
```

By moving entire functions into actor-isolated code, you may also be able to reduce the number of suspension points, or even make the function synchronous. This can result in simpler code, as the compiler guarantees that no other code can modify the actor-protected state while you are running code synchronously on that actor.

Once you’re willing to reconsider which isolation `Terrarium` belongs to, as in the `@MainActor` example above, it’s worth also considering whether `Terrarium` needs isolation at all. In some cases your type may already be used without being sent, and does not need to be `Sendable` or isolated. The compiler will still ensure callers of `Terrarium` protect it, pushing the problem up a level:

```swift
class Plant {
    var height = 0
}

class Terrarium {
    var label = "Yarrow"
    let plant = Plant()
}

nonisolated func growAndReport(in terrarium: Terrarium, by amount: Int) {
    let label = terrarium.label
    let plant = terrarium.plant
    plant.height += amount
    print("\(label) is now \(plant.height) cm tall")
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/getting-non-sendable-values-out-of-actors)*