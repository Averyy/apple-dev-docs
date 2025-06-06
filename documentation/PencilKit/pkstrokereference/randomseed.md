# randomSeed

**Framework**: PencilKit  
**Kind**: property

An unsigned 32-bit integer to use as a random seed for drawing strokes that use randomized effects.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var randomSeed: UInt32 { get }
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
- [var renderBounds: CGRect](pkstrokereference/renderbounds.md)
  The bounds of the rendered stroke, including the width and line properties of the stroke after applying the transform.
- [var transform: CGAffineTransform](pkstrokereference/transform.md)
  The affine transform of the stroke after rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/randomseed)*