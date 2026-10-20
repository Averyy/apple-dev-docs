# chamferSegmentCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of line segments used to create each rounded edge of the box. Animatable.

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
var chamferSegmentCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger chamferSegmentCount;
```

#### Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curve for each rounded edge and corner at a cost to rendering performance.

The default corner segment count is `10`. Setting this property’s value to a number less than `1` results in undefined behavior.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var heightSegmentCount: Int](./heightsegmentcount.md)
  The number of subdivisions in each face of the box along its y-axis. Animatable.
- [var widthSegmentCount: Int](./widthsegmentcount.md)
  The number of subdivisions in each face of the box along its x-axis. Animatable.
- [var lengthSegmentCount: Int](./lengthsegmentcount.md)
  The number of subdivisions in each face of the box along its z-axis. Animatable.
### Adding Rounded Edges and Corners
- [var chamferRadius: CGFloat](./chamferradius.md)
  The radius of curvature for the edges and corners of the box. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnbox/chamfersegmentcount)*