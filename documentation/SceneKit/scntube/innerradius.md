# innerRadius

**Framework**: SceneKit  
**Kind**: property

The radius of the circular hole through the tube. Animatable.

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
var innerRadius: CGFloat { get set }
```

#### Discussion

The tube is centered in its local coordinate system. For example, if a tube has an inner radius of `1.0`, the cylindrical hole through its center extends from `-0.5` to `0.5` along the x- and z-axes. The default inner radius is `0.25`.

An inner radius of zero or less, or equal to or greater than the outer radius, creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var outerRadius: CGFloat](scntube/outerradius.md)
  The radius of the tube’s outer circular cross section. Animatable.
- [var height: CGFloat](scntube/height.md)
  The extent of the tube along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntube/innerradius)*