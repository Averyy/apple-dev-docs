# CATransform3DMakeTranslation(_:_:_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

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

```c
extern CATransform3D CATransform3DMakeTranslation(CGFloat tx, CGFloat ty, CGFloat tz);
```

## Discussion

`t =  [1 0 0 0; 0 1 0 0; 0 0 1 0; tx ty tz 1].`

## See Also

### Creating Transforms
- [func CATransform3DMakeScale(CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dmakescale%28_,_,_%29.md)
  Returns a transform that scales by `(sx, sy, sz)`.
- [func CATransform3DMakeRotation(CGFloat, CGFloat, CGFloat, CGFloat) -> CATransform3D](./catransform3dmakerotation%28_,_,_,_%29.md)
  Returns a transform that rotates by `angle` radians about the vector `(x, y, z)`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dmaketranslation(_:_:_:))*