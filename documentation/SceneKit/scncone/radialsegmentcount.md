# radialSegmentCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of subdivisions around the circumference of the cone. Animatable.

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
var radialSegmentCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger radialSegmentCount;
```

#### Discussion

A larger number of segments adds more vertex data to the geometry, creating a smoother curve for the cone’s circular cross section at a cost to rendering performance.

The default segment count is `48`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting Geometric Detail
- [var heightSegmentCount: Int](./heightsegmentcount.md)
  The number of subdivisions in the sides of the cone along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncone/radialsegmentcount)*