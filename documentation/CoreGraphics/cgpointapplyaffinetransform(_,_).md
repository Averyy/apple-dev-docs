# CGPointApplyAffineTransform(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns the point resulting from an affine transformation of an existing point.

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
func CGPointApplyAffineTransform(_ point: CGPoint, _ t: CGAffineTransform) -> CGPoint
```

```c
extern CGPoint CGPointApplyAffineTransform(CGPoint point, CGAffineTransform t);
```

## Return Value

A new point resulting from applying the specified affine transform to the existing point.

## Parameters

- `point`: A point that specifies the x- and y-coordinates to transform.
- `t`: The affine transform to apply.

## See Also

### Applying Affine Transformations
- [func CGSizeApplyAffineTransform(CGSize, CGAffineTransform) -> CGSize](./cgsizeapplyaffinetransform%28_,_%29.md)
  Returns the height and width resulting from a transformation of an existing height and width.
- [func CGRectApplyAffineTransform(CGRect, CGAffineTransform) -> CGRect](./cgrectapplyaffinetransform%28_,_%29.md)
  Applies an affine transform to a rectangle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgpointapplyaffinetransform(_:_:))*