# init(ink:path:transform:mask:)

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
init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform = .identity, mask: UIBezierPath? = nil)
```

## Parameters

- `ink`: The   the framework uses to render this stroke.
- `path`: The B-spline path that describes this stroke.
- `transform`: The   to apply to this stroke.
- `mask`: The pretransform mask the framework uses to clip the rendering of the stroke.

## See Also

- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?)](pkstroke-swift.struct/init(ink:path:transform:mask:)-w7ti.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:)-10m5j.md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32)](pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:)-epus.md)
  Creates a macOS stroke with the line properties, path, transform, mask, and random seed that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/init(ink:path:transform:mask:)-1imp6)*