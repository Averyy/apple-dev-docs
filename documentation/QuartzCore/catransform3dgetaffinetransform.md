# CATransform3DGetAffineTransform(_:)

**Framework**: Core Animation  
**Kind**: func

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

#### Discussion

If `t` can not be exactly represented as an affine transform, the return value is undefined.

## See Also

- [func CATransform3DMakeAffineTransform(CGAffineTransform) -> CATransform3D](catransform3dmakeaffinetransform(_:).md)
  Returns a transform with the same effect as affine transform `m`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dgetaffinetransform(_:))*