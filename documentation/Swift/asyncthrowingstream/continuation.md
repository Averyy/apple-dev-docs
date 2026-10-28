# AsyncThrowingStream.Continuation

**Framework**: Swift  
**Kind**: struct  
**Role**: Structure

A mechanism to interface between synchronous code and an asynchronous stream.

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
struct Continuation
```

## Overview

The closure you provide to the `AsyncThrowingStream` in `init(_:bufferingPolicy:_:)` receives an instance of this type when invoked. Use this continuation to provide elements to the stream by calling one of the `yield` methods, then terminate the stream normally by calling the `finish()` method. You can also use the continuation’s `finish(throwing:)` method to terminate the stream by throwing an error.

> **Note**: Unlike other continuations in Swift, `AsyncThrowingStream.Continuation` supports escaping.

## Topics

### Producing Elements
- [func yield(sending Element) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./continuation/yield%28_%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [func yield(with: sending Result<Element, Failure>) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./continuation/yield%28with%29.md)
  Resume the task awaiting the next iteration point by having it return normally or throw, based on a given result.
- [func yield() -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./continuation/yield%28%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [AsyncThrowingStream.Continuation.YieldResult](./continuation/yieldresult.md)
  A type that indicates the result of yielding a value to a client, by way of the continuation.
### Finishing the Stream
- [func finish(throwing: Failure?)](./continuation/finish%28throwing%29.md)
  Resume the task awaiting the next iteration point by having it return nil, which signifies the end of the iteration.
### Handling Termination
- [var onTermination: ((AsyncThrowingStream<Element, Failure>.Continuation.Termination) -> Void)?](./continuation/ontermination.md)
  A callback to invoke when canceling iteration of an asynchronous stream.
- [AsyncThrowingStream.Continuation.Termination](./continuation/termination.md)
  A type that indicates how the stream terminated.
### Enumerations
- [AsyncThrowingStream.Continuation.BufferingPolicy](./continuation/bufferingpolicy.md)
  A strategy that handles exhaustion of a buffer’s capacity.
### Default Implementations
- [Equatable Implementations](./continuation/equatable-implementations.md)
- [Hashable Implementations](./continuation/hashable-implementations.md)

## Relationships

### Conforms To
- [Equatable](../equatable.md)
- [Hashable](../hashable.md)
- [Sendable](../sendable.md)
- [SendableMetatype](../sendablemetatype.md)

## See Also

### Creating a Continuation-Based Stream
- [init(Element.Type, bufferingPolicy: AsyncThrowingStream<Element, Failure>.Continuation.BufferingPolicy, (AsyncThrowingStream<Element, Failure>.Continuation) -> Void)](./init%28_,bufferingpolicy,_%29.md)
  Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [AsyncThrowingStream.Continuation.BufferingPolicy](./continuation/bufferingpolicy.md)
  A strategy that handles exhaustion of a buffer’s capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation)*