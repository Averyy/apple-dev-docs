# AnchorUpdate

**Framework**: ARKit  
**Kind**: struct

Information about the event that updated an anchor.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
struct AnchorUpdate<AnchorType> where AnchorType : Anchor
```

## Topics

### Inspecting anchor updates
- [let anchor: AnchorType](anchorupdate/anchor.md)
  The anchor that this anchor update contains information about.
- [var timestamp: TimeInterval](anchorupdate/timestamp.md)
  The time when this anchor update occurred.
- [let event: AnchorUpdate<AnchorType>.Event](anchorupdate/event-swift.property.md)
  The event which caused the anchor to update.
- [AnchorUpdate.Event](anchorupdate/event-swift.enum.md)
  An event that indicates whether an anchor was added, updated, or removed.
- [var description: String](anchorupdate/description.md)
  A textual representation of this anchor update.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct AnchorUpdateSequence](anchorupdatesequence.md)
  An asynchronous sequence of updates to anchors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdate)*