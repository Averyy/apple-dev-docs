# AsyncThrowingStream.Continuation.YieldResult

**Framework**: Swift  
**Kind**: enum

A type that indicates the result of yielding a value to a client, by way of the continuation.

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
enum YieldResult
```

#### Overview

The various `yield` methods of `AsyncThrowingStream.Continuation` return this type to indicate the success or failure of yielding an element to the continuation.

## Topics

### Yield Results
- [AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)](asyncthrowingstream/continuation/yieldresult/enqueued(remaining:).md)
  The stream successfully enqueued the element.
- [AsyncThrowingStream.Continuation.YieldResult.dropped(_:)](asyncthrowingstream/continuation/yieldresult/dropped(_:).md)
  The stream didn’t enqueue the element because the buffer was full.
- [AsyncThrowingStream.Continuation.YieldResult.terminated](asyncthrowingstream/continuation/yieldresult/terminated.md)
  The stream didn’t enqueue the element because the stream was in a terminal state.

## Relationships

### Conforms To
- [Sendable](sendable.md)

## See Also

- [func yield(sending Element) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](asyncthrowingstream/continuation/yield(_:).md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [func yield(with: sending Result<Element, Failure>) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](asyncthrowingstream/continuation/yield(with:).md)
  Resume the task awaiting the next iteration point by having it return normally or throw, based on a given result.
- [func yield() -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](asyncthrowingstream/continuation/yield.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yieldresult)*