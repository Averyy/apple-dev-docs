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
var chamferProfile: NSBezierPath? { get set }
```

#### Discussion

The value of this property must be a two-dimensional path starting at the point `{1, 0}` and ending at the point `{0, 1}`, determining the contour of the shape along its extruded sides, as illustrated in the figure below. If the value of this property is `nil` and the value of the [`chamferRadius`](scnshape/chamferradius.md) property is greater than zero, SceneKit uses a chamfer profile in the shape of a quarter circle.

![None](https://docs-assets.developer.apple.com/published/af94b4693c8c6fbeb2f8e492e79c50fc/media-2929770%402x.png)

## See Also

- [var chamferMode: SCNChamferMode](scnshape/chamfermode.md)
  A constant specifying which ends of the extruded shape’s profile are chamfered.
- [enum SCNChamferMode](scnchamfermode.md)
  Options for which edges of an extruded shape are chamfered, used by the [`chamferMode`](scnshape/chamfermode.md) property.
- [var chamferRadius: CGFloat](scnshape/chamferradius.md)
  The width or depth of each chamfered edge. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/chamferprofile)*