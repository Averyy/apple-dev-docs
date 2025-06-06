# AsyncStream.Continuation

**Framework**: Swift  
**Kind**: struct

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

#### Overview

The closure you provide to the `AsyncStream` in `init(_:bufferingPolicy:_:)` receives an instance of this type when invoked. Use this continuation to provide elements to the stream by calling one of the `yield` methods, then terminate the stream normally by calling the `finish()` method.

> **Note**: Unlike other continuations in Swift, `AsyncStream.Continuation` supports escaping.

## Topics

### Producing Elements
- [func yield(sending Element) -> AsyncStream<Element>.Continuation.YieldResult](asyncstream/continuation/yield(_:).md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [func yield(with: sending Result<Element, Never>) -> AsyncStream<Element>.Continuation.YieldResult](asyncstream/continuation/yield(with:).md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given result’s success value.
- [func yield() -> AsyncStream<Element>.Continuation.YieldResult](asyncstream/continuation/yield.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point.
- [AsyncStream.Continuation.YieldResult](asyncstream/continuation/yieldresult.md)
  A type that indicates the result of yielding a value to a client, by way of the continuation.
### Finishing the Stream
- [func finish()](asyncstream/continuation/finish.md)
  Resume the task awaiting the next iteration point by having it return nil, which signifies the end of the iteration.
### Handling Termination
- [var onTermination: ((AsyncStream<Element>.Continuation.Termination) -> Void)?](asyncstream/continuation/ontermination.md)
  A callback to invoke when canceling iteration of an asynchronous stream.
- [AsyncStream.Continuation.Termination](asyncstream/continuation/termination.md)
  A type that indicates how the stream terminated.
### Enumerations
- [AsyncStream.Continuation.BufferingPolicy](asyncstream/continuation/bufferingpolicy.md)
  A strategy that handles exhaustion of a buffer’s capacity.

## Relationships

### Conforms To
- [Sendable](sendable.md)

## See Also

- [init(Element.Type, bufferingPolicy: AsyncStream<Element>.Continuation.BufferingPolicy, (AsyncStream<Element>.Continuation) -> Void)](asyncstream/init(_:bufferingpolicy:_:).md)
  Constructs an asynchronous stream for an element type, using the specified buffering policy and element-producing closure.
- [AsyncStream.Continuation.BufferingPolicy](asyncstream/continuation/bufferingpolicy.md)
  A strategy that handles exhaustion of a buffer’s capacity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation)*