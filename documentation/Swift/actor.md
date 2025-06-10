# Actor

**Framework**: Swift  
**Kind**: protocol

Common protocol to which all actors conform.

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
protocol Actor : AnyObject, Sendable
```

#### Overview

The `Actor` protocol generalizes over all `actor` types. Actor types implicitly conform to this protocol.

##### Actors and Serialexecutors

By default, actors execute tasks on a shared global concurrency thread pool. This pool is shared by all default actors and tasks, unless an actor or task specified a more specific executor requirement.

It is possible to configure an actor to use a specific [`SerialExecutor`](serialexecutor.md), as well as impact the scheduling of default tasks and actors by using a [`TaskExecutor`](taskexecutor.md).

> **Note**: [`SerialExecutor`](serialexecutor.md)

> **Note**: [`TaskExecutor`](taskexecutor.md)

## Topics

### Instance Properties
- [var unownedExecutor: UnownedSerialExecutor](actor/unownedexecutor.md)
  Retrieve the executor for this actor as an optimized, unowned reference.
### Instance Methods
- [func assertIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](actor/assertisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this actor’s serial executor.
- [func assumeIsolated<T>((isolated Self) throws -> T, file: StaticString, line: UInt) rethrows -> T](actor/assumeisolated(_:file:line:).md)
  Assume that the current task is executing on this actor’s serial executor, or stop program execution otherwise.
- [func preconditionIsolated(@autoclosure () -> String, file: StaticString, line: UInt)](actor/preconditionisolated(_:file:line:).md)
  Stops program execution if the current task is not executing on this actor’s serial executor.

## Relationships

### Inherits From
- [Sendable](sendable.md)
- [SendableMetatype](sendablemetatype.md)
### Conforming Types
- [MainActor](mainactor.md)

## See Also

- [protocol Sendable](sendable.md)
  A thread-safe type whose values can be shared across arbitrary concurrent contexts without introducing a risk of data races.
- [typealias AnyActor](anyactor.md)
  Common marker protocol providing a shared “base” for both (local) `Actor` and (potentially remote) `DistributedActor` types.
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

*[View on Apple Developer](https://developer.apple.com/documentation/swift/actor)*