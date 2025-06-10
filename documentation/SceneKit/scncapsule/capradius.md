# capRadius

**Framework**: SceneKit  
**Kind**: property

The radius both of the capsule’s circular center cross section and of its hemispherical ends. Animatable.

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
var capRadius: CGFloat { get set }
```

#### Discussion

The capsule is centered in its local coordinate system. For example, the cylindrical body of a capsule of radius `5.0` extends from `-5.0` to `5.0` along the x- and z-axes.

If the cap radius is zero or less, or greater than half the capsule’s height, the geometry is empty. The default cap radius is `0.5`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var height: CGFloat](scncapsule/height.md)
  The extent of the capsule along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/capradius)*