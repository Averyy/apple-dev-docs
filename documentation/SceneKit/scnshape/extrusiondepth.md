# extrusionDepth

**Framework**: SceneKit  
**Kind**: property

The thickness of the extruded shape along the z-axis. Animatable.

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
var extrusionDepth: CGFloat { get set }
```

#### Discussion

The extruded shape is centered at the zero point of its z-axis. For example, an extrusion depth of `1.0` creates a shape that extends from `-0.5` to `0.5` along the z-axis. An extrusion depth of zero creates a flat, one-sided shape.

You can animate changes to this property’s value. See [`Animating SceneKit Content`](animating-scenekit-content.md).

## See Also

- [var path: UIBezierPath?](scnshape/path.md)
  The two-dimensional path forming the basis of the shape.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnshape/extrusiondepth)*