# pipeSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions around the torus pipe. Animatable.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var pipeSegmentCount: Int { get set }
```

#### Discussion

This segment count corresponds to the circle formed by the torus’ minor radius or [`pipeRadius`](scntorus/piperadius.md) property. A larger number of segments adds more vertex data to the geometry, creating a more smoothly curved surface at a cost to rendering performance.

The default segment count is `24`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var ringSegmentCount: Int](scntorus/ringsegmentcount.md)
  The number of subdivisions around the torus ring. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus/pipesegmentcount)*