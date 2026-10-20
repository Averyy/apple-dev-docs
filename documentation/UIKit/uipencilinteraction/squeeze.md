# UIPencilInteraction.Squeeze

**Framework**: UIKit  
**Kind**: class  
**Role**: Class

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

```objc
@interface UIPencilInteractionSqueeze : NSObject
```

## Topics

### Getting information about a squeeze interaction
- [var timestamp: TimeInterval](./squeeze/timestamp.md)
  The timestamp of the squeeze interaction.
- [var phase: UIPencilInteraction.Phase](./squeeze/phase.md)
  The phase of a squeeze interaction on Apple Pencil.
- [UIPencilInteraction.Phase](./phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [var hoverPose: UIPencilHoverPose?](./squeeze/hoverpose.md)
  The hover pose of Apple Pencil during a squeeze interaction.
- [class UIPencilHoverPose](../uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.

## Relationships

### Inherits From
- [NSObject](../../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../../Swift/cvararg.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [NSObjectProtocol](../../ObjectiveC/nsobjectprotocol.md)
- [Sendable](../../Swift/sendable.md)

## See Also

### Apple Pencil interactions in UIKit
- [class UIPencilInteraction](../uipencilinteraction.md)
  An interaction that tells your app when a person double-taps or squeezes Apple Pencil.
- [protocol UIPencilInteractionDelegate](../uipencilinteractiondelegate.md)
  The interface an object implements to handle double taps or squeezes a person makes on Apple Pencil.
- [UIPencilInteraction.Tap](./tap.md)
  An interaction that represents a double tap on Apple Pencil.
- [UIPencilInteraction.Phase](./phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [class UIPencilHoverPose](../uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/squeeze)*