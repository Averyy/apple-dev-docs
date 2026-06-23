# init(positions:coefficients:tetrahedronIndices:)

**Framework**: RealityKit  
**Kind**: init

Creates a diffuse probe resource from arrays of probe data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
nonisolated
convenience init(positions: [SIMD3<Float>], coefficients: [InlineArray<3, SIMD4<Float>>], tetrahedronIndices: [SIMD4<UInt16>]) throws
```

#### Discussion

> **Note**: An error if the data is invalid — for example, if `positions.count` and `coefficients.count` differ, if fewer than 4 probes are provided, or if any tetrahedral index is out of bounds.

## Parameters

- `positions`: The 3D positions of each probe, in local space relative to the probe group entity. Must contain at least 4 positions to form a valid tetrahedral mesh.
- `coefficients`: Spherical harmonic coefficients for each probe. Each entry contains exactly 3 `SIMD4<Float>` values — one per RGB channel, ordered as `(L0, L1.x, L1.y, L1.z)`. Must have the same count as `positions`.
- `tetrahedronIndices`: Indices defining the tetrahedral mesh connectivity. Each `SIMD4<UInt16>` references 4 probe positions by index into `positions`. Must contain at least 1 tetrahedron, and all indices must be less than `positions.count`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/diffuseproberesource/init(positions:coefficients:tetrahedronindices:))*