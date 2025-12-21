# DragSession.Phase

**Framework**: SwiftUI  
**Kind**: enum

The phase of the current drag session

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
- [DragSession.Phase.active](dragsession/phase-swift.enum/active.md)
  The drag has moved to a new location.
- [DragSession.Phase.dataTransferCompleted](dragsession/phase-swift.enum/datatransfercompleted.md)
  Dragged items have been transferred. You can remove temporary items, perform any cleanup if needed.
- [DragSession.Phase.ended(_:)](dragsession/phase-swift.enum/ended(_:).md)
  The drag has ended.
- [DragSession.Phase.ending(_:)](dragsession/phase-swift.enum/ending(_:).md)
  The drag is about to finish.
- [DragSession.Phase.initial](dragsession/phase-swift.enum/initial.md)
  The drag session is about to begin

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragsession/phase-swift.enum)*