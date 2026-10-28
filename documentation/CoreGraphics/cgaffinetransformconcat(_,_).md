# CGAffineTransformConcat(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns an affine transformation matrix constructed by combining two existing affine transforms.

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
func CGAffineTransformConcat(_ t1: CGAffineTransform, _ t2: CGAffineTransform) -> CGAffineTransform
```

```c
extern CGAffineTransform CGAffineTransformConcat(CGAffineTransform t1, CGAffineTransform t2);
```

## Return Value

A new affine transformation matrix. That is, t’ = t1*t2.

## Discussion

Concatenation combines two affine transformation matrices by multiplying them together. You might perform several concatenations in order to create a single affine transform that contains the cumulative effects of several transformations.

Note that matrix operations are not commutative—the order in which you concatenate matrices is important. That is, the result of multiplying matrix `t1` by matrix `t2` does not necessarily equal the result of multiplying matrix `t2` by matrix `t1`.

## Parameters

- `t1`: The first affine transform.
- `t2`: The second affine transform. This affine transform is concatenated to the first affine transform.

## See Also

### Modifying Affine Transformations
- [func CGAffineTransformTranslate(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformtranslate%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by translating an existing affine transform.
- [func CGAffineTransformScale(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformscale%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [func CGAffineTransformRotate(CGAffineTransform, CGFloat) -> CGAffineTransform](./cgaffinetransformrotate%28_,_%29.md)
  Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [func CGAffineTransformInvert(CGAffineTransform) -> CGAffineTransform](./cgaffinetransforminvert%28_%29.md)
  Returns an affine transformation matrix constructed by inverting an existing affine transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformconcat(_:_:))*