# heightSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions in the sides of the capsule along its y-axis. Animatable.

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
var heightSegmentCount: Int { get set }
```

#### Discussion

A larger number of segments adds more vertex data to the geometry. Although the sides of the capsule’s cylindrical body are flat in the y-axis direction, extra vertices can be useful for lighting or custom shader programs. Adding vertices increases rendering cost, so use the minimal segment count that produces your desired visual effect.

The default segment count is `1`. Setting this property’s value to a number less than `1` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var radialSegmentCount: Int](scncapsule/radialsegmentcount.md)
  The number of subdivisions around the lateral circumference of the capsule. Animatable.
- [var capSegmentCount: Int](scncapsule/capsegmentcount.md)
  The number of subdivisions in the height of each hemispherical end of the capsule. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/heightsegmentcount)*