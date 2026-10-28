# topRadius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The radius of the cone’s circular top. Animatable.

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
var topRadius: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat topRadius;
```

## Discussion

The cone is centered in its local coordinate system. For example, the upper surface of a cone whose top radius is `5.0` extends from `-5.0` to `5.0` along the x- and z-axes.

If either the top or bottom radius is zero, the geometry forms a cone that tapers to an apex point at that end. If both top and bottom radii are nonzero, the geometry forms a frustum that tapers (or expands) from a circular base to a circular top. If both top and bottom radii are zero or less, or either if the top or bottom radius is less than zero, the geometry is empty. The default top radius is `0.0`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting a Cone’s Dimensions
- [var bottomRadius: CGFloat](./bottomradius.md)
  The radius of the cone’s circular base. Animatable.
- [var height: CGFloat](./height.md)
  The extent of the cylinder along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncone/topradius)*