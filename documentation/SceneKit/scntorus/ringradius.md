# ringRadius

**Framework**: SceneKit  
**Kind**: property

The major radius of the torus, defining a circle in the x- and z-axis dimensions. Animatable.

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
var ringRadius: CGFloat { get set }
```

#### Discussion

In the definition of a torus as a surface of revolution, the ring radius is the distance from the center of a circle (defined by the [`pipeRadius`](scntorus/piperadius.md) property) to the axis of revolution (the y-axis of the torus’s local coordinate space). Rotating the circle around the axis forms a pipe that follows a ring-shaped path.

The default ring radius is `0.5`. A ring radius of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var pipeRadius: CGFloat](scntorus/piperadius.md)
  The minor radius of the torus, defining the pipe that encircles the torus ring. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus/ringradius)*