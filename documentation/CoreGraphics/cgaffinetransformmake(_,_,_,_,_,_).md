# CGAffineTransformMake(_:_:_:_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns an affine transformation matrix constructed from values you provide.

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
func CGAffineTransformMake(_ a: CGFloat, _ b: CGFloat, _ c: CGFloat, _ d: CGFloat, _ tx: CGFloat, _ ty: CGFloat) -> CGAffineTransform
```

```c
extern CGAffineTransform CGAffineTransformMake(CGFloat a, CGFloat b, CGFloat c, CGFloat d, CGFloat tx, CGFloat ty);
```

#### Return Value

A new affine transform matrix constructed from the values you specify.

#### Discussion

This function creates a `CGAffineTransform` structure that represents a new affine transformation matrix, which you can use (and reuse, if you want) to transform a coordinate system. The matrix takes the following form:

![A 3 by 3 matrix.](https://developer.apple.com/tutorials/images/com.apple.coregraphics/media-1966718@2x.png)

Because the third column is always `(0,0,1)`, the `CGAffineTransform` data structure returned by this function contains values for only the first two columns.

If you want only to transform an object to be drawn, it is not necessary to construct an affine transform to do so. The most direct way to transform your drawing is by calling the appropriate `CGContext` function to adjust the current transformation matrix. For a list of functions, see [`CGContext`](./cgcontext.md).

## Parameters

- `a`: The value at position [1,1] in the matrix.
- `b`: The value at position [1,2] in the matrix.
- `c`: The value at position [2,1] in the matrix.
- `d`: The value at position [2,2] in the matrix.
- `tx`: The value at position [3,1] in the matrix.
- `ty`: The value at position [3,2] in the matrix.

## See Also

### Creating an Affine Transformation Matrix
- [func CGAffineTransformMakeRotation(CGFloat) -> CGAffineTransform](./cgaffinetransformmakerotation%28_%29.md)
  Returns an affine transformation matrix constructed from a rotation value you provide.
- [func CGAffineTransformMakeScale(CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformmakescale%28_,_%29.md)
  Returns an affine transformation matrix constructed from scaling values you provide.
- [func CGAffineTransformMakeTranslation(CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformmaketranslation%28_,_%29.md)
  Returns an affine transformation matrix constructed from translation values you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformmake(_:_:_:_:_:_:))*