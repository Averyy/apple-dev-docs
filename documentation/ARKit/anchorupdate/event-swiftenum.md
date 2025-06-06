# AnchorUpdate.Event

**Framework**: ARKit  
**Kind**: enum

An event that indicates whether an anchor was added, updated, or removed.

**Availability**:
- visionOS 1.0+

## Declaration

```swift
@frozen
enum Event
```

## Topics

### Inspecting anchor update events
- [AnchorUpdate.Event.added](anchorupdate/event-swift.enum/added.md)
  An event that occurs when ARKit starts tracking an anchor.
- [AnchorUpdate.Event.updated](anchorupdate/event-swift.enum/updated.md)
  An event that occurs when an existing anchor updates data.
- [AnchorUpdate.Event.removed](anchorupdate/event-swift.enum/removed.md)
  An event that occurs when ARKit stops tracking an anchor.
### Instance Properties
- [var description: String](anchorupdate/event-swift.enum/description.md)
  A textual representation of AnchorUpdate.Event

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [let anchor: AnchorType](anchorupdate/anchor.md)
  The anchor that this anchor update contains information about.
- [var timestamp: TimeInterval](anchorupdate/timestamp.md)
  The time when this anchor update occurred.
- [let event: AnchorUpdate<AnchorType>.Event](anchorupdate/event-swift.property.md)
  The event which caused the anchor to update.
- [var description: String](anchorupdate/description.md)
  A textual representation of this anchor update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdate/event-swift.enum)*