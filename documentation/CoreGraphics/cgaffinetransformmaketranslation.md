# CGAffineTransformMakeTranslation(_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns an affine transformation matrix constructed from translation values you provide.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGAffineTransformMakeTranslation(_ tx: CGFloat, _ ty: CGFloat) -> CGAffineTransform
```

#### Return Value

A new affine transform matrix.

#### Discussion

This function creates a `CGAffineTransform` structure. which you can use (and reuse, if you want) to move a coordinate system. The matrix takes the following form:

![A 3 by 3 matrix for translation.](https://docs-assets.developer.apple.com/published/d3f20158f45b6884521dea50065da09b/media-1966750%402x.png)

Because the third column is always `(0,0,1)`, the `CGAffineTransform` data structure returned by this function contains values for only the first two columns.

These are the resulting equations used to apply the translation to a point (x,y):

![Translation equations.](https://docs-assets.developer.apple.com/published/7f47312b5509bb3fe710b89c425126f0/media-1966756%402x.png)

If you want only to move the location where an object is drawn, it is not necessary to construct an affine transform to do so. The most direct way to move your drawing is by calling the function [`translateBy(x:y:)`](cgcontext/translateby(x:y:).md).

## Parameters

- `tx`: The value by which to move the x-axis of the coordinate system.
- `ty`: The value by which to move the y-axis of the coordinate system.

## See Also

- [func CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmake(_:_:_:_:_:_:).md)
  Returns an affine transformation matrix constructed from values you provide.
- [func CGAffineTransformMakeRotation(CGFloat) -> CGAffineTransform](cgaffinetransformmakerotation(_:).md)
  Returns an affine transformation matrix constructed from a rotation value you provide.
- [func CGAffineTransformMakeScale(CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmakescale(_:_:).md)
  Returns an affine transformation matrix constructed from scaling values you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformmaketranslation(_:_:))*