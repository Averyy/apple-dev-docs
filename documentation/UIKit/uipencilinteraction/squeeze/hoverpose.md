# hoverPose

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The hover pose of Apple Pencil during a squeeze interaction.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 26.2+

## Declaration

```swift
var hoverPose: UIPencilHoverPose? { get }
```

```objc
@property (nonatomic, strong, readonly, nullable) UIPencilHoverPose * hoverPose;
```

#### Discussion

The value of this property is `nil` if Apple Pencil isn’t close enough to the screen to detect a hover, or if the device doesn’t support hover.

## See Also

### Getting information about a squeeze interaction
- [var timestamp: TimeInterval](./timestamp.md)
  The timestamp of the squeeze interaction.
- [var phase: UIPencilInteraction.Phase](./phase.md)
  The phase of a squeeze interaction on Apple Pencil.
- [UIPencilInteraction.Phase](../phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [class UIPencilHoverPose](../../uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/squeeze/hoverpose)*