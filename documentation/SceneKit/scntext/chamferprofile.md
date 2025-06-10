# chamferProfile

**Framework**: SceneKit  
**Kind**: property

A path that determines the cross-sectional contour of each chamfered edge.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
@NSCopying
var chamferProfile: UIBezierPath? { get set }
```

#### Discussion

The value of this property must be a two-dimensional path starting at the point `{1, 0}` and ending at the point `{0, 1}`, determining the contour of the shape along its extruded sides. If the value of this property is `nil` and the value of the [`chamferRadius`](scntext/chamferradius.md) property is greater than zero, SceneKit uses a chamfer profile in the shape of a quarter circle. [`Figure 1`](scntext/1523334-chamferprofile#1965884.md) illustrates various chamfer profiles applied to the shape of a tilde (~) character.

![None](https://docs-assets.developer.apple.com/published/5a92cf08a192d2bc019ad9266b486308/media-1965884%402x.png)

## See Also

- [var flatness: CGFloat](scntext/flatness.md)
  A number that determines the accuracy or smoothness of the text geometry.
- [var extrusionDepth: CGFloat](scntext/extrusiondepth.md)
  The extent of the extruded text in the z-axis direction. Animatable.
- [var chamferRadius: CGFloat](scntext/chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/chamferprofile)*