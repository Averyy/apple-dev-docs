# pipeRadius

**Framework**: SceneKit  
**Kind**: property

The minor radius of the torus, defining the pipe that encircles the torus ring. Animatable.

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
var pipeRadius: CGFloat { get set }
```

#### Discussion

In the definition of a torus as a surface of revolution, the pipe radius defines a circle that is rotated around an axis (the Y axis of the torus’ local coordinate space). Rotating the circle around this axis makes it follow a circular path (whose radius is defined by the [`ringRadius`](scntorus/ringradius.md) property) and creates the surface of the torus.

The default pipe radius is `0.25`. A pipe radius of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var ringRadius: CGFloat](scntorus/ringradius.md)
  The major radius of the torus, defining a circle in the x- and z-axis dimensions. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntorus/piperadius)*