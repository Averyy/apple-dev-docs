# DropSession.Phase

**Framework**: SwiftUI  
**Kind**: enum

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
- [DropSession.Phase.active](dropsession/phase-swift.enum/active.md)
  The drop session is active inside the drop destination.
- [DropSession.Phase.dataTransferCompleted](dropsession/phase-swift.enum/datatransfercompleted.md)
  Dragged items have been transferred. You can remove temporary items, perform any cleanup if needed.
- [DropSession.Phase.ended(_:)](dropsession/phase-swift.enum/ended(_:).md)
  The drop has ended.
- [DropSession.Phase.entering](dropsession/phase-swift.enum/entering.md)
  The drop session is entering the drop destination.
- [DropSession.Phase.exiting](dropsession/phase-swift.enum/exiting.md)
  The drop session has exited the drop destination.

## Relationships

### Conforms To
- [Copyable](../swift/copyable.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Escapable](../swift/escapable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [var id: DropSession.ID](dropsession/id-swift.property.md)
  The unique identifier of the drop session.
- [DropSession.ID](dropsession/id-swift.struct.md)
  The identifier of a drag session.
- [var localSession: DropSession.LocalSession?](dropsession/localsession-swift.property.md)
  Provides additional information about a session if it originated within the app.
- [DropSession.LocalSession](dropsession/localsession-swift.struct.md)
  Describes the session originated within the app.
- [var phase: DropSession.Phase](dropsession/phase-swift.property.md)
  The phase of the current drop session.
- [var suggestedOperations: DropOperation.Set](dropsession/suggestedoperations.md)
  Operations suggested by the drag source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/phase-swift.enum)*