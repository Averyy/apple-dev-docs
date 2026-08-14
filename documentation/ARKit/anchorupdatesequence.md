# AnchorUpdateSequence

**Framework**: ARKit  
**Kind**: struct

An asynchronous sequence of updates to anchors.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct AnchorUpdateSequence<AnchorType> where AnchorType : Anchor
```

## Topics

### Performing sequence operations
- [AnchorUpdateSequence.Iterator](anchorupdatesequence/iterator.md)
### Instance Methods
- [func makeAsyncIterator() -> AnchorUpdateSequence<AnchorType>.Iterator<AnchorType>](anchorupdatesequence/makeasynciterator.md)
  Creates an asynchronous iterator that produces `AnchorUpdate` elements on this asynchronous sequence.

## Relationships

### Conforms To
- [AsyncSequence](../swift/asyncsequence.md)

## See Also

- [struct AnchorUpdate](anchorupdate.md)
  Information about the event that updated an anchor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdatesequence)*