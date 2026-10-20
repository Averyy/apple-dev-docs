# randomSeed

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
var randomSeed: UInt32 { get set }
```

## See Also

### Getting the stroke properties
- [var ink: PKInk](./ink.md)
  The Ink, which is a combination of a tool used to render this stroke.
- [var mask: UIBezierPath?](./mask-8g6sx.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var mask: NSBezierPath?](./mask-16kkz.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var maskedPathRanges: [ClosedRange<CGFloat>]](./maskedpathranges.md)
  The range of points in the stroke path reference that intersect the stroke’s mask.
- [var path: PKStrokePath](./path.md)
  The B-spline path that describes this stroke.
- [var renderBounds: CGRect](./renderbounds.md)
  The bounds of the rendered stroke, including the width and line properties of the stroke after applying the transform.
- [var transform: CGAffineTransform](./transform.md)
  The affine transform of the stroke after rendering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/randomseed)*