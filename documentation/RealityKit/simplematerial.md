# SimpleMaterial

**Framework**: RealityKit  
**Kind**: struct

A basic material that responds to lights in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
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
- [init(color: SimpleMaterial.Color, roughness: MaterialScalarParameter, isMetallic: Bool)](simplematerial/init(color:roughness:ismetallic:)-mwh5.md)
  Creates a simple material with specific characteristics in macOS.
- [init(color: SimpleMaterial.Color, roughness: MaterialScalarParameter, isMetallic: Bool)](simplematerial/init(color:roughness:ismetallic:)-1qshm.md)
  Creates a simple material with specific characteristics in macOS.
### Characterizing a material
- [var color: SimpleMaterial.BaseColor](simplematerial/color.md)
  The material’s color.
- [var baseColor: MaterialColorParameter](simplematerial/basecolor-swift.property.md)
  The base color of the material.
- [var tintColor: UIColor](simplematerial/tintcolor-18qur.md)
  A tint color applied to the base color in macOS.
- [var tintColor: NSColor](simplematerial/tintcolor-6aik0.md)
  A tint color applied to the base color in macOS.
- [var metallic: MaterialScalarParameter](simplematerial/metallic.md)
  A value that you set to control whether the material has a metallic look.
- [var roughness: MaterialScalarParameter](simplematerial/roughness.md)
  The roughness of the material.
### Initializers
- [init(color:roughness:isMetallic:)](simplematerial/init(color:roughness:ismetallic:).md)
  Creates a simple material with specific characteristics in macOS.
### Instance Properties
- [var faceCulling: SimpleMaterial.FaceCulling](simplematerial/faceculling-6lmly.md)
  A process in which the system specifies polygons to remove before rendering a mesh using this material.
- [var faceCulling: SimpleMaterial.FaceCulling](simplematerial/faceculling-9izub.md)
  A process in which the system specifies polygons to remove before rendering a mesh using this material.
- [var readsDepth: Bool](simplematerial/readsdepth-26hjz.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
- [var readsDepth: Bool](simplematerial/readsdepth-l9cl.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
- [var triangleFillMode: SimpleMaterial.TriangleFillMode](simplematerial/trianglefillmode-swift.property.md)
  The object that controls how RealityKit draws triangles.
- [var writesDepth: Bool](simplematerial/writesdepth-4nh0k.md)
  A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.
- [var writesDepth: Bool](simplematerial/writesdepth-9o9eg.md)
  A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.
### Type Aliases
- [SimpleMaterial.BaseColor](simplematerial/basecolor-10zk1.md)
  The type used to represent base color.
- [SimpleMaterial.BaseColor](simplematerial/basecolor-8p27k.md)
  The type used to represent base color.
- [SimpleMaterial.FaceCulling](simplematerial/faceculling-203bc.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [SimpleMaterial.FaceCulling](simplematerial/faceculling-5lval.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [SimpleMaterial.Texture](simplematerial/texture-1uofr.md)
  The type used to represent textures.
- [SimpleMaterial.Texture](simplematerial/texture-36h1v.md)
  The type used to represent textures.
- [SimpleMaterial.TriangleFillMode](simplematerial/trianglefillmode-swift.typealias.md)

## Relationships

### Conforms To
- [Material](material.md)

## See Also

- [SimpleMaterial.TriangleFillMode](simplematerial/trianglefillmode-swift.typealias.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/simplematerial)*