# CGAffineTransformRotate(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Returns an affine transformation matrix constructed by rotating an existing affine transform.

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
func CGAffineTransformRotate(_ t: CGAffineTransform, _ angle: CGFloat) -> CGAffineTransform
```

```c
extern CGAffineTransform CGAffineTransformRotate(CGAffineTransform t, CGFloat angle);
```

## Return Value

A new affine transformation matrix.

## Discussion

You use this function to create a new affine transformation matrix by adding a rotation value to an existing affine transform. The resulting structure represents a new affine transform, which you can use (and reuse, if you want) to rotate a coordinate system.

The actual direction of rotation is dependent on the coordinate system orientation of the target platform, which is different in iOS and macOS.

## Parameters

- `t`: An existing affine transform.
- `angle`: The angle, in radians, by which to rotate the affine transform. In iOS, a positive value specifies counterclockwise rotation and a negative value specifies clockwise rotation. In macOS, a positive value specifies clockwise rotation and a negative value specifies counterclockwise rotation.

## See Also

### Modifying Affine Transformations
- [func CGAffineTransformTranslate(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformtranslate%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by translating an existing affine transform.
- [func CGAffineTransformScale(CGAffineTransform, CGFloat, CGFloat) -> CGAffineTransform](./cgaffinetransformscale%28_,_,_%29.md)
  Returns an affine transformation matrix constructed by scaling an existing affine transform.
- [func CGAffineTransformInvert(CGAffineTransform) -> CGAffineTransform](./cgaffinetransforminvert%28_%29.md)
  Returns an affine transformation matrix constructed by inverting an existing affine transform.
- [func CGAffineTransformConcat(CGAffineTransform, CGAffineTransform) -> CGAffineTransform](./cgaffinetransformconcat%28_,_%29.md)
  Returns an affine transformation matrix constructed by combining two existing affine transforms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformrotate(_:_:))*