# chamferSegmentCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of divisions SceneKit uses to create each chamfered edge of the text geometry. Animatable.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

> **Deprecated**: The [`flatness`](./flatness.md) property controls the level of detail of both the text and its chamfer profile.

## Declaration

```objc
@property (nonatomic) NSInteger chamferSegmentCount;
```

#### Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curve for chamfered edges at a cost to rendering performance.

The default segment count is `10`. Setting this property’s value to a number less than `1` results in undefined behavior.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Managing the Text’s 3D Representation
- [var flatness: CGFloat](./flatness.md)
  A number that determines the accuracy or smoothness of the text geometry.
- [var extrusionDepth: CGFloat](./extrusiondepth.md)
  The extent of the extruded text in the z-axis direction. Animatable.
- [var chamferRadius: CGFloat](./chamferradius.md)
  The width or depth of each chamfered edge. Animatable.
- [var chamferProfile: UIBezierPath?](./chamferprofile.md)
  A path that determines the cross-sectional contour of each chamfered edge.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntext/chamfersegmentcount)*