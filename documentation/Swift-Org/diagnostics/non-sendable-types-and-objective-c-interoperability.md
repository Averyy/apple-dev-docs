---
url: "https://docs.swift.org/latest/documentation/diagnostics/non-sendable-types-and-objective-c-interoperability"
framework: "Swift-Org/diagnostics"
---

# Non-Sendable types and Objective-C interoperability (NonSendableObjCInterop)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Actor-isolated methods that are `async` can be exposed to Objective-C using `@objc`. These methods are imported into Objective-C with a completion handler parameter. When Objective-C code calls any of these methods, an unstructured task is created that calls the `async` Swift method in the actor’s isolation and eventually forwards the results to the completion handler.

Since Objective-C does not have knowledge of actor isolation, any types involved in the method’s signature —either as parameters or as results— are crossing an actor boundary, and are required to be `Sendable`. Otherwise, the crossing will be diagnosed under complete concurrency checking. This is an error in the Swift 6 language mode.

For example:

```swift
@objc
class Succulent: NSObject {
    var waterLevel = 0
}

actor Nursery: NSObject {
    var storedSucculent = Succulent()

    @objc
    func getSucculent() async -> Succulent { // error: non-Sendable type 'Succulent' returned by actor-isolated '@objc' instance method 'getSucculent()' cannot cross actor boundary
        return storedSucculent
    }

    @objc
    func setSucculent(to succulent: Succulent) async { // error: non-Sendable parameter type 'Succulent' of actor-isolated '@objc' instance method 'setSucculent(to:)' cannot cross actor boundary
        storedSucculent = succulent
    }
}
```

Here, `getSucculent() async` provides a non-Sendable `Succulent` type back to Objective-C, but the Objective-C code receiving the `Succulent` is not in the actor instance’s isolation, which means that an isolation boundary is crossed. Similarly, `setSucculent(to succulent: Succulent) async` is passing a `Succulent` from Objective-C code (which can’t be isolated to the `Nursery` actor instance) into the instance’s isolation, which also means an isolation boundary is crossed. This is not safe for non-Sendable types.

There are a few possible ways to address this issue.

#### Make all parameters and results `Sendable`

If all the parameters and result types of the method are `Sendable`, it’s safe to send them across any isolation boundaries.

```swift
@objc
final class Succulent: NSObject, Sendable {
    let waterLevel = 0
}

actor Nursery: NSObject {
    var storedSucculent = Succulent()

    @objc func getSucculent() async -> Succulent { // OK
        return storedSucculent
    }

    @objc func setSucculent(to succulent: Succulent) async { // OK
        storedSucculent = succulent
    }
}
```

Types can be made `Sendable` by an explicit `Sendable` conformance, a `@MainActor` annotation, or with `@unchecked Sendable` when the type has been made thread safe by a different synchronization mechanism like a lock or a queue.

#### Use a global actor like `@MainActor`

Another solution is to use a global actor (like `@MainActor`) instead of an actor’s instance to protect mutable state that needs to be accessed from Objective-C:

```swift
@objc
class Succulent: NSObject {
    var waterLevel = 0
}

@MainActor
final class Nursery: NSObject {
    var storedSucculent = Succulent()

    @objc func getSucculent() async -> Succulent { // OK
        return storedSucculent
    }

    @objc func setSucculent(to succulent: Succulent) async { // OK
        storedSucculent = succulent
    }
}
```

However, on the Objective-C side, care must be taken to only call these methods from the global actor’s executor. For the main actor, that means only calling these methods from the main thread.

#### Make non-Sendable parameters or results `sending`

If the parameters or results can’t be made `Sendable`, and the implementation needs to be isolated to an actor instance (which Objective-C won’t be aware of), it may still be possible to make those parameters or results `sending` if care is taken. For Swift code, the compiler will ensure that crossings of a non-Sendable value into a different isolation using `sending` are safe, by making those values unavailable in their original isolation after being sent. However, this cannot be checked for Objective-C, so extreme care needs to be taken that values passed to `sending` parameters are never used after being sent. This may be very difficult to ensure without copying the value and sending the copy. Using a value in Objective-C after passing it to a `sending` parameter may lead to data races.

## See Also

### Related Documentation
- [TaskLocal](https://developer.apple.com/documentation/swift/tasklocal)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/non-sendable-types-and-objective-c-interoperability)*