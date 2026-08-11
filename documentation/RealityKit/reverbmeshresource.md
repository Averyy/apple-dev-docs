# ReverbMeshResource

**Framework**: RealityKit  
**Kind**: class

A high-level representation of a collection of vertices and edges that define a shape used for simulating reverb.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
final class ReverbMeshResource
```

#### Overview

Use a `ReverbMeshResource` to describe the acoustic geometry of your scene. Create one from geometric primitives, custom vertex data, or an existing [`MeshResource`](meshresource.md):

```swift
// From a geometric primitive:
let room = ReverbMeshResource.shoebox(size: [4, 3, 5])

// From custom vertex data:
let mesh = try ReverbMeshResource(
    positions: myPositions,
    triangleIndices: myIndices,
    materials: perFaceMaterialIndices
)

// From an existing mesh resource:
let mesh = try ReverbMeshResource(from: myVisualMesh)
```

Pair a reverb mesh with [`Audio.Material`](audio/material.md) values and set a [`ReverbComponent`](reverbcomponent.md) on an entity to activate simulated reverb:

```swift
let reverb: Reverb = .simulated(mesh: room, materials: [.concrete, .carpet])
entity.components.set(ReverbComponent(reverb: reverb))
```

> **Note**: Reverb meshes perform best with fewer than 1000 polygons.

## Topics

### Creating standard room shapes
- [static func shoebox(size: SIMD3<Float>) -> Self](reverbmeshresource/shoebox(size:).md)
  Creates a box mesh with the vertices positioned such that the bottom surface is at y=0, with faces oriented inward.
- [static func box(size: SIMD3<Float>) -> Self](reverbmeshresource/box(size:).md)
  Creates a box mesh with vertices positioned such that the origin is at the center, with faces oriented outward.
- [static func plane(width: Float, depth: Float) -> Self](reverbmeshresource/plane(width:depth:).md)
  Creates a new rectangle reverb mesh with the specified dimensions in the entity’s xz-plane.
### Creating a custom mesh
- [convenience init(positions: [SIMD3<Float>], triangleIndices: [UInt32], materials: [UInt32]) throws](reverbmeshresource/init(positions:triangleindices:materials:).md)
  Creates a reverb mesh resource from a list of positions, triangle indices, and material indices.
### Initializers
- [convenience(from:)](reverbmeshresource/init(from:).md)
  Creates a reverb mesh resource from a mesh resource.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Resource](resource.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [class AudioPlaybackGroupController](audioplaybackgroupcontroller.md)
  A controller that manages synchronized playback for a group of audio resources.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/reverbmeshresource)*