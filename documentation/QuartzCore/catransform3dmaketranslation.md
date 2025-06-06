# CATransform3DMakeTranslation(_:_:_:)

**Framework**: Core Animation  
**Kind**: func

Returns a transform that translates by `(tx, ty, tz)`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DMakeTranslation(_ tx: CGFloat, _ ty: CGFloat, _ tz: CGFloat) -> CATransform3D
```

#### Discussion

`t =  [1 0 0 0; 0 1 0 0; 0 0 1 0; tx ty tz 1].`

## See Also

- [func CATransform3DMakeScale(CGFloat, CGFloat, CGFloat) -> CATransform3D](catransform3dmakescale(_:_:_:).md)
  Returns a transform that scales by `(sx, sy, sz)`.
- [func CATransform3DMakeRotation(CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D](catransform3dmakerotation(_:_:_:_:).md)
  Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dmaketranslation(_:_:_:))*