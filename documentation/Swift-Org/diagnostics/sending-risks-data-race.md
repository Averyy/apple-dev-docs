---
url: "https://docs.swift.org/latest/documentation/diagnostics/sending-risks-data-race"
framework: "Swift-Org/diagnostics"
---

# Sending value risks causing data races (SendingRisksDataRace)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Sharing mutable state between concurrent tasks can cause data races in your program. Resolve this error by only accessing mutable state in one task at a time.

If a type does not conform to `Sendable` the compiler will enforce that each instance of that type is only accessed by one concurrency domain at a time. The `sending 'x' risks causing data races` error indicates that your code can access a non-`Sendable` value from multiple concurrency domains at once.

For example, if a value can be accessed from the main actor, it’s invalid to send the same instance to another concurrency domain while the main actor can still access it. This mistake is common when calling an `async` function on a class from the main actor:

```swift
class Person {
  var name: String = ""

  func printNameConcurrently() async {
    print(name)
  }
}

@MainActor
func onMainActor(person: Person) async {
  await person.printNameConcurrently()
}
```

The above code produces:

```
await person.printNameConcurrently()
            |- error: sending 'person' risks causing data races
            `- note: sending main actor-isolated 'person' to nonisolated instance method 'printNameConcurrently()' risks causing data races between nonisolated and main actor-isolated uses
```

This happens because the `printNameConcurrently` function runs off of the main actor, and the `onMainActor` function suspends while waiting for `printNameConcurrently` to complete. While suspended, the main actor can run other tasks that still have access to `person`, which can lead to a data race.

The most common fix is to change the `async` method to run on the caller’s actor using the `nonisolated(nonsending)` specifier:

```swift
class Person {
  var name: String = ""

  nonisolated(nonsending)
  func printNameConcurrently() async {
    print(name)
  }
}

@MainActor
func onMainActor(person: Person) async {
  await person.printNameConcurrently()
}
```

This eliminates the risk of data-races because `printNameConcurrently` continues to run on the main actor, so all access to `person` is serialized.

You can also enable the `NonisolatedNonsendingByDefault` upcoming feature to make `nonisolated(nonsending)` the default for async functions on non-`Sendable` types.

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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/sending-risks-data-race)*