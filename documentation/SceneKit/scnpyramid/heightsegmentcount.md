# heightSegmentCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of subdivisions in each face of the pyramid along its y-axis. Animatable.

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
var heightSegmentCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger heightSegmentCount;
```

#### Discussion

A larger number of segments adds more vertex data to the geometry. Though each face of the pyramid is a flat plane, extra vertices can be useful for lighting or custom shader programs. Adding vertices increases rendering cost, so you should use the minimal segment count that produces your desired visual effect.

The default segment count is `1`. Setting this property’s value to a number less than `1` results in undefined behavior.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting Geometric Detail
- [var widthSegmentCount: Int](./widthsegmentcount.md)
  The number of subdivisions in each face of the pyramid along its x-axis. Animatable.
- [var lengthSegmentCount: Int](./lengthsegmentcount.md)
  The number of subdivisions in each face of the pyramid along its z-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnpyramid/heightsegmentcount)*