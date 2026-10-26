---
url: "https://docs.swift.org/latest/documentation/diagnostics/mutable-global-variable"
framework: "Swift-Org/diagnostics"
---

# Unsafe mutable global and static variables (MutableGlobalVariable)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

#### Overview

Mutable global and static variables that can be accessed from anywhere can cause data races in your program. Resolve this error by making the state immutable or protecting it with a global actor.

Concurrency checking prohibits mutable global and static variables that are `nonisolated` because they can be accessed from arbitrary concurrency domains at once and lead to data races.

For example:

```swift
struct Constants {
  static var value = 10
}
```

Building this code with complete concurrency checking will point out the unsafe static variable:

```
| struct Constants {
|   static var value = 10
|              |- error: static property 'value' is not concurrency-safe because it is nonisolated global shared mutable state
|              |- note: convert 'value' to a 'let' constant to make 'Sendable' shared state immutable
|              |- note: add '@MainActor' to make static property 'value' part of global actor 'MainActor'
|              `- note: disable concurrency-safety checks if accesses are protected by an external synchronization mechanism
```

If the type of the variable conforms to `Sendable` and the value is never changed, a common fix is to change the `var` to a `let` to make the state immutable. Immutable state is safe to access concurrently!

If you carefully access the global variable in a way that cannot cause data races, such as by wrapping all accesses in an external synchronization mechanism like a lock or a dispatch queue, you can apply `nonisolated(unsafe)` to opt out of concurrency checking:

```swift
  nonisolated(unsafe) static var value = 10
```

Now consider a static variable with a type that does not conform to `Sendable`:

```swift
class MyModel {
  static let shared = MyModel()

  // mutable state
}
```

This code is also diagnosed under complete concurrency checking. Even though the `shared` variable is a `let` constant, the `MyModel` type is not `Sendable`, so it could have mutable stored properties. A common fix in this case is to isolate the variable to the main actor:

```swift
class MyModel {
  @MainActor
  static let shared = MyModel()
}
```

Alternatively, isolate the `MyModel` class to the main actor, which will also make the type `Sendable` because the main actor protects access to all mutable state:

```swift
@MainActor
class MyModel {
  static let shared = MyModel()
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/mutable-global-variable)*