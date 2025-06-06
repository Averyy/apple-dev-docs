# UIPencilInteraction.Tap

**Framework**: UIKit  
**Kind**: class

An interaction that represents a double tap on Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+

## Declaration

```swift
@MainActor
class Tap
```

## Topics

### Getting information about a double-tap interaction
- [var timestamp: TimeInterval](uipencilinteraction/tap/timestamp.md)
  The timestamp of the double-tap interaction.
- [var hoverPose: UIPencilHoverPose?](uipencilinteraction/tap/hoverpose.md)
  The hover pose of Apple Pencil during a double-tap interaction.
- [class UIPencilHoverPose](uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UIPencilInteraction](uipencilinteraction.md)
  An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [protocol UIPencilInteractionDelegate](uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [UIPencilInteraction.Squeeze](uipencilinteraction/squeeze.md)
  An interaction that represents a squeeze on Apple Pencil.
- [UIPencilInteraction.Phase](uipencilinteraction/phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [class UIPencilHoverPose](uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/tap)*