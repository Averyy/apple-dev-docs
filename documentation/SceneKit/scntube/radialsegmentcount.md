# radialSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions around the circumference of the tube. Animatable.

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
var radialSegmentCount: Int { get set }
```

#### Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curve for the tube’s circular inner and outer surfaces at a cost to rendering performance.

The default segment count is `48`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var heightSegmentCount: Int](scntube/heightsegmentcount.md)
  The number of subdivisions in the inner and outer surfaces of the tube along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntube/radialsegmentcount)*