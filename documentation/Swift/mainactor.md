# MainActor

**Framework**: Swift  
**Kind**: class

A singleton actor whose executor is equivalent to the main dispatch queue.

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
@globalActor
final actor MainActor
```

## Topics

### Instance Properties
- [var unownedExecutor: UnownedSerialExecutor](mainactor/unownedexecutor.md)
  Retrieve the executor for this actor as an optimized, unowned reference.
### Instance Methods
- [func enqueue(UnownedJob)](mainactor/enqueue(_:).md)
### Type Aliases
- [MainActor.ActorType](mainactor/actortype.md)
  The type of the shared actor instance that will be used to provide mutually-exclusive access to declarations annotated with the given global actor type.
### Type Properties
- [static let shared: MainActor](mainactor/shared.md)
  The shared actor instance that will be used to provide mutually-exclusive access to declarations annotated with the given global actor type.
- [static var sharedUnownedExecutor: UnownedSerialExecutor](mainactor/sharedunownedexecutor.md)
  Shorthand for referring to the `shared.unownedExecutor` of this global actor.
### Type Methods
- [static func assumeIsolated<T>(() throws -> T, file: StaticString, line: UInt) rethrows -> T](mainactor/assumeisolated(_:file:line:).md)
  Assume that the current task is executing on the main actor’s serial executor, or stop program execution.
- [static func run<T>(resultType: T.Type, body: () throws -> T) async rethrows -> T](mainactor/run(resulttype:body:).md)
  Execute the given body closure on the main actor.
### Default Implementations
- [Actor Implementations](mainactor/actor-implementations.md)
- [GlobalActor Implementations](mainactor/globalactor-implementations.md)

## Relationships

### Conforms To
- [Actor](actor.md)
- [GlobalActor](globalactor.md)
- [Sendable](sendable.md)

## See Also

- [protocol Sendable](sendable.md)
  A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [protocol Actor](actor.md)
  Common protocol to which all actors conform.
- [typealias AnyActor](anyactor.md)
  Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.
- [protocol GlobalActor](globalactor.md)
  A type that represents a globally-unique actor that can be used to isolate various declarations anywhere in the program.
- [typealias ConcurrentValue](concurrentvalue.md)
- [protocol UnsafeSendable](unsafesendable.md)
  A type whose values can safely be passed across concurrency domains by copying, but which disables some safety checking at the conformance site.
- [typealias UnsafeConcurrentValue](unsafeconcurrentvalue.md)
- [macro isolation<T>() -> T](isolation().md)
  Produce a reference to the actor to which the enclosing code is isolated, or `nil` if the code is nonisolated.
- [func extractIsolation<each Arg, Result>((repeat each Arg) async throws -> Result) -> (any Actor)?](extractisolation(_:).md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/mainactor)*