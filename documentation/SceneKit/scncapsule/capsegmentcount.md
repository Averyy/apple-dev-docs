# capSegmentCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of subdivisions in the height of each hemispherical end of the capsule. Animatable.

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
var capSegmentCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger capSegmentCount;
```

## Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curved surface for the capsule’s ends at a cost to rendering performance.

The default segment count is `24`. Setting this property’s value to a number less than `1` results in undefined behavior.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting Geometric Detail
- [var radialSegmentCount: Int](./radialsegmentcount.md)
  The number of subdivisions around the lateral circumference of the capsule. Animatable.
- [var heightSegmentCount: Int](./heightsegmentcount.md)
  The number of subdivisions in the sides of the capsule along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/capsegmentcount)*