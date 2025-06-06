# renderBounds

**Framework**: PencilKit  
**Kind**: property

The bounds of the rendered stroke, including the width and line properties of the stroke after applying the transform.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var renderBounds: CGRect { get }
```

## See Also

- [var ink: PKInk](pkstrokereference/ink.md)
  The line properties used to render this stroke.
- [var mask: UIBezierPath?](pkstrokereference/mask.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var maskedPathRanges: [__PKFloatRange]](pkstrokereference/maskedpathranges.md)
  The range of points in the stroke path reference that intersect the stroke’s mask.
- [var path: PKStrokePath](pkstrokereference/path.md)
  The B-spline path that describes this stroke.
- [var transform: CGAffineTransform](pkstrokereference/transform.md)
  The affine transform of the stroke after rendering.
- [var randomSeed: UInt32](pkstrokereference/randomseed.md)
  An unsigned 32-bit integer to use as a random seed for drawing strokes that use randomized effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/renderbounds)*