# transform

**Framework**: PencilKit  
**Kind**: property  
**Role**: Instance Property

The affine transform of the stroke after rendering.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
var transform: CGAffineTransform { get }
```

```objc
@property (nonatomic, readonly) CGAffineTransform transform;
```

## See Also

### Getting the stroke properties
- [var ink: PKInk](./ink.md)
  The line properties used to render this stroke.
- [var mask: UIBezierPath?](./mask.md)
  The pretransform mask used to clip the rendering of the stroke.
- [var maskedPathRanges: [__PKFloatRange]](./maskedpathranges.md)
  The range of points in the stroke path reference that intersect the stroke’s mask.
- [var path: PKStrokePath](./path.md)
  The B-spline path that describes this stroke.
- [var renderBounds: CGRect](./renderbounds.md)
  The bounds of the rendered stroke, including the width and line properties of the stroke after applying the transform.
- [var randomSeed: UInt32](./randomseed.md)
  An unsigned 32-bit integer to use as a random seed for drawing strokes that use randomized effects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/transform)*