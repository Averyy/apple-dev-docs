# OcclusionMaterial

**Framework**: RealityKit  
**Kind**: struct

An invisible material that hides objects rendered behind it.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
struct OcclusionMaterial
```

#### Overview

Add an `OcclusionMaterial` to a model by setting it as one of the [`materials`](modelcomponent/materials.md) in a [`ModelComponent`](modelcomponent.md).

```swift
let model = ModelComponent(
    mesh: .generateBox(size: 1),
    materials: [OcclusionMaterial()]
)
smallBoxEntity.components.set(model)
```

For example, on the left is a case of two cubes, the larger red cube is slightly further from the camera and has a simple material. The slightly smaller and closer cube has no material in the left image and an occlusion material on the right image.

| No material | Occlusion material |
| --- | --- |
| ![A screenshot of two cubes in a living room scene. One cube is red and is slightly further from the camera, the other cube has a magenta striped material, is slightly closer to the camera, and is smaller than the red cube.](https://docs-assets.developer.apple.com/published/4c31cbb7ff4c44e34d587750a711c63d/occlusionmaterial-not-applied.jpg) | ![A screenshot of a partial red shape in a living room scene. The shape is of a cube with a cut-out in the shape of another cube slightly towards the upper right corner of the cube.](https://docs-assets.developer.apple.com/published/4829d1d102fa2b00dbce41407e1ea834/occlusionmaterial-applied.jpg) |

## Topics

### Creating an occlusion material
- [init(receivesDynamicLighting: Bool)](occlusionmaterial/init(receivesdynamiclighting:).md)
  Creates an occlusion material.
- [init()](occlusionmaterial/init.md)
### Receiving dynamic lighting
- [let receivesDynamicLighting: Bool](occlusionmaterial/receivesdynamiclighting.md)
  A Boolean that indicates whether the occlusion material receives dynamic lighting.
### Setting depth testing properties
- [var readsDepth: Bool](occlusionmaterial/readsdepth.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
### Instance Properties
- [var faceCulling: OcclusionMaterial.FaceCulling](occlusionmaterial/faceculling-swift.property.md)
  A process in which the system specifies polygons to remove before rendering a mesh using this material.
### Type Aliases
- [OcclusionMaterial.FaceCulling](occlusionmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
### Default Implementations
- [Material Implementations](occlusionmaterial/material-implementations.md)

## Relationships

### Conforms To
- [Material](material.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [OcclusionMaterial.FaceCulling](occlusionmaterial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/occlusionmaterial)*