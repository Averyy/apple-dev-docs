# matrix4x4f::transformDirection

**Framework**: Compute Graph  
**Kind**: func

Transforms a direction vector by a 4x4 matrix, ignoring translation.

**Availability**:
- macOS ?+
- Reality Composer Pro ?+

## Declaration

```swift
float3 matrix4x4f::transformDirection(float4x4 matrix, float3 vector)
```

#### Return Value

The transformed 3D direction vector.

#### Discussion

Multiplies the vector by the matrix with a `w` component of `0.0`, so only rotation and scale are applied. This is appropriate for normals, tangents, and other direction vectors that should not be affected by the matrix’s translational component.

> **Note**: ![Graph](/images/com.apple.computegraph/matrix4x4f__transformDirection.svg)

## Parameters

- `matrix`: The 4x4 transformation matrix to apply.
- `vector`: The 3D direction vector to transform.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/matrix4x4f/transformdirection)*