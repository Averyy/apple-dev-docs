# extrusionDepth

**Framework**: SceneKit  
**Kind**: property

The extent of the extruded text in the z-axis direction. Animatable.

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
var extrusionDepth: CGFloat { get set }
```

#### Discussion

The geometry is centered along the z-axis of its local coordinate space. For example, if its extrusion depth is is `1.0`, the geometry extends from `-0.5` to `0.5` along the z-axis.

An extrusion depth of `0.0` (the default) creates a flat, one-sided shape.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var flatness: CGFloat](scntext/flatness.md)
  A number that determines the accuracy or smoothness of the text geometry.
- [var chamferRadius: CGFloat](scntext/chamferradius.md)
  The width or depth of each chamfered edge. Animatable.
- [var chamferProfile: UIBezierPath?](scntext/chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/extrusiondepth)*