# pipeSegmentCount

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The number of subdivisions around the torus pipe. Animatable.

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
var pipeSegmentCount: Int { get set }
```

```objc
@property (nonatomic) NSInteger pipeSegmentCount;
```

#### Discussion

This segment count corresponds to the circle formed by the torus’ minor radius or [`pipeRadius`](./piperadius.md) property. A larger number of segments adds more vertex data to the geometry, creating a more smoothly curved surface at a cost to rendering performance.

The default segment count is `24`. Setting this property’s value to a number less than `3` results in undefined behavior.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Configuring Torus Properties
- [var ringSegmentCount: Int](./ringsegmentcount.md)
  The number of subdivisions around the torus ring. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus/pipesegmentcount)*