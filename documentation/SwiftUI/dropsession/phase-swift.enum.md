# DropSession.Phase

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

The phase of the current drop session.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
enum Phase
```

## Topics

### Enumeration Cases
- [DropSession.Phase.active](./phase-swift.enum/active.md)
  The drop session is active inside the drop destination.
- [DropSession.Phase.dataTransferCompleted](./phase-swift.enum/datatransfercompleted.md)
  Dragged items have been transferred. You can remove temporary items, perform any cleanup if needed.
- [DropSession.Phase.ended(_:)](./phase-swift.enum/ended%28_%29.md)
  The drop has ended.
- [DropSession.Phase.entering](./phase-swift.enum/entering.md)
  The drop session is entering the drop destination.
- [DropSession.Phase.exiting](./phase-swift.enum/exiting.md)
  The drop session has exited the drop destination.

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Getting drop session details
- [var id: DropSession.ID](./id-swift.property.md)
  The unique identifier of the drop session.
- [DropSession.ID](./id-swift.struct.md)
  The identifier of a drag session.
- [var localSession: DropSession.LocalSession?](./localsession-swift.property.md)
  Provides additional information about a session if it originated within the app.
- [DropSession.LocalSession](./localsession-swift.struct.md)
  Describes the session originated within the app.
- [var phase: DropSession.Phase](./phase-swift.property.md)
  The phase of the current drop session.
- [var suggestedOperations: DropOperation.Set](./suggestedoperations.md)
  Operations suggested by the drag source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/phase-swift.enum)*