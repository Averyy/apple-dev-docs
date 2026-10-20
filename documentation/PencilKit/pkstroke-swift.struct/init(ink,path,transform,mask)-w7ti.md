# init(ink:path:transform:mask:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a stroke with the line properties, path, transform, and mask that you specify.

**Availability**:
- macOS 11.0+

## Declaration

```swift
init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform = .identity, mask: NSBezierPath? = nil)
```

## Parameters

- `ink`: The [`PKInk`](../pkink-swift.struct.md) the framework uses to render this stroke.
- `path`: The B-spline path that describes this stroke.
- `transform`: The [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) to apply to this stroke.
- `mask`: The pretransform mask the framework uses to clip the rendering of the stroke.

## See Also

### Creating a stroke object
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](./init%28ink,path,transform,mask%29-1imp6.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](./init%28ink,path,transform,mask,randomseed%29-10m5j.md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.
- [init(ink: PKInk, path: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32)](./init%28ink,path,transform,mask,randomseed%29-epus.md)
  Creates a macOS stroke with the line properties, path, transform, mask, and random seed that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstroke-swift.struct/init(ink:path:transform:mask:)-w7ti)*