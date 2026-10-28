# CATransform3DEqualToTransform(_:_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

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

```c
extern bool CATransform3DEqualToTransform(CATransform3D a, CATransform3D b);
```

## Return Value

[`true`](../Swift/true.md) if `a` and `b` are exactly equal, otherwise [`false`](../Swift/false.md).

## See Also

### Determining Transform Properties
- [func CATransform3DIsAffine(CATransform3D) -> Bool](./catransform3disaffine%28_%29.md)
  Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.
- [func CATransform3DIsIdentity(CATransform3D) -> Bool](./catransform3disidentity%28_%29.md)
  Returns a Boolean value that indicates whether the transform is the identity transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3dequaltotransform(_:_:))*