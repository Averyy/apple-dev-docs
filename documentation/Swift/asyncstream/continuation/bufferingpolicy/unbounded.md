# AsyncStream.Continuation.BufferingPolicy.unbounded

**Framework**: Swift  
**Kind**: case  
**Role**: Case

Continue to add to the buffer, without imposing a limit on the number of buffered elements.

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
case unbounded
```

## See Also

### Buffering Policies
- [AsyncStream.Continuation.BufferingPolicy.bufferingOldest(_:)](./bufferingoldest%28_%29.md)
  When the buffer is full, discard the newly received element.
- [AsyncStream.Continuation.BufferingPolicy.bufferingNewest(_:)](./bufferingnewest%28_%29.md)
  When the buffer is full, discard the oldest element in the buffer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/asyncstream/continuation/bufferingpolicy/unbounded)*