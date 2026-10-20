# AnchorUpdate.Event

**Framework**: ARKit  
**Kind**: enum  
**Role**: Enumeration

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
- [AnchorUpdate.Event.added](./event-swift.enum/added.md)
  An event that occurs when ARKit starts tracking an anchor.
- [AnchorUpdate.Event.updated](./event-swift.enum/updated.md)
  An event that occurs when an existing anchor updates data.
- [AnchorUpdate.Event.removed](./event-swift.enum/removed.md)
  An event that occurs when ARKit stops tracking an anchor.
### Instance Properties
- [var description: String](./event-swift.enum/description.md)
  A textual representation of this anchor update event.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting anchor updates
- [let anchor: AnchorType](./anchor.md)
  The anchor that this anchor update contains information about.
- [var timestamp: TimeInterval](./timestamp.md)
  The time when this anchor update occurred.
- [let event: AnchorUpdate<AnchorType>.Event](./event-swift.property.md)
  The event which caused the anchor to update.
- [var description: String](./description.md)
  A textual representation of this anchor update.


---

*[View on Apple Developer](https://developer.apple.com/documentation/arkit/anchorupdate/event-swift.enum)*