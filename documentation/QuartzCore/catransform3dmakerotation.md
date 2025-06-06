# CATransform3DMakeRotation(_:_:_:_:)

**Framework**: Core Animation  
**Kind**: func

Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DMakeRotation(_ angle: CGFloat, _ x: CGFloat, _ y: CGFloat, _ z: CGFloat) -> CATransform3D
```

#### Discussion

If the vector has length zero, this function returns the identity transform.

## See Also

- [func CATransform3DMakeTranslation(CGFloat, CGFloat, CGFloat) -> CATransform3D](catransform3dmaketranslation(_:_:_:).md)
  Returns a transform that translates by `(tx, ty, tz)`.
- [func CATransform3DMakeScale(CGFloat, CGFloat, CGFloat) -> CATransform3D](catransform3dmakescale(_:_:_:).md)
  Returns a transform that scales by `(sx, sy, sz)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dmakerotation(_:_:_:_:))*