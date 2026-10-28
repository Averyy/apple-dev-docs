# CGAffineTransformScale(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns an affine transformation matrix constructed by scaling an existing affine transform.

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
func CGAffineTransformScale(_ t: CGAffineTransform, _ sx: CGFloat, _ sy: CGFloat) -> CGAffineTransform
```

```c
extern CGAffineTransform CGAffineTransformScale(CGAffineTransform t, CGFloat sx, CGFloat sy);
```

## Return Value

A new affine transformation matrix.

## Discussion

You use this function to create a new affine transformation matrix by adding scaling values to an existing affine transform. The resulting structure represents a new affine transform, which you can use (and reuse, if you want) to scale a coordinate system.

## Parameters

- `t`: An existing affine transform.
- `sx`: The value by which to scale x values of the affine transform.
- `sy`: The value by which to scale y values of the affine transform.

## See Also

### Modifying Affine Transformations
- [func CGAffineTransformTranslate(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformtranslate%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by translating an existing affine transform.
- [func CGAffineTransformRotate(CGAffineTransform, CGFloat) -> CGAffineTransform](./cgaffinetransformrotate%28_,_%29.md)
  Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [func CGAffineTransformInvert(CGAffineTransform) -> CGAffineTransform](./cgaffinetransforminvert%28_%29.md)
  Returns an affine transformation matrix constructed by inverting an existing affine transform.
- [func CGAffineTransformConcat(CGAffineTransform, CGAffineTransform) -> CGAffineTransform](./cgaffinetransformconcat%28_,_%29.md)
  Returns an affine transformation matrix constructed by combining two existing affine transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformscale(_:_:_:))*