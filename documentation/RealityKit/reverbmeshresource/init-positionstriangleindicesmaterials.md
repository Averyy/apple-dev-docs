# init(positions:triangleIndices:materials:)

**Framework**: RealityKit  
**Kind**: init

Creates a reverb mesh resource from a list of positions, triangle indices, and material indices.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32], materials: [UInt32]) throws
```

#### Discussion

Use this initializer when you have precise control over the geometry:

```swift
let mesh = try ReverbMeshResource(
    positions: myPositions,
    triangleIndices: myIndices,
    materials: perFaceMaterialIndices
)
```

## Parameters

- `positions`: The vertex positions of the mesh.
- `triangleIndices`: The triangle indices that reference positions in the `positions` array.
- `materials`: An array of material indices, one per triangle, that map each face to a material in the [`Audio.Material`](audio/material.md) array provided to [`simulated(mesh:materials:)`](reverb/simulated(mesh:materials:).md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource/init(positions:triangleindices:materials:))*