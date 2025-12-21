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
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dropsession/phase-swift.enum)*