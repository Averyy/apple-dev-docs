# AnchorUpdateSequence.Iterator

**Framework**: ARKit  
**Kind**: struct  
**Role**: Structure

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct Iterator<TypeOfAnchor> where TypeOfAnchor : Anchor
```

## Topics

### Instance Methods
- [func next() async -> AnchorUpdateSequence<AnchorType>.Iterator<TypeOfAnchor>.Element?](./iterator/next%28%29.md)
  Asynchronously retrieve the next anchor update.

## Relationships

### Conforms To
- [AsyncIteratorProtocol](../../Swift/asynciteratorprotocol.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdatesequence/iterator)*