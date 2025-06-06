# AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)

**Framework**: Swift  
**Kind**: case

The stream successfully enqueued the element.

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
case enqueued(remaining: Int)
```

#### Discussion

This value represents the successful enqueueing of an element, whether the stream buffers the element or delivers it immediately to a pending call to `next()`. The associated value `remaining` is a hint that indicates the number of remaining slots in the buffer at the time of the `yield` call.

> **Note**: From a thread safety perspective, `remaining` is a lower bound on the number of remaining slots. This is because a subsequent call that uses the `remaining` value could race on the consumption of values from the stream.

From a thread safety perspective, `remaining` is a lower bound on the number of remaining slots. This is because a subsequent call that uses the `remaining` value could race on the consumption of values from the stream.

## See Also

- [AsyncThrowingStream.Continuation.YieldResult.dropped(_:)](asyncthrowingstream/continuation/yieldresult/dropped(_:).md)
  The stream didn’t enqueue the element because the buffer was full.
- [AsyncThrowingStream.Continuation.YieldResult.terminated](asyncthrowingstream/continuation/yieldresult/terminated.md)
  The stream didn’t enqueue the element because the stream was in a terminal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yieldresult/enqueued(remaining:))*