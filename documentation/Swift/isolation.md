# isolation()

**Framework**: Swift  
**Kind**: macro

Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
@freestanding
(expression) macro isolation<T>() -> T
```

#### Overview

If the type annotation provided for `#isolation` is not `(any Actor)?`, the type must match the enclosing actor type. If no type annotation is provided, the type defaults to `(any Actor)?`.

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
- [typealias ConcurrentValue](concurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/isolation())*