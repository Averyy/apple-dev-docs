# init(ink:strokePath:transform:mask:randomSeed:)

**Framework**: PencilKit  
**Kind**: init

Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32)
```

## Parameters

- `ink`: The [`PKInkReference`](pkinkreference.md) used to render this stroke.
- `strokePath`: The B-spline path that describes this stroke.
- `transform`: The [`CGAffineTransform`](https://developer.apple.com/documentation/corefoundation/cgaffinetransform) to apply to this stroke. Defaults to [`CGAffineTransformIdentity`](https://developer.apple.com/documentation/coregraphics/cgaffinetransformidentity).
- `mask`: The pretransform mask used to clip the rendering of the stroke.
- `randomSeed`: The random seed for the stroke.

## See Also

- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](pkstrokereference/init(ink:strokepath:transform:mask:).md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/init(ink:strokepath:transform:mask:randomseed:))*