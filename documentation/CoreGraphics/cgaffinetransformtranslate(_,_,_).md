# CGAffineTransformTranslate(_:_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns an affine transformation matrix constructed by translating an existing affine transform.

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
func CGAffineTransformTranslate(_ t: CGAffineTransform, _ tx: CGFloat, _ ty: CGFloat) -> CGAffineTransform
```

```c
extern CGAffineTransform CGAffineTransformTranslate(CGAffineTransform t, CGFloat tx, CGFloat ty);
```

#### Return Value

A new affine transformation matrix.

#### Discussion

You use this function to create a new affine transform by adding translation values to an existing affine transform. The resulting structure represents a new affine transform, which you can use (and reuse, if you want) to move a coordinate system.

## Parameters

- `t`: An existing affine transform.
- `tx`: The value by which to move x values with the affine transform.
- `ty`: The value by which to move y values with the affine transform.

## See Also

### Modifying Affine Transformations
- [func CGAffineTransformScale(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformscale%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [func CGAffineTransformRotate(CGAffineTransform, CGFloat) -> CGAffineTransform](./cgaffinetransformrotate%28_,_%29.md)
  Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [func CGAffineTransformInvert(CGAffineTransform) -> CGAffineTransform](./cgaffinetransforminvert%28_%29.md)
  Returns an affine transformation matrix constructed by inverting an existing affine transform.
- [func CGAffineTransformConcat(CGAffineTransform, CGAffineTransform) -> CGAffineTransform](./cgaffinetransformconcat%28_,_%29.md)
  Returns an affine transformation matrix constructed by combining two existing affine transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformtranslate(_:_:_:))*