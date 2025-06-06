# CATransform3DMakeScale(_:_:_:)

**Framework**: Core Animation  
**Kind**: func

Returns a transform that scales by `(sx, sy, sz)`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DMakeScale(_ sx: CGFloat, _ sy: CGFloat, _ sz: CGFloat) -> CATransform3D
```

#### Discussion

`t = [sx 0 0 0; 0 sy 0 0; 0 0 sz 0; 0 0 0 1].`

## See Also

- [func CATransform3DMakeTranslation(CGFloat, CGFloat, CGFloat) -> CATransform3D](catransform3dmaketranslation(_:_:_:).md)
  Returns a transform that translates by `(tx, ty, tz)`.
- [func CATransform3DMakeRotation(CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D](catransform3dmakerotation(_:_:_:_:).md)
  Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dmakescale(_:_:_:))*