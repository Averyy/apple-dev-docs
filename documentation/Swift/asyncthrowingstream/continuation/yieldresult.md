# AsyncThrowingStream.Continuation.YieldResult

**Framework**: Swift  
**Kind**: enum  
**Role**: Enumeration

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
- [AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)](./yieldresult/enqueued%28remaining%29.md)
  The stream successfully enqueued the element.
- [AsyncThrowingStream.Continuation.YieldResult.dropped(_:)](./yieldresult/dropped%28_%29.md)
  The stream didn’t enqueue the element because the buffer was full.
- [AsyncThrowingStream.Continuation.YieldResult.terminated](./yieldresult/terminated.md)
  The stream didn’t enqueue the element because the stream was in a terminal state.

## Relationships

### Conforms To
- [Sendable](../../sendable.md)
- [SendableMetatype](../../sendablemetatype.md)

## See Also

### Producing Elements
- [func yield(sending Element) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./yield%28_%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point with a given element.
- [func yield(with: sending Result<Element, Failure>) -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./yield%28with%29.md)
  Resume the task awaiting the next iteration point by having it return normally or throw, based on a given result.
- [func yield() -> AsyncThrowingStream<Element, Failure>.Continuation.YieldResult](./yield%28%29.md)
  Resume the task awaiting the next iteration point by having it return normally from its suspension point.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yieldresult)*