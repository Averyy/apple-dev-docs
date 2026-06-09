# AnchorUpdateSequence.Iterator

**Framework**: ARKit  
**Kind**: struct

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Iterator<TypeOfAnchor> where TypeOfAnchor : Anchor
```

## Topics

### Instance Methods
- [func next() async -> AnchorUpdateSequence<AnchorType>.Iterator<TypeOfAnchor>.Element?](anchorupdatesequence/iterator/next.md)
  Asynchronously retrieve the next anchor update.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../Swift/AsyncIteratorProtocol.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdatesequence/iterator)*