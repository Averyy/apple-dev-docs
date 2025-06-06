# hoverPose

**Framework**: UIKit  
**Kind**: property

The hover pose of Apple Pencil during a double-tap interaction.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+

## Declaration

```swift
@MainActor
var hoverPose: UIPencilHoverPose? { get }
```

#### Discussion

The value of this property is `nil` if Apple Pencil isn’t close enough to the screen to detect a hover, or if the device doesn’t support hover.

## See Also

- [var timestamp: TimeInterval](uipencilinteraction/tap/timestamp.md)
  The timestamp of the double-tap interaction.
- [class UIPencilHoverPose](uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/tap/hoverpose)*