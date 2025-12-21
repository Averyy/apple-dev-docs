# SimpleMaterial

**Framework**: RealityKit  
**Kind**: struct

A basic material that responds to lights in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS ?+

## Declaration

```swift
struct SimpleMaterial
```

## Mentions

- [Adding procedural assets to a scene](adding-procedural-assets-to-a-scene.md)

#### Overview

`SimpleMaterial` responds to both real and virtual lighting to enhance realism.

Add a `SimpleMaterial` to a model by setting it as one of the [`materials`](modelcomponent/materials.md) in a [`ModelComponent`](modelcomponent.md).

```swift
let simpleMaterial = SimpleMaterial(
    color: .red, isMetallic: false
)
let model = ModelComponent(
    mesh: .generateBox(size: 1),
    materials: [simpleMaterial]
)
redBoxEntity.components.set(model)
```

For example, a red `SimpleMaterial` that is not metallic, and one that is metallic:

| Not metallic | Metallic |
| --- | --- |
| ![A screenshot of a red cube in a living room scene. The cube is rounded on the edges and appears to be made of a reflective plastic material.](https://docs-assets.developer.apple.com/published/1c42115ca829aa1fde7b9c344fac4ebc/simplematerial-not-metallic.jpg) | ![A screenshot of a red cube in a living room scene. The cube is rounded on the edges and appears to be made of a reflective metal material.](https://docs-assets.developer.apple.com/published/d58949e85bccef55e9218565e2e3f237/simplematerial-metallic.jpg) |

## Topics

### Creating a simple material
- [init()](simplematerial/init.md)
  Creates a simple material.
### Characterizing a material
- [var color: SimpleMaterial.BaseColor](simplematerial/color.md)
  The material’s color.
- [var baseColor: MaterialColorParameter](simplematerial/basecolor-swift.property.md)
  The base color of the material.
- [SimpleMaterial.BaseColor](simplematerial/basecolor-swift.typealias.md)
  The type used to represent base color.
- [SimpleMaterial.Texture](simplematerial/texture.md)
  The type used to represent textures.
- [var metallic: MaterialScalarParameter](simplematerial/metallic.md)
  A value that you set to control whether the material has a metallic look.
- [var roughness: MaterialScalarParameter](simplematerial/roughness.md)
  The roughness of the material.
### Initializers
- [init(color:roughness:isMetallic:)](simplematerial/init(color:roughness:ismetallic:).md)
  Creates a simple material with specific characteristics in macOS.
### Instance Properties
- [var faceCulling: SimpleMaterial.FaceCulling](simplematerial/faceculling-swift.property.md)
  A process in which the system specifies polygons to remove before rendering a mesh using this material.
- [var readsDepth: Bool](simplematerial/readsdepth.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
- [var tintColor: NSColor](simplematerial/tintcolor-6v03h.md)
  A tint color applied to the base color in macOS.
- [var tintColor: UIColor](simplematerial/tintcolor-74a0x.md)
  A tint color applied to the base color in macOS.
- [var triangleFillMode: SimpleMaterial.TriangleFillMode](simplematerial/trianglefillmode-swift.property.md)
  The object that controls how RealityKit draws triangles.
- [var writesDepth: Bool](simplematerial/writesdepth.md)
  A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.
### Type Aliases
- [SimpleMaterial.FaceCulling](simplematerial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [SimpleMaterial.TriangleFillMode](simplematerial/trianglefillmode-swift.typealias.md)

## Relationships

### Conforms To
- [Material](material.md)

## See Also

- [SimpleMaterial.BaseColor](simplematerial/basecolor-swift.typealias.md)
  The type used to represent base color.
- [SimpleMaterial.Texture](simplematerial/texture.md)
  The type used to represent textures.
- [SimpleMaterial.FaceCulling](simplematerial/faceculling-swift.typealias.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [SimpleMaterial.TriangleFillMode](simplematerial/trianglefillmode-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/simplematerial)*