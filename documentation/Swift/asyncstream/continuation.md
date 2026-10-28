# AsyncStream.Continuation

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

The closure you provide to the `AsyncStream` in `init(_:bufferingPolicy:_:)` receives an instance of this type when invoked. Use this continuation to provide elements to the stream by calling one of the `yield` methods, then terminate the stream normally by calling the `finish()` method.

> **Note**: Unlike other continuations in Swift, `AsyncStream.Continuation` supports escaping.

## Topics

### Producing Elements
- [func yield(sending Element) -> AsyncStream<Element>.Continuation.YieldResult](./continuation/yield%28_%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [func yield(with: sending Result<Element, Never>) -> AsyncStream<Element>.Continuation.YieldResult](./continuation/yield%28with%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given result’s success value.
- [func yield() -> AsyncStream<Element>.Continuation.YieldResult](./continuation/yield%28%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [AsyncStream.Continuation.YieldResult](./continuation/yieldresult.md)
  A type that indicates the result of yielding a value to a client, by way of the continuation.
### Finishing the Stream
- [func finish()](./continuation/finish%28%29.md)
  Resume the task awaiting the next iteration point by having it return nil, which signifies the end of the iteration.
### Handling Termination
- [var onTermination: ((AsyncStream<Element>.Continuation.Termination) -> Void)?](./continuation/ontermination.md)
  A callback to invoke when canceling iteration of an asynchronous stream.
- [AsyncStream.Continuation.Termination](./continuation/termination.md)
  A type that indicates how the stream terminated.
### Enumerations
- [AsyncStream.Continuation.BufferingPolicy](./continuation/bufferingpolicy.md)
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
- [init(Element.Type, bufferingPolicy: AsyncStream<Element>.Continuation.BufferingPolicy, (AsyncStream<Element>.Continuation) -> Void)](./init%28_,bufferingpolicy,_%29.md)
  Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [AsyncStream.Continuation.BufferingPolicy](./continuation/bufferingpolicy.md)
  A strategy that handles exhaustion of a buffer’s capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation)*