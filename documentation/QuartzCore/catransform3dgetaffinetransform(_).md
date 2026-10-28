# CATransform3DGetAffineTransform(_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

Returns the affine transform represented by `t`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DGetAffineTransform(_ t: CATransform3D) -> CGAffineTransform
```

```c
extern CGAffineTransform CATransform3DGetAffineTransform(CATransform3D t);
```

## Discussion

If `t` can not be exactly represented as an affine transform, the return value is undefined.

## See Also

### Converting to and from Core Graphics Affine Transforms
- [func CATransform3DMakeAffineTransform(CGAffineTransform) -> CATransform3D](./catransform3dmakeaffinetransform%28_%29.md)
  Returns a transform with the same effect as affine transform `m`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dgetaffinetransform(_:))*