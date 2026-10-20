# capRadius

**Framework**: SceneKit  
**Kind**: property  
**Role**: Instance Property

The radius both of the capsule’s circular center cross section and of its hemispherical ends. Animatable.

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
var capRadius: CGFloat { get set }
```

```objc
@property (nonatomic) CGFloat capRadius;
```

#### Discussion

The capsule is centered in its local coordinate system. For example, the cylindrical body of a capsule of radius `5.0` extends from `-5.0` to `5.0` along the x- and z-axes.

If the cap radius is zero or less, or greater than half the capsule’s height, the geometry is empty. The default cap radius is `0.5`.

You can animate changes to this property’s value. See [Animating SceneKit Content](../animating-scenekit-content.md).

## See Also

### Adjusting a Capsule’s Dimensions
- [var height: CGFloat](./height.md)
  The extent of the capsule along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/capradius)*