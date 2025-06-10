# bottomRadius

**Framework**: SceneKit  
**Kind**: property

The radius of the cone’s circular base. Animatable.

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
var bottomRadius: CGFloat { get set }
```

#### Discussion

The cone is centered in its local coordinate system. For example, the base of a cone whose bottom radius is `5.0` extends from `-5.0` to `5.0` along the x- and z-axes.

If either the top or bottom radius is zero, the geometry forms a cone that tapers to an apex point at that end. If both top and bottom radii are nonzero, the geometry forms a frustum that tapers (or expands) from a circular base to a circular top. If both top and bottom radii are zero or less, or either if the top or bottom radius is less than zero, the geometry is empty. The default bottom radius is `0.5`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var topRadius: CGFloat](scncone/topradius.md)
  The radius of the cone’s circular top. Animatable.
- [var height: CGFloat](scncone/height.md)
  The extent of the cylinder along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncone/bottomradius)*