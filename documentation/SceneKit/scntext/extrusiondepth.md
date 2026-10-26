# extrusionDepth

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The extent of the extruded text in the z-axis direction. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
var extrusionDepth: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat extrusionDepth;
```

#### Discussion

The geometry is centered along the z-axis of its local coordinate space. For example, if its extrusion depth is is `1.0`, the geometry extends from `-0.5` to `0.5` along the z-axis.

An extrusion depth of `0.0` (the default) creates a flat, one-sided shape.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing the Text’s 3D Representation
- [var flatness: CGFloat](./flatness.md)
  A number that determines the accuracy or smoothness of the text geometry.
- [var chamferRadius: CGFloat](./chamferradius.md)
  The width or depth of each chamfered edge. Animatable.
- [var chamferProfile: UIBezierPath?](./chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.
- [chamferSegmentCount](./chamfersegmentcount.md)
  The number of divisions SceneKit uses to create each chamfered edge of the text geometry. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/extrusiondepth)*