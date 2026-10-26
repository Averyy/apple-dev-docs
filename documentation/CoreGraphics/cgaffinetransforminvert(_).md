# CGAffineTransformInvert(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns an affine transformation matrix constructed by inverting an existing affine transform.

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
func CGAffineTransformInvert(_ t: CGAffineTransform) -> CGAffineTransform
```

```c
extern CGAffineTransform CGAffineTransformInvert(CGAffineTransform t);
```

#### Return Value

A new affine transformation matrix. If the affine transform passed in parameter `t` cannot be inverted, the affine transform is returned unchanged.

#### Discussion

Inversion is generally used to provide reverse transformation of points within transformed objects. Given the coordinates (x,y), which have been transformed by a given matrix to new coordinates (x’,y’), transforming the coordinates (x’,y’) by the inverse matrix produces the original coordinates (x,y).

## Parameters

- `t`: An existing affine transform.

## See Also

### Modifying Affine Transformations
- [func CGAffineTransformTranslate(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformtranslate%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by translating an existing affine transform.
- [func CGAffineTransformScale(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformscale%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [func CGAffineTransformRotate(CGAffineTransform, CGFloat) -> CGAffineTransform](./cgaffinetransformrotate%28_,_%29.md)
  Returns an affine transformation matrix constructed by rotating an existing affine transform.
- [func CGAffineTransformConcat(CGAffineTransform, CGAffineTransform) -> CGAffineTransform](./cgaffinetransformconcat%28_,_%29.md)
  Returns an affine transformation matrix constructed by combining two existing affine transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransforminvert(_:))*