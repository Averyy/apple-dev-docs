# CATransform3DEqualToTransform(_:_:)

**Framework**: Core Animation  
**Kind**: func

Returns a Boolean value that indicates whether the two transforms are exactly equal.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DEqualToTransform(_ a: CATransform3D, _ b: CATransform3D) -> Bool
```

#### Return Value

[`true`](https://developer.apple.com/documentation/swift/true) if `a` and `b` are exactly equal, otherwise [`false`](https://developer.apple.com/documentation/swift/false).

## See Also

- [func CATransform3DIsAffine(CATransform3D) -> Bool](catransform3disaffine(_:).md)
  Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.
- [func CATransform3DIsIdentity(CATransform3D) -> Bool](catransform3disidentity(_:).md)
  Returns a Boolean value that indicates whether the transform is the identity transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dequaltotransform(_:_:))*