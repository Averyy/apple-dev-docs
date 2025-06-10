# init(ink:strokePath:transform:mask:)

**Framework**: PencilKit  
**Kind**: init

Creates a stroke with the line properties, path, transform, and mask that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?)
```

## Parameters

- `ink`: The   the class uses to render this stroke.
- `strokePath`: The B-spline path that describes this stroke.
- `transform`: The   to apply to this stroke. Defaults to  .
- `mask`: The pretransform mask the class uses to clip the rendering of the stroke.

## See Also

- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](pkstrokereference/init(ink:strokepath:transform:mask:randomseed:).md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/init(ink:strokepath:transform:mask:))*