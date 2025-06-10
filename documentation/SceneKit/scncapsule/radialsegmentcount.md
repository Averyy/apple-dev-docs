# radialSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions around the lateral circumference of the capsule. Animatable.

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

A larger number of segments adds more vertex data to the geometry, creating a smoother curve for the capsule’s circular horizontal cross sections at a cost to rendering performance.

The default segment count is `48`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var capSegmentCount: Int](scncapsule/capsegmentcount.md)
  The number of subdivisions in the height of each hemispherical end of the capsule. Animatable.
- [var heightSegmentCount: Int](scncapsule/heightsegmentcount.md)
  The number of subdivisions in the sides of the capsule along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/radialsegmentcount)*