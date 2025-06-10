# chamferRadius

**Framework**: SceneKit  
**Kind**: property

The width or depth of each chamfered edge. Animatable.

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
var chamferRadius: CGFloat { get set }
```

#### Discussion

A value of `0.0` (the default) or less specifies no chamfer—the extruded sides of each character end at right angles to its front and back.

The maximum chamfer radius is half the value of the [`extrusionDepth`](scntext/extrusiondepth.md) property. At this radius, the front chamfer ends where the back chamfer begins. However, SceneKit may automatically reduce the chamfer radius for character shapes with thin strokes.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var flatness: CGFloat](scntext/flatness.md)
  A number that determines the accuracy or smoothness of the text geometry.
- [var extrusionDepth: CGFloat](scntext/extrusiondepth.md)
  The extent of the extruded text in the z-axis direction. Animatable.
- [var chamferProfile: UIBezierPath?](scntext/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/chamferradius)*