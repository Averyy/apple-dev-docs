# AnyActor

**Framework**: Swift  
**Kind**: typealias

Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
typealias AnyActor = AnyObject & Sendable
```

#### Discussion

The `AnyActor` marker protocol generalizes over all actor types, including distributed ones. In practice, this protocol can be used to restrict protocols, or generic parameters to only be usable with actors, which provides the guarantee that calls may be safely made on instances of given type without worrying about the thread-safety of it – as they are guaranteed to follow the actor-style isolation semantics.

While both local and distributed actors are conceptually “actors”, there are some important isolation model differences between the two, which make it impossible for one to refine the other.

## See Also

- [protocol Sendable](sendable.md)
  A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [protocol Actor](actor.md)
  Common protocol to which all actors conform.
- [actor MainActor](mainactor.md)
  A singleton actor whose executor is equivalent to the main dispatch queue.
- [protocol GlobalActor](globalactor.md)
  A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [protocol SendableMetatype](sendablemetatype.md)
  A type `T` whose metatype `T.Type` is `Sendable`.
- [typealias ConcurrentValue](concurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [macro isolation<T>() -> T](isolation().md)
  Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/anyactor)*