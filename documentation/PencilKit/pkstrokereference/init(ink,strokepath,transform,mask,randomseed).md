# init(ink:strokePath:transform:mask:randomSeed:)

**Framework**: PencilKit  
**Kind**: init  
**Role**: Initializer

Creates a stroke with the line properties, path, transform, mask, and random seed that you specify.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- visionOS 1.0+

## Declaration

*iOS, iPadOS, Mac Catalyst, visionOS*

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?, randomSeed: UInt32)
```

*macOS*

```swift
init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: NSBezierPath?, randomSeed: UInt32)
```

*iOS, iPadOS, Mac Catalyst, visionOS*

```objc
- (instancetype) initWithInk:(PKInk *) ink strokePath:(PKStrokePath *) strokePath transform:(CGAffineTransform) transform mask:(UIBezierPath *) mask randomSeed:(uint32_t) randomSeed;
```

*macOS*

```objc
- (instancetype) initWithInk:(PKInk *) ink strokePath:(PKStrokePath *) strokePath transform:(CGAffineTransform) transform mask:(NSBezierPath *) mask randomSeed:(uint32_t) randomSeed;
```

## Parameters

- `ink`: The [`PKInkReference`](../pkinkreference.md) used to render this stroke.
- `strokePath`: The B-spline path that describes this stroke.
- `transform`: The [`CGAffineTransform`](../../CoreFoundation/cgaffinetransform.md) to apply to this stroke. Defaults to [`CGAffineTransformIdentity`](../../CoreGraphics/cgaffinetransformidentity.md).
- `mask`: The pretransform mask used to clip the rendering of the stroke.
- `randomSeed`: The random seed for the stroke.

## See Also

### Creating a stroke object
- [init(ink: PKInk, strokePath: PKStrokePath, transform: CGAffineTransform, mask: UIBezierPath?)](./init%28ink,strokepath,transform,mask%29.md)
  Creates a stroke with the line properties, path, transform, and mask that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/pencilkit/pkstrokereference/init(ink:strokepath:transform:mask:randomseed:))*