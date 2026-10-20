# AnchorUpdateSequence

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

An asynchronous sequence of updates to anchors.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct AnchorUpdateSequence<AnchorType> where AnchorType : Anchor
```

## Topics

### Performing sequence operations
- [AnchorUpdateSequence.Iterator](./anchorupdatesequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AnchorUpdateSequence<AnchorType>.Iterator<AnchorType>](./anchorupdatesequence/makeasynciterator%28%29.md)
  Creates an asynchronous iterator that produces anchor update elements on this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../Swift/asyncsequence.md)

## See Also

### Tracking anchors over time
- [struct AnchorUpdate](./anchorupdate.md)
  Information about the event that updated an anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdatesequence)*