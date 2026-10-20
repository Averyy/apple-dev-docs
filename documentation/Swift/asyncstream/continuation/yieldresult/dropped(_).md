# AsyncStream.Continuation.YieldResult.dropped(_:)

**Framework**: Swift  
**Kind**: case  
**Role**: Case

The stream didn’t enqueue the element because the buffer was full.

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
case dropped(Element)
```

#### Discussion

The associated element for this case is the element dropped by the stream.

## See Also

### Yield Results
- [AsyncStream.Continuation.YieldResult.enqueued(remaining:)](./enqueued%28remaining%29.md)
  The stream successfully enqueued the element.
- [AsyncStream.Continuation.YieldResult.terminated](./terminated.md)
  The stream didn’t enqueue the element because the stream was in a terminal state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/yieldresult/dropped(_:))*