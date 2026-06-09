# matrix4x4h::transformDirection

**Framework**: ComputeGraph  
**Kind**: func

Transforms a half-precision direction vector by a 4x4 matrix, ignoring translation.

**Availability**:
- macOS 27.0+ (Beta)
- Reality Composer Pro 27.0+ (Beta)

## Declaration

```swift
half3 matrix4x4h::transformDirection(half4x4 matrix, half3 vector)
```

#### Return Value

The transformed 3D direction vector.

#### Discussion

Multiplies the vector by the matrix with a `w` component of `0.0`, so only rotation and scale are applied. This is appropriate for normals, tangents, and other direction vectors that should not be affected by the matrix’s translational component.

> **Note**: ![Graph](https://docs-assets.developer.apple.com/published/a0961fc84ad0bbe519078eecc812da50/matrix4x4h__transformDirection.svg)

## Parameters

- `matrix`: The 4x4 transformation matrix to apply.
- `vector`: The 3D direction vector to transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/matrix4x4h/transformdirection)*