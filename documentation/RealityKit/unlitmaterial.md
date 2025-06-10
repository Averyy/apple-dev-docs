# UnlitMaterial

**Framework**: RealityKit  
**Kind**: struct

A material that doesn’t respond to lights in the scene.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
struct UnlitMaterial
```

## Mentions

- [Modifying RealityKit rendering using custom materials](modifying-realitykit-rendering-using-custom-materials.md)

#### Overview

`UnlitMaterial` materials do not respond to virtual or real lighting.

Add an `UnlitMaterial` to a model by setting it as one of the [`materials`](modelcomponent/materials.md) in a [`ModelComponent`](modelcomponent.md).

```swift
let unlitMaterial = UnlitMaterial(color: .red)
let model = ModelComponent(
    mesh: .generateBox(size: 1),
    materials: [unlitMaterial]
)
redBoxEntity.components.set(model)
```

For example, a [`SimpleMaterial`](simplematerial.md) on the left, and an `UnlitMaterial` on the right:

| [`SimpleMaterial`](simplematerial.md) | `UnlitMaterial` |
| --- | --- |
| ![A screenshot of a red cube in a living room scene. The cube is rounded on the edges, and appears to be made of a reflective plastic material.](https://docs-assets.developer.apple.com/published/1c42115ca829aa1fde7b9c344fac4ebc/simplematerial-not-metallic.jpg) | ![A screenshot of a red cube in a living room scene. The shape is of a cube observed from an angle above and to the right of it, and has no discernible edges as it has no response to lighting.](https://docs-assets.developer.apple.com/published/6114f83b3a9a7c75c60bc409b961edcb/unlitmaterial-red.jpg) |

> **Note**: The blending mode of `UnlitMaterial` materials should be configured explicitly with the [`blending`](unlitmaterial/blending-swift.property.md) property for transparent or translucent surfaces.  The `opaque` mode is used when unset.

## Topics

### Creating an unlit material
- [init()](unlitmaterial/init.md)
  Creates an unlit material.
- [init(color: UIColor)](unlitmaterial/init(color:)-1h0ca.md)
  Creates an unlit material with the given base color.
- [init(color: NSColor)](unlitmaterial/init(color:)-1sk7r.md)
  Creates an unlit material with the given base color.
- [init(applyPostProcessToneMap:)](unlitmaterial/init(applypostprocesstonemap:).md)
- [init(color: NSColor, applyPostProcessToneMap: Bool)](unlitmaterial/init(color:applypostprocesstonemap:)-2cszc.md)
- [init(color: UIColor, applyPostProcessToneMap: Bool)](unlitmaterial/init(color:applypostprocesstonemap:)-9pbcy.md)
- [init(program:)](unlitmaterial/init(program:).md)
- [init(texture:)](unlitmaterial/init(texture:).md)
  Creates a new unlit material with the provided color texture.
### Configuring base color
- [var color: UnlitMaterial.BaseColor](unlitmaterial/color.md)
  The material’s base color.
### Tinting an unlit material
- [var tintColor: NSColor](unlitmaterial/tintcolor-5k3sj.md)
  A tint color applied to the base color.
- [var tintColor: UIColor](unlitmaterial/tintcolor-8gx1u.md)
  A tint color applied to the base color.
### Controlling opacity
- [var opacityThreshold: Float?](unlitmaterial/opacitythreshold.md)
  A threshold below which RealityKit ignores opacity.
- [var blending: UnlitMaterial.Blending](unlitmaterial/blending-swift.property.md)
  The transparency options for the material.
### Classes
- [UnlitMaterial.Program](unlitmaterial/program-7swyg.md)
  An object that represents the backing shader compilation required for unlit materials.
- [UnlitMaterial.Program](unlitmaterial/program-9tv7i.md)
  An object that represents the backing shader compilation required for unlit materials.
### Initializers
- [init(color:)](unlitmaterial/init(color:).md)
  Creates an unlit material with the given base color.
- [init(color:applyPostProcessToneMap:)](unlitmaterial/init(color:applypostprocesstonemap:).md)
### Instance Properties
- [var baseColor: MaterialColorParameter](unlitmaterial/basecolor-2nks9.md)
  The base color of the material.
- [var baseColor: MaterialColorParameter](unlitmaterial/basecolor-9cd6z.md)
  The base color of the material.
- [var faceCulling: UnlitMaterial.FaceCulling](unlitmaterial/faceculling-2vyua.md)
- [var faceCulling: UnlitMaterial.FaceCulling](unlitmaterial/faceculling-6h4qh.md)
- [var program: UnlitMaterial.Program](unlitmaterial/program-68r53.md)
- [var program: UnlitMaterial.Program](unlitmaterial/program-9rxw3.md)
- [var readsDepth: Bool](unlitmaterial/readsdepth-3dp8b.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
- [var readsDepth: Bool](unlitmaterial/readsdepth-86tkk.md)
  A boolean value that determines whether this material performs the depth test by reading RealityKit’s depth buffer.
- [var secondaryTextureCoordinateTransform: UnlitMaterial.TextureCoordinateTransform](unlitmaterial/secondarytexturecoordinatetransform-1a1ap.md)
  A two-dimensional transformation to apply to the entity’s secondary texture coordinates.
- [var secondaryTextureCoordinateTransform: UnlitMaterial.TextureCoordinateTransform](unlitmaterial/secondarytexturecoordinatetransform-45g63.md)
  A two-dimensional transformation to apply to the entity’s secondary texture coordinates.
- [var textureCoordinateTransform: UnlitMaterial.TextureCoordinateTransform](unlitmaterial/texturecoordinatetransform-1pbf5.md)
  A two-dimensional transformation to apply to the entity’s primary texture coordinates.
- [var textureCoordinateTransform: UnlitMaterial.TextureCoordinateTransform](unlitmaterial/texturecoordinatetransform-3583e.md)
  A two-dimensional transformation to apply to the entity’s primary texture coordinates.
- [var tintColor: UIColor](unlitmaterial/tintcolor-k1do.md)
  A tint color applied to the base color.
- [var triangleFillMode: UnlitMaterial.TriangleFillMode](unlitmaterial/trianglefillmode-9i4bf.md)
  The object that controls how RealityKit draws triangles.
- [var triangleFillMode: UnlitMaterial.TriangleFillMode](unlitmaterial/trianglefillmode-i1j1.md)
  The object that controls how RealityKit draws triangles.
- [var writesDepth: Bool](unlitmaterial/writesdepth-1bife.md)
  A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.
- [var writesDepth: Bool](unlitmaterial/writesdepth-5gfwa.md)
  A boolean value that determines whether this material writes its depth into RealityKit’s depth buffer.
### Type Aliases
- [UnlitMaterial.BaseColor](unlitmaterial/basecolor-4bbsb.md)
  The type used to represent base color.
- [UnlitMaterial.BaseColor](unlitmaterial/basecolor-dbh3.md)
  The type used to represent base color.
- [UnlitMaterial.Blending](unlitmaterial/blending-53ard.md)
  The type used to represent opacity information.
- [UnlitMaterial.Blending](unlitmaterial/blending-8ev2p.md)
  The type used to represent opacity information.
- [UnlitMaterial.FaceCulling](unlitmaterial/faceculling-5naqt.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [UnlitMaterial.FaceCulling](unlitmaterial/faceculling-wlgw.md)
  An alias for the cull mode object that’s appropriate for this material class.
- [UnlitMaterial.Texture](unlitmaterial/texture-6ew65.md)
  The type used to represent textures.
- [UnlitMaterial.Texture](unlitmaterial/texture-8p34r.md)
  The type used to represent textures.
- [UnlitMaterial.TextureCoordinateTransform](unlitmaterial/texturecoordinatetransform-295ea.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.
- [UnlitMaterial.TextureCoordinateTransform](unlitmaterial/texturecoordinatetransform-9w7o8.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.
- [UnlitMaterial.TriangleFillMode](unlitmaterial/trianglefillmode-4gpdd.md)
- [UnlitMaterial.TriangleFillMode](unlitmaterial/trianglefillmode-5dnnu.md)

## Relationships

### Conforms To
- [Material](material.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/unlitmaterial)*