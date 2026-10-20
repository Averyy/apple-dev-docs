# CATransform3DMakeAffineTransform(_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

Returns a transform with the same effect as affine transform `m`.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DMakeAffineTransform(_ m: CGAffineTransform) -> CATransform3D
```

```c
extern CATransform3D CATransform3DMakeAffineTransform(CGAffineTransform m);
```

## See Also

### Converting to and from Core Graphics Affine Transforms
- [func CATransform3DGetAffineTransform(CATransform3D) -> CGAffineTransform](./catransform3dgetaffinetransform%28_%29.md)
  Returns the affine transform represented by `t`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dmakeaffinetransform(_:))*