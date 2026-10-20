# CATransform3DScale(_:_:_:_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

Scales `t` by `(sx, sy, sz)` and returns the result: `t = scale(sx, sy, sz) * t`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DScale(_ t: CATransform3D, _ sx: CGFloat, _ sy: CGFloat, _ sz: CGFloat) -> CATransform3D
```

```c
extern CATransform3D CATransform3DScale(CATransform3D t, CGFloat sx, CGFloat sy, CGFloat sz);
```

## See Also

### Chaining Transforms
- [func CATransform3DConcat(CATransform3D, CATransform3D) -> CATransform3D](./catransform3dconcat%28_,_%29.md)
  Concatenates `b` to `a` and returns the result: `t = a * b`.
- [func CATransform3DTranslate(CATransform3D, CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dtranslate%28_,_,_,_%29.md)
  Translates `t` by `(tx, ty, tz)` and returns the result: `t` `= translate(tx, ty, tz) * t`.
- [func CATransform3DRotate(CATransform3D, CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3drotate%28_,_,_,_,_%29.md)
  Rotates `t` by `angle` radians about the vector `(x, y, z)` and returns the result.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dscale(_:_:_:_:))*