# capSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions in the height of each hemispherical end of the capsule. Animatable.

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
var capSegmentCount: Int { get set }
```

#### Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curved surface for the capsule’s ends at a cost to rendering performance.

The default segment count is `24`. Setting this property’s value to a number less than `1` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var radialSegmentCount: Int](scncapsule/radialsegmentcount.md)
  The number of subdivisions around the lateral circumference of the capsule. Animatable.
- [var heightSegmentCount: Int](scncapsule/heightsegmentcount.md)
  The number of subdivisions in the sides of the capsule along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/capsegmentcount)*