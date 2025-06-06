# height

**Framework**: SceneKit  
**Kind**: property

The extent of the capsule along its y-axis. Animatable.

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
var height: CGFloat { get set }
```

#### Discussion

The capsule is centered in its local coordinate system. For example, if a capsule has a height of `10.0`, it extends from `-5.0` to `5.0` along the y-axis. This property measures the total height of the capsule, including its hemispherical ends.

If the height is zero or less, or less than twice the cap radius, the geometry is empty. The default height is `2.0`.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var capRadius: CGFloat](scncapsule/capradius.md)
  The radius both of the capsule’s circular center cross section and of its hemispherical ends. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scncapsule/height)*