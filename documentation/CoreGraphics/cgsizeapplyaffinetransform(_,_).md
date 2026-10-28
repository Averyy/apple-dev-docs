# CGSizeApplyAffineTransform(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the height and width resulting from a transformation of an existing height and width.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGSizeApplyAffineTransform(_ size: CGSize, _ t: CGAffineTransform) -> CGSize
```

```c
extern CGSize CGSizeApplyAffineTransform(CGSize size, CGAffineTransform t);
```

## Return Value

A new size resulting from applying the specified affine transform to the existing size.

## Parameters

- `size`: A size that specifies the height and width to transform.
- `t`: The affine transform to apply.

## See Also

### Applying Affine Transformations
- [func CGPointApplyAffineTransform(CGPoint, CGAffineTransform) -> CGPoint](./cgpointapplyaffinetransform%28_,_%29.md)
  Returns the point resulting from an affine transformation of an existing point.
- [func CGRectApplyAffineTransform(CGRect, CGAffineTransform) -> CGRect](./cgrectapplyaffinetransform%28_,_%29.md)
  Applies an affine transform to a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgsizeapplyaffinetransform(_:_:))*