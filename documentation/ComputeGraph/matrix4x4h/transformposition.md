# matrix4x4h::transformPosition

**Framework**: ComputeGraph  
**Kind**: func

Transforms a half-precision position by a 4x4 matrix, including translation.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
half3 matrix4x4h::transformPosition(half4x4 matrix, half3 position)
```

#### Return Value

The transformed 3D position.

#### Discussion

Multiplies the position by the matrix with a `w` component of `1.0`, so rotation, scale, and translation are all applied. This is appropriate for points in space that should be fully transformed by the matrix.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/c7d71bcfcc5d7f2ac81874279dbb7129/matrix4x4h__transformPosition.svg)

## Parameters

- `matrix`: The 4x4 transformation matrix to apply.
- `position`: The 3D position to transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/matrix4x4h/transformposition)*