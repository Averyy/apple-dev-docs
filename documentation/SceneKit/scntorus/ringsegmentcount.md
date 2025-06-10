# ringSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions around the torus ring. Animatable.

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
var ringSegmentCount: Int { get set }
```

#### Discussion

This segment count corresponds to the circle formed by the torus’ major radius or [`ringRadius`](scntorus/ringradius.md) property. A larger number of segments adds more vertex data to the geometry, creating a more smoothly curved surface at a cost to rendering performance.

The default segment count is `48`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var pipeSegmentCount: Int](scntorus/pipesegmentcount.md)
  The number of subdivisions around the torus pipe. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus/ringsegmentcount)*