---
url: "https://docs.swift.org/latest/documentation/diagnostics/actor-isolated-mutating-async"
framework: "Swift-Org/diagnostics"
---

# Calling a mutating async actor-isolated method (ActorIsolatedMutatingAsync)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

Calling a mutating async method on actor-isolated state allows concurrent access to that state during mutation, risking data races. To resolve this error, copy the state to a local variable, call the mutating async method on the copy, then write it back. This will overwrite concurrent changes.

For example:

```swift
struct Backpack {
  var snacks = 5
  mutating func refill() async {
    snacks += await purchaseSnacks(current: snacks)
  }
}

@MainActor
class Hiker {
  var backpack = Backpack()

  func getReady() async {
    await backpack.refill()
  }

  func eatSnack() {
    backpack.snacks -= 1
  }
}
```

Building the above code produces an error about calling a mutating async function on an actor-isolated property:

```
|   func getReady() async {
|     await backpack.refill()
|           |        `- error: cannot call mutating async function 'refill()' on actor-isolated property 'backpack' [#ActorIsolatedMutatingAsync]
|           `- note: 'backpack' can be concurrently accessed during mutation, risking data races
|   }
```

A `mutating async` function takes `self` as `inout`. This means that the value of `backpack` will be copied into `refill`, then copied out when the method returns. `inout` requires exclusive access for the duration of the call. While `refill` is suspended, the main actor is free to do other work. This is a data race, since `refill` is still mutating `backpack`. If `eatSnack` ran before `refill` finished, it would decrement `snacks`, but the eaten snack reappears when `refill` writes back the stale copy.

```swift
// Task 1: getReady()                  | // Task 2
await backpack.refill()
// copies backpack (snacks: 5)         |
// suspends...                         |
                                         eatSnack()
//                                     | // backpack.snacks is now 4
// resumes                             |
// purchaseSnacks returns 0            |
// writes back backpack (snacks: 5)    |
// backpack.snacks is 5                |
// eatSnack() was silently lost!       |
```

When possible, you can structure code to avoid the need for mutating async functions by separating async computation and mutation:

```swift
func getReady() async {
  // await the asynchronous computation
  let refill = await backpack.computeRefill()
  // apply the mutation synchronously
  backpack.apply(refill)
}
```

Because the mutation is synchronous, no concurrent changes can occur between reading and writing `backpack` as part of `apply`. If `eatSnack` is called concurrently while `computeRefill` is suspended, the `Hiker` may purchase too few snacks, but the decrement from eating a snack won’t be lost.

If restructuring isn’t appropriate, copy `backpack` to a local variable to make the potential overwrite explicit at the call site. This way, the call site shows that `backpack` is overwritten after `await`, rather than happening implicitly due to `inout`. Because `copy` is a local variable, it is not shared with other tasks and can be safely mutated.

```swift
func getReady() async {
  var copy = backpack
  await copy.refill()
  backpack = copy
}
```

## See also

- [In-Out Parameters](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/declarations#In-Out-Parameters)
- [Overlapping accesses, but operation requires exclusive access (ExclusivityViolation)](./exclusivity-violation.md.md)

## See Also

- [@dynamicCallable implementation requirements (DynamicCallable)](./dynamic-callable-requirements.md)
- [Add @preconcurrency import (AddPreconcurrencyImport)](./add-preconcurrency-import.md)
- [Always enabled availability domains (AlwaysAvailableDomain)](./always-available-domain.md)
  Warnings that identify `@available` attributes and `if #available` statements that reference custom availability domains which have been permanently enabled.
- [Argument matching for trailing closures (TrailingClosureMatching)](./trailing-closure-matching.md)
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
- [Explicit `Sendable` annotations on public type declarations (ExplicitSendable)](./explicit-sendable-annotations.md)
  Adds a warning for any public types without a `Sendable` annotation.


---

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/actor-isolated-mutating-async)*