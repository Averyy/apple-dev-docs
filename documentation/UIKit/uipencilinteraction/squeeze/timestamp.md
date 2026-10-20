# timestamp

**Framework**: UIKit  
**Kind**: property  
**Role**: Instance Property

The timestamp of the squeeze interaction.

**Availability**:
- iOS 17.5+
- iPadOS 17.5+
- Mac Catalyst 17.5+
- visionOS 26.2+

## Declaration

```swift
var timestamp: TimeInterval { get }
```

```objc
@property (nonatomic, assign, readonly) NSTimeInterval timestamp;
```

## See Also

### Getting information about a squeeze interaction
- [var phase: UIPencilInteraction.Phase](./phase.md)
  The phase of a squeeze interaction on Apple Pencil.
- [UIPencilInteraction.Phase](../phase.md)
  Constants that describe the phases of an interaction on Apple Pencil.
- [var hoverPose: UIPencilHoverPose?](./hoverpose.md)
  The hover pose of Apple Pencil during a squeeze interaction.
- [class UIPencilHoverPose](../../uipencilhoverpose.md)
  An object that describes the hover pose of Apple Pencil during an interaction like double tap or squeeze.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uipencilinteraction/squeeze/timestamp)*