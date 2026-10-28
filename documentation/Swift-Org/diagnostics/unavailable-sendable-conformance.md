---
url: "https://docs.swift.org/latest/documentation/diagnostics/unavailable-sendable-conformance"
framework: "Swift-Org/diagnostics"
---

# Unavailable Sendable conformance (UnavailableSendableConformance)

**Framework**: Swift-Org/diagnostics  
**Role**: Article

## Overview

An unavailable sendable conformance is an explicit prohibition on conforming to `Sendable`. It is declared by marking the conformance `unavailable` with the `available` attribute. Like other conformances, unavailable conformances are inherited by subclasses. Providing an unavailable conformance to the `Sendable` protocol states that a type and its subclasses must not conform to `Sendable`:

```swift
class ImageLoader {}

@available(*, unavailable)
extension ImageLoader: Sendable {}
```

Suppose you subclass a type with an unavailable `Sendable` conformance:

```swift
final class ThumbnailLoader: ImageLoader, @unchecked Sendable {}
```

This results in a warning like:

```
| final class ThumbnailLoader: ImageLoader, @unchecked Sendable {}
|             |                                        `- warning: 'ThumbnailLoader' inherits an unavailable 'Sendable' conformance; conforming here risks data races
|             `- note: 'ThumbnailLoader' inherits unavailable conformance to protocol 'Sendable' from superclass here
```

An unavailable `Sendable` conformance means the type does not meet the criteria for `Sendable`, so it would not be safe to treat it or any subclass as `Sendable`. Suppose `ImageLoader` comes from a library with mutable implementation details like an unsynchronized cache, which makes it unsafe to send, so the library author used an unavailable conformance to ensure it’s never treated as `Sendable`. Sharing an `ImageLoader` between concurrency domains would be a data race. Your `ThumbnailLoader` subclass inherits these implementation details, so it must not be marked `Sendable` either.

These rules also apply to extensions of types; you shouldn’t extend a type to conform to `Sendable` when it was defined with an unavailable `Sendable` conformance. Treating a non-`Sendable` type as `Sendable` will prevent enforcing race safety.

## Suppressed conformances

By writing `~Sendable`, a type can suppress inferred `Sendable` conformance without preventing subclasses from adding protections for state and conforming to `Sendable`. A superclass can also use `~Sendable` to let subclasses choose whether to be `Sendable`.

```swift
class ImageLoader: ~Sendable {
  // Not thread safe.
}

final class ThreadSafeImageLoader: ImageLoader, @unchecked Sendable {
  // Protects state from ImageLoader in some way that makes it safe to access i.e. via a lock.
}
```

## Sendable wrapper

To resolve this warning, instead of trying to make a non-`Sendable` type conform to `Sendable`, create a `Sendable` wrapper that ensures exclusive access, or wrap the type in a `Mutex`, which is `Sendable`.

```swift
actor SendableImageLoader {
  let loader: ImageLoader
  // ...
}
```

## See Also

### Related Documentation
- [Sendable Types](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/concurrency/#Sendable-Types)
- [Implicit Conformance to a Protocol](https://docs.swift.org/swift-book/documentation/the-swift-programming-language/protocols/#Implicit-Conformance-to-a-Protocol)
- [SE-0518: ~Sendable for explicitly marking non-Sendable types](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0518-tilde-sendable.md)
- [SE-0337: Incremental migration to concurrency checking](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0337-support-incremental-migration-to-concurrency-checking.md#sendable-conformance-status)
- [SE-0364: Warning for Retroactive Conformances of External Types](https://github.com/swiftlang/swift-evolution/blob/main/proposals/0364-retroactive-conformance-warning.md)
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

*[View on docs.swift.org](https://docs.swift.org/latest/documentation/diagnostics/unavailable-sendable-conformance)*