# outerRadius

**Framework**: SceneKit  
**Kind**: property

The radius of the tube’s outer circular cross section. Animatable.

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
var outerRadius: CGFloat { get set }
```

#### Discussion

The tube is centered in its local coordinate system. For example, a tube whose outer radius is  `5.0` extends from `-5.0` to `5.0` along the x- and z-axes. The default outer radius is `0.5`.

An outer radius of zero or less, or equal to or smaller than the inner radius, creates an empty geometry.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var innerRadius: CGFloat](scntube/innerradius.md)
  The radius of the circular hole through the tube. Animatable.
- [var height: CGFloat](scntube/height.md)
  The extent of the tube along its y-axis. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scntube/outerradius)*