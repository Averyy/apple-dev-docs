# init(ink:path:transform:mask:randomSeed:)

**Framework**: PencilKit  
**Kind**: init

Creates a macOS stroke with the line properties, path, transform, mask, and random seed that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- macOS 13.0+

## Declaration

```swift
init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform = .identity, mask: NSBezierPath? = nil, randomSeed: UInt32)
```

## Parameters

- `ink`: The   the framework uses to render this stroke.
- `path`: The B-spline path that describes this stroke.
- `transform`: The   to apply to this stroke. Defaults to  .
- `mask`: The pretransform mask the framework uses to clip the rendering of the stroke.
- `randomSeed`: The random seed for the stroke.

## See Also

- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](pkstroke-swift.struct/init(ink:path:transform:mask:)-1imp6.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?)](pkstroke-swift.struct/init(ink:path:transform:mask:)-w7ti.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:)-10m5j.md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:)-epus)*