# CGAffineTransformIsIdentity(_:)

**Framework**: Core Graphics  
**Kind**: func  
**Role**: Function

Checks whether an affine transform is the identity transform.

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
func CGAffineTransformIsIdentity(_ t: CGAffineTransform) -> Bool
```

```c
extern bool CGAffineTransformIsIdentity(CGAffineTransform t);
```

#### Return Value

Returns `true` if `t` is the identity transform, `false` otherwise.

## Parameters

- `t`: The affine transform to check.

## See Also

### Evaluating Affine Transforms
- [func CGAffineTransformEqualToTransform(CGAffineTransform, CGAffineTransform) -> Bool](./cgaffinetransformequaltotransform%28_,_%29.md)
  Checks whether two affine transforms are equal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgaffinetransformisidentity(_:))*