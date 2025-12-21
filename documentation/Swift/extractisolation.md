# extractIsolation(_:)

**Framework**: Swift  
**Kind**: func

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
func extractIsolation<each Arg, Result>(_ fn: @escaping @isolated(any) (repeat each Arg) async throws -> Result) -> (any Actor)?
```

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
  A type whose metatype can be shared across arbitrary concurrent contexts without introducing a risk of data races. When a generic type `T` conforms to `SendableMetatype`, its metatype `T.Type` conforms to `Sendable`.  All concrete types implicitly conform to the `SendableMetatype` protocol, so its primary purpose is in generic code to prohibit the use of isolated conformances along with the generic type.
- [typealias ConcurrentValue](concurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [macro isolation<T>() -> T](isolation().md)
  Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/extractisolation(_:))*