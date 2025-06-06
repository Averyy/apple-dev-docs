# radialSegmentCount

**Framework**: SceneKit  
**Kind**: property

The number of subdivisions around the circumference of the cylinder. Animatable.

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
var radialSegmentCount: Int { get set }
```

#### Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curve for the cylinder’s circular cross section at a cost to rendering performance.

The default segment count is `48`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var heightSegmentCount: Int](scncylinder/heightsegmentcount.md)
  The number of subdivisions in the sides of the cylinder along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncylinder/radialsegmentcount)*