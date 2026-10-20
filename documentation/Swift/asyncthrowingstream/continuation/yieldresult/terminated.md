# AsyncThrowingStream.Continuation.YieldResult.terminated

**Framework**: Swift  
**Kind**: case  
**Role**: Case

The stream didn’t enqueue the element because the stream was in a terminal state.

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
case terminated
```

#### Discussion

This indicates the stream terminated prior to calling `yield`, either because the stream finished normally or through cancellation, or it threw an error.

## See Also

### Yield Results
- [AsyncThrowingStream.Continuation.YieldResult.enqueued(remaining:)](./enqueued%28remaining%29.md)
  The stream successfully enqueued the element.
- [AsyncThrowingStream.Continuation.YieldResult.dropped(_:)](./dropped%28_%29.md)
  The stream didn’t enqueue the element because the buffer was full.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncthrowingstream/continuation/yieldresult/terminated)*