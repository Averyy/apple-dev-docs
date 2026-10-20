# init(ink:path:transform:mask:randomSeed:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- visionOS 1.0+

## Declaration

```swift
init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform = .identity, mask: UIBezierPath? = nil, randomSeed: UInt32)
```

## Parameters

- `ink`: The [`PKInkReference`](../pkinkreference.md) the framework uses to render this stroke.
- `path`: The B-spline path that describes this stroke.
- `transform`: The [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) to apply to this stroke. Defaults to [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md).
- `mask`: The pretransform mask the framework uses to clip the rendering of the stroke.
- `randomSeed`: The random seed for the stroke.

## See Also

### Creating a stroke object
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](./init%28ink,path,transform,mask%29-1imp6.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?)](./init%28ink,path,transform,mask%29-w7ti.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32)](./init%28ink,path,transform,mask,randomseed%29-epus.md)
  Creates a macOS stroke with the line properties, path, transform, mask, and random seed that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/init(ink:path:transform:mask:randomseed:)-10m5j)*