# PhysicallyBasedMaterial.Normal

**Framework**: RealityKit  
**Kind**: struct  
**Role**: Structure

An object that specifies an entity’s normal map.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 26.0+
- visionOS

## Declaration

```swift
struct Normal
```

## Overview

The `normal` property of a RealityKit entity holds an optional *normal map*, which stores fine details about the entity’s surface, using a texture rather than increasing the number of polygons in the model. If you provide a normal map, RealityKit uses the vectors from that normal map when rendering the entity, resulting in greater detail and more accurate highlights, shadows, and reflections.

## Topics

### Creating a normal object
- [init(texture: PhysicallyBasedMaterial.Texture?)](./normal-swift.struct/init%28texture%29.md)
  Creates an object from a specified texture.
- [init(CustomMaterial.Normal)](./normal-swift.struct/init%28_%29.md)
  Creates a normal object from a custom material’s normal property.
### Accessing the normal map
- [var texture: PhysicallyBasedMaterial.Texture?](./normal-swift.struct/texture.md)
  The material’s normal map.
- [static let textureSemantic: TextureResource.Semantic](./normal-swift.struct/texturesemantic.md)
  The intended use of the object’s texture property.

## See Also

### Realistic materials
- [Applying realistic material and lighting effects to entities](../applying-realistic-material-and-lighting-effects-to-entities.md)
  Enhance the appearance of objects in a RealityKit scene with Physically Based Rendering (PBR).
- [Rendering high-fidelity characters](../rendering-high-fidelity-characters.md)
  Configure material and lighting properties to avoid flat, dull skin and static hair on your characters.
- [Generating procedural textures](../../visionOS/generating-procedural-textures-in-visionos.md)
  Display a 3D model that generates procedural textures in a reality view.
- [struct PhysicallyBasedMaterial](../physicallybasedmaterial.md)
  A material that simulates the appearance of real-world objects.
- [PhysicallyBasedMaterial.BaseColor](./basecolor-swift.struct.md)
  An object that defines an entity’s base color.
- [PhysicallyBasedMaterial.Roughness](./roughness-swift.struct.md)
  An object that defines the roughness of an entity’s surface.
- [PhysicallyBasedMaterial.Metallic](./metallic-swift.struct.md)
  An object that defines the reflectiveness of an entity.
- [PhysicallyBasedMaterial.Blending](./blending-swift.enum.md)
  The object that defines the transparency of an entity.
- [PhysicallyBasedMaterial.AmbientOcclusion](./ambientocclusion-swift.struct.md)
  An object that defines the ambient occlusion of an entity’s surface.
- [PhysicallyBasedMaterial.Specular](./specular-swift.struct.md)
  An object that defines the specular highlights of an entity.
- [PhysicallyBasedMaterial.SheenColor](./sheencolor.md)
  An object that defines the color of an entity’s sheen.
- [PhysicallyBasedMaterial.Clearcoat](./clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [PhysicallyBasedMaterial.ClearcoatRoughness](./clearcoatroughness-swift.struct.md)
  An object that defines the degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [PhysicallyBasedMaterial.AnisotropyLevel](./anisotropylevel-swift.struct.md)
  An object that defines the degree to which an entity reflects light to create stretched or oblong highlights.
- [PhysicallyBasedMaterial.AnisotropyAngle](./anisotropyangle-swift.struct.md)
  An object used to define a material’s anisotropy angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicallybasedmaterial/normal-swift.struct)*