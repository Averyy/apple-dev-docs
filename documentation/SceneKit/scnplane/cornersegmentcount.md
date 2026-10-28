# cornerSegmentCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of line segments used to create each rounded corner of the plane. Animatable.

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
var cornerSegmentCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger cornerSegmentCount;
```

## Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curve for each rounded corner at a cost to rendering performance.

The default corner segment count is `10`. Setting this property’s value to a number less than `1` results in undefined behavior.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Related Documentation
- [var heightSegmentCount: Int](./heightsegmentcount.md)
  The number of subdivisions in the plane’s surface along its vertical axis. Animatable.
- [var widthSegmentCount: Int](./widthsegmentcount.md)
  The number of subdivisions in the plane’s surface along its horizontal axis. Animatable.
### Adding Rounded Corners
- [var cornerRadius: CGFloat](./cornerradius.md)
  The radius of curvature for the plane’s corners. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnplane/cornersegmentcount)*