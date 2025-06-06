# cornerRadius

**Framework**: SceneKit  
**Kind**: property

The radius of curvature for the plane’s corners. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.9+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var cornerRadius: CGFloat { get set }
```

#### Discussion

The minimum (and default) corner radius is `0.0`, specifying square corners. Set this property to a nonzero value to add rounded corners to the plane. Setting a corner radius of less than zero creates an empty geometry.

The maximum corner radius is half the plane’s smaller dimension. For example, if a plane’s [`width`](scnplane/width.md) and [`height`](scnplane/height.md) properties are both `10.0`, setting a corner radius of `5.0` gives the plane a circular shape, and increasing the corner radius beyond `5.0` has no effect. If a plane has width `10.0` and height `5.0`, the maximum corner radius is `2.5`, creating a rectangular shape with circular endcaps.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var cornerSegmentCount: Int](scnplane/cornersegmentcount.md)
  The number of line segments used to create each rounded corner of the plane. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnplane/cornerradius)*