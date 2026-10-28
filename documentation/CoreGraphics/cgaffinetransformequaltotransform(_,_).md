# CGAffineTransformEqualToTransform(_:_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Checks whether two affine transforms are equal.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.4+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func CGAffineTransformEqualToTransform(_ t1: CGAffineTransform, _ t2: CGAffineTransform) -> Bool
```

```c
extern bool CGAffineTransformEqualToTransform(CGAffineTransform t1, CGAffineTransform t2);
```

## Return Value

Returns `true` if `t1` and `t2` are equal, `false` otherwise.

## Parameters

- `t1`: An affine transform.
- `t2`: An affine transform.

## See Also

### Evaluating Affine Transforms
- [func CGAffineTransformIsIdentity(CGAffineTransform) -> Bool](./cgaffinetransformisidentity%28_%29.md)
  Checks whether an affine transform is the identity transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformequaltotransform(_:_:))*