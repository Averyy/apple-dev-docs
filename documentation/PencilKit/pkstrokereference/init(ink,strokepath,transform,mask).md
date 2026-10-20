# init(ink:strokePath:transform:mask:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a stroke with the line properties, path, transform, and mask that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)
```

*macOS*

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (instancetype) initWithInk:(PKInk *) ink strokePath:(PKStrokePath *) strokePath transform:(CGAffineTransform) transform mask:(UIBezierPath *) mask;
```

*macOS*

```objc
- (instancetype) initWithInk:(PKInk *) ink strokePath:(PKStrokePath *) strokePath transform:(CGAffineTransform) transform mask:(NSBezierPath *) mask;
```

## Parameters

- `ink`: The [`PKInkReference`](../pkinkreference.md) the class uses to render this stroke.
- `strokePath`: The B-spline path that describes this stroke.
- `transform`: The [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) to apply to this stroke. Defaults to [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md).
- `mask`: The pretransform mask the class uses to clip the rendering of the stroke.

## See Also

### Creating a stroke object
- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)](./init%28ink,strokepath,transform,mask,randomseed%29.md)
  Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/init(ink:strokepath:transform:mask:))*