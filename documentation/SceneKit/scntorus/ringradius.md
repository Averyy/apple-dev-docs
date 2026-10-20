# ringRadius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The major radius of the torus, defining a circle in the x- and z-axis dimensions. Animatable.

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
var ringRadius: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat ringRadius;
```

#### Discussion

In the definition of a torus as a surface of revolution, the ring radius is the distance from the center of a circle (defined by the [`pipeRadius`](./piperadius.md) property) to the axis of revolution (the y-axis of the torus’s local coordinate space). Rotating the circle around the axis forms a pipe that follows a ring-shaped path.

The default ring radius is `0.5`. A ring radius of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting a Torus’ Dimensions
- [var pipeRadius: CGFloat](./piperadius.md)
  The minor radius of the torus, defining the pipe that encircles the torus ring. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus/ringradius)*