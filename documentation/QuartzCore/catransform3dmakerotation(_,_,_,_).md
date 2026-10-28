# CATransform3DMakeRotation(_:_:_:_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

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

```c
extern CATransform3D CATransform3DMakeRotation(CGFloat angle, CGFloat x, CGFloat y, CGFloat z);
```

## Discussion

If the vector has length zero, this function returns the identity transform.

## See Also

### Creating Transforms
- [func CATransform3DMakeTranslation(CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dmaketranslation%28_,_,_%29.md)
  Returns a transform that translates by `(tx, ty, tz)`.
- [func CATransform3DMakeScale(CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dmakescale%28_,_,_%29.md)
  Returns a transform that scales by `(sx, sy, sz)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dmakerotation(_:_:_:_:))*