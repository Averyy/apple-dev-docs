# CGAffineTransformMakeScale(_:_:)

**Framework**: Core Graphics  
**Kind**: func

Returns an affine transformation matrix constructed from scaling values you provide.

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
func CGAffineTransformMakeScale(_ sx: CGFloat, _ sy: CGFloat) -> CGAffineTransform
```

#### Return Value

A new affine transformation matrix.

#### Discussion

This function creates a `CGAffineTransform` structure, which you can use (and reuse, if you want) to scale a coordinate system. The matrix takes the following form:

![A 3 by 3 matrix used to scale.](/images/com.apple.coregraphics/media-1966736@2x.png)

Because the third column is always `(0,0,1)`, the `CGAffineTransform` data structure returned by this function contains values for only the first two columns.

These are the resulting equations used to scale the coordinates of a point (x,y):

![Scaling equations.](/images/com.apple.coregraphics/media-1966741@2x.png)

If you want only to scale an object to be drawn, it is not necessary to construct an affine transform to do so. The most direct way to scale your drawing is by calling the function [`scaleBy(x:y:)`](cgcontext/scaleby(x:y:).md).

## Parameters

- `sx`: The factor by which to scale the x-axis of the coordinate system.
- `sy`: The factor by which to scale the y-axis of the coordinate system.

## See Also

- [func CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmake(_:_:_:_:_:_:).md)
  Returns an affine transformation matrix constructed from values you provide.
- [func CGAffineTransformMakeRotation(CGFloat) -> CGAffineTransform](cgaffinetransformmakerotation(_:).md)
  Returns an affine transformation matrix constructed from a rotation value you provide.
- [func CGAffineTransformMakeTranslation(CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmaketranslation(_:_:).md)
  Returns an affine transformation matrix constructed from translation values you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformmakescale(_:_:))*