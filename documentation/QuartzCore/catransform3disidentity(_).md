# CATransform3DIsIdentity(_:)

**Framework**: Core Animation  
**Kind**: func  
**Role**: Function

Returns a Boolean value that indicates whether the transform is the identity transform.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+

## Declaration

```swift
func CATransform3DIsIdentity(_ t: CATransform3D) -> Bool
```

```c
extern bool CATransform3DIsIdentity(CATransform3D t);
```

## Return Value

[`true`](../Swift/true.md) if `t` is the identity transform, otherwise [`false`](../Swift/false.md).

## See Also

### Determining Transform Properties
- [func CATransform3DIsAffine(CATransform3D) -> Bool](./catransform3disaffine%28_%29.md)
  Returns a Boolean value that indicates whether a transform can be exactly represented by an affine transform.
- [func CATransform3DEqualToTransform(CATransform3D, CATransform3D) -> Bool](./catransform3dequaltotransform%28_,_%29.md)
  Returns a Boolean value that indicates whether the two transforms are exactly equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/quartzcore/catransform3disidentity(_:))*