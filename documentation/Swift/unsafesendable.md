# UnsafeSendable

**Framework**: Swift  
**Kind**: protocol

A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+
- Unknown ?+ - Deprecated
- Mac Catalyst 13.0+

## Declaration

```swift
protocol UnsafeSendable : Sendable
```

#### Overview

Use an unchecked conformance to `Sendable` instead — for example:

```swift
struct MyStructure: @unchecked Sendable { ... }
```

## Relationships

### Inherits From
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)

## See Also

- [protocol Sendable](sendable.md)
  A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [protocol Actor](actor.md)
  Common protocol to which all actors conform.
- [typealias AnyActor](anyactor.md)
  Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.
- [actor MainActor](mainactor.md)
  A singleton actor whose executor is equivalent to the main dispatch queue.
- [protocol GlobalActor](globalactor.md)
  A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [protocol SendableMetatype](sendablemetatype.md)
  A type `T` whose metatype `T.Type` is `Sendable`.
- [typealias ConcurrentValue](concurrentvalue.md)
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [macro isolation<T>() -> T](isolation().md)
  Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/unsafesendable)*