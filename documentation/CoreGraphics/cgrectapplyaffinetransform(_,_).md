# CGRectApplyAffineTransform(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Applies an affine transform to a rectangle.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGRectApplyAffineTransform(_ rect: CGRect, _ t: CGAffineTransform) -> CGRect
```

```c
extern CGRect CGRectApplyAffineTransform(CGRect rect, CGAffineTransform t);
```

## Return Value

The transformed rectangle.

## Discussion

Because affine transforms do not preserve rectangles in general, this function returns the smallest rectangle that contains the transformed corner points of the `rect` parameter. If the affine transform `t` consists solely of scaling and translation operations, then the returned rectangle coincides with the rectangle constructed from the four transformed corners.

## Parameters

- `rect`: The rectangle whose corner points you want to transform.
- `t`: The affine transform to apply to the `rect` parameter.

## See Also

### Applying Affine Transformations
- [func CGPointApplyAffineTransform(CGPoint, CGAffineTransform) -> CGPoint](./cgpointapplyaffinetransform%28_,_%29.md)
  Returns the point resulting from an affine transformation of an existing point.
- [func CGSizeApplyAffineTransform(CGSize, CGAffineTransform) -> CGSize](./cgsizeapplyaffinetransform%28_,_%29.md)
  Returns the height and width resulting from a transformation of an existing height and width.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgrectapplyaffinetransform(_:_:))*