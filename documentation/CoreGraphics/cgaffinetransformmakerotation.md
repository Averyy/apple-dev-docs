# CGAffineTransformMakeRotation(_:)

**Framework**: Core Graphics  
**Kind**: func

Returns an affine transformation matrix constructed from a rotation value you provide.

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
func CGAffineTransformMakeRotation(_ angle: CGFloat) -> CGAffineTransform
```

#### Return Value

A new affine transformation matrix.

#### Discussion

This function creates a `CGAffineTransform` structure, which you can use (and reuse, if you want) to rotate a coordinate system. The matrix takes the following form:

![A 3 by 3 matrix.](https://docs-assets.developer.apple.com/published/208a3d614f01846a4816496780b1a1fb/media-1966725%402x.png)

The actual direction of rotation is dependent on the coordinate system orientation of the target platform, which is different in iOS and macOS. Because the third column is always `(0,0,1)`, the `CGAffineTransform` data structure returned by this function contains values for only the first two columns.

These are the resulting equations used to apply the rotation to a point (x, y):

![Rotation equations.](https://docs-assets.developer.apple.com/published/6aee9efda1c1ac989f5c0fceb3b21a44/media-1966730%402x.png)

If you want only to rotate an object to be drawn, it is not necessary to construct an affine transform to do so. The most direct way to rotate your drawing is by calling the function [`rotate(by:)`](cgcontext/rotate(by:).md).

## Parameters

- `angle`: The angle, in radians, by which this matrix rotates the coordinate system axes. In iOS, a positive value specifies counterclockwise rotation and a negative value specifies clockwise rotation. In macOS, a positive value specifies clockwise rotation and a negative value specifies counterclockwise rotation.

## See Also

- [func CGAffineTransformMake(CGFloat, CGFloat, CGFloat, CGFloat, CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmake(_:_:_:_:_:_:).md)
  Returns an affine transformation matrix constructed from values you provide.
- [func CGAffineTransformMakeScale(CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmakescale(_:_:).md)
  Returns an affine transformation matrix constructed from scaling values you provide.
- [func CGAffineTransformMakeTranslation(CGFloat, CGFloat) -> CGAffineTransform](cgaffinetransformmaketranslation(_:_:).md)
  Returns an affine transformation matrix constructed from translation values you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformmakerotation(_:))*