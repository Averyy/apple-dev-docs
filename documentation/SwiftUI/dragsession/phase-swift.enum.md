# DragSession.Phase

**Framework**: SwiftUI  
**Kind**: enum  
**Role**: Enumeration

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
- [DragSession.Phase.active](./phase-swift.enum/active.md)
  The drag has moved to a new location.
- [DragSession.Phase.dataTransferCompleted](./phase-swift.enum/datatransfercompleted.md)
  Dragged items have been transferred. You can remove temporary items, perform any cleanup if needed.
- [DragSession.Phase.ended(_:)](./phase-swift.enum/ended%28_%29.md)
  The drag has ended.
- [DragSession.Phase.ending(_:)](./phase-swift.enum/ending%28_%29.md)
  The drag is about to finish.
- [DragSession.Phase.initial](./phase-swift.enum/initial.md)
  The drag session is about to begin

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swiftui/dragsession/phase-swift.enum)*