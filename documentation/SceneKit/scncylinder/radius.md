# radius

**Framework**: SceneKit  
**Kind**: property

The radius of the cylinder’s circular cross section. Animatable.

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
var radius: CGFloat { get set }
```

#### Discussion

The cylinder is centered in its local coordinate system. For example, a cylinder of radius `5.0` extends from `-5.0` to `5.0` along the x- and z-axes. The default radius is `0.5`. A radius of zero or less creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [class SCNCylinder](scncylinder.md)
  A right circular cylinder geometry.
- [var height: CGFloat](scncylinder/height.md)
  The extent of the cylinder along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncylinder/radius)*