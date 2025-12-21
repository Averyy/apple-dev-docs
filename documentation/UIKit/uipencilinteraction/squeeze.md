# UIPencilInteraction.Squeeze

**Framework**: UIKit  
**Kind**: class

An interaction that represents a squeeze on Apple Pencil.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 26.2+

## Declaration

```swift
@MainActor
class Squeeze
```

## Topics

### Getting information about a squeeze interaction
- [var timestamp: TimeInterval](uipencilinteraction/squeeze/timestamp.md)
  The timestamp of the squeeze interaction.
- [var phase: UIPencilInteraction.Phase](uipencilinteraction/squeeze/phase.md)
  The phase of a squeeze interaction on Apple Pencil.
- [UIPencilInteraction.Phase](uipencilinteraction/phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [var hoverPose: UIPencilHoverPose?](uipencilinteraction/squeeze/hoverpose.md)
  The hover pose of Apple Pencil during a squeeze interaction.
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
- [UIPencilInteraction.Tap](uipencilinteraction/tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Phase](uipencilinteraction/phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [class UIPencilHoverPose](uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/squeeze)*