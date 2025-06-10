# Applying realistic material and lighting effects to entities

**Framework**: RealityKit

Enhance the appearance of objects in a RealityKit scene with Physically Based Rendering (PBR).

#### Overview

A [`Material`](material.md) instance describes the surface properties of an entity and controls how RealityKit renders that entity. A [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) is a type of material that closely approximates the way light bounces off objects in the real world. It creates very realistic rendered objects that look natural when placed into an AR scene.

When you import models from USDZ files, RealityKit automatically creates one or more [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) instances from the PBR material settings in the file. You can also create PBR materials manually, either to change the appearance of an entity loaded from a USDZ file at runtime, or to use PBR rendering with procedurally created entities.

##### Create a Material and Specify Core Properties

PBR materials use three core properties to define an object’s fundamental appearance: [`baseColor`](physicallybasedmaterial/basecolor-swift.property.md), [`roughness`](physicallybasedmaterial/roughness-swift.property.md), and [`metallic`](physicallybasedmaterial/metallic-swift.property.md). The [`baseColor`](physicallybasedmaterial/basecolor-swift.property.md) property defines the underlying color of the entity as it would look under soft, bright, neutral lighting with no shadows or highlights. The `roughness` property is a measure of how the surface of the entity scatters the light that it reflects. A material with a low `roughness` looks shiny, while one with a high `roughness` has a matte appearance. The `metallic` property defines how the material reflects the environment around the entity. The figure below illustrates the visual effects of changing the [`metallic`](physicallybasedmaterial/metallic-swift.property.md) and [`roughness`](physicallybasedmaterial/roughness-swift.property.md) values of a [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) while keeping its [`baseColor`](physicallybasedmaterial/basecolor-swift.property.md) unchanged.

![An illustration showing a matrix of spheres rendered with a physically based material. Each sphere has a different roughness and metallic value to demonstrate the impact of changing these attributes.](https://docs-assets.developer.apple.com/published/ff798fb7c11104058e658b0ec4144e6d/applying-realistic-material-and-lighting-effects-to-entities-1%402x.png)

This example demonstrates how to create a PBR material that uses a color and a single `roughness` and `metallic` value for the entire material:

```swift
var material = PhysicallyBasedMaterial()
material.baseColor.tint = .orange
material.roughness = PhysicallyBasedMaterial.Roughness(
    floatLiteral: 0.0
)
material.metallic = PhysicallyBasedMaterial.Metallic(
    floatLiteral: 1.0
)
```

And the following example shows how to create a PBR material using UV-mapped image textures for all three properties:

```swift
var material = PhysicallyBasedMaterial()

if let baseResource = try? TextureResource.load(named: "entity_basecolor") {
    let baseTexture = MaterialParameters.Texture(baseResource)
    material.baseColor = PhysicallyBasedMaterial.BaseColor(
        texture: baseTexture
    )
}

if let metalResource = try? TextureResource.load(named: "entity_metallic") {
    let metalTexture = MaterialParameters.Texture(metalResource)
    material.metallic = PhysicallyBasedMaterial.Metallic(
        texture: metalTexture
    )
}

if let roughnessResource = try? TextureResource.load(named: "entity_roughness") {
    let roughnessTexture = MaterialParameters.Texture(roughnessResource)
    material.roughness = PhysicallyBasedMaterial.Roughness(
        texture: roughnessTexture
    )
}
```

For [`metallic`](physicallybasedmaterial/metallic-swift.property.md) and [`roughness`](physicallybasedmaterial/roughness-swift.property.md) maps, use a grayscale image. If you use a color image, RealityKit only uses the red channel.

##### Add a Normal Map

 is a real-time rendering technique that captures fine surface details for a model using a texture instead of increasing the number of polygons in the model. It works by storing , which are vectors perpendicular to the surface of the model, from a much higher resolution version of the same 3D object. A normal map stores vectors by storing its `X`, `Y`, and `Z` value as the `R`, `G`, and `B` components of the corresponding pixel in a UV-mapped image. RealityKit uses those normals to do lighting calculations, which results in much more realistic highlights, shadows, and reflections without incurring the computational cost of using a much higher resolution 3D model.

RealityKit’s `PhysicallyBasedMaterial` supports normal maps using the [`normal`](physicallybasedmaterial/normal-swift.property.md) property.

> **Note**: RealityKit uses  which many 3D software packages can create. You can recognize tangent space normal maps by their predominately purple color.

To add a `normal` map to your entity, load it as a texture resource, and use the resource to create a `PhysicallyBasedMaterial.Normal` instance, as in this example:

```swift
if let normalResource = try? TextureResource.load(named: "entity_normals") {
    let normalTexture = MaterialParameters.Texture(normalResource)
    material.normal = PhysicallyBasedMaterial.Normal(
        texture: normalTexture
    )
}
```

##### Specify Blending and Opacity

By default, RealityKit materials are opaque, but RealityKit can render entities with transparency to simulate real-world objects. To render a material with transparency, change the [`blending`](physicallybasedmaterial/blending-swift.property.md) value from `.opaque` to `.transparent`. The `.transparent` enumeration case takes an associated value that controls the amount of transparency.

To specify opacity, create a `PhysicallyBasedMaterial.Opacity` object. You can specify opacity for the entire entity using a single value between `0.0` and `1.0`, where `1.0` is fully opaque and `0.0` is fully transparent.

```swift
material.blending = .transparent(
    opacity: PhysicallyBasedMaterial.Opacity(floatLiteral: 0.5)
)
```

You can also specify opacity using an image texture (sometimes called an  or ). In an alpha map, black pixels represent fully transparent parts of the entity, white pixels represent fully opaque parts of the entity, and gray pixels represent parts of the entity that are partially transparent.

```swift
if let opacityResource = try? TextureResource.load(named: "entity_opacity") {
    let opacityMap = MaterialParameters.Texture(opacityResource)
    let opacityValue = PhysicallyBasedMaterial.Opacity(texture: opacityMap)
    material.blending = .transparent(opacity: opacityValue)
}
```

You can change the behavior of an alpha map to function as a  rather than a transparency map. When using an alpha mask, RealityKit draws every pixel of the entity either fully transparent or fully opaque with no partially transparency. Use the [`opacityThreshold`](physicallybasedmaterial/opacitythreshold.md) property to enable alpha masking. If you specify a value greater than `0.0`, RealityKit uses the image texture as a mask, and renders any pixel with a value of less than or equal to [`opacityThreshold`](physicallybasedmaterial/opacitythreshold.md) as fully transparent. RealityKit draws any pixel value greater than [`opacityThreshold`](physicallybasedmaterial/opacitythreshold.md) as fully opaque.

##### Add Specular Highlights

RealityKit automatically draws  for physically based materials using the values of various properties, primarily [`roughness`](physicallybasedmaterial/roughness-swift.property.md) and [`metallic`](physicallybasedmaterial/metallic-swift.property.md). Specular highlights are bright spots of reflected light that appear on shiny objects.

![An illustration showing a sphere and a cube with rounded corners. Both have a shiny surface and a small white spot labeled “specular highlights” where they reflect the scene’s light source.](https://docs-assets.developer.apple.com/published/0b83dd2d5721a30ef708e7bf6420620b/applying-realistic-material-and-lighting-effects-to-entities-2%402x.png)

While many real-world objects can be accurately and realistically simulated with just the core PBR properties, you can create additional realistic effects by augmenting the specular highlights.

Use the [`specular`](physicallybasedmaterial/specular-swift.property.md) property to simulate the bright highlights found on certain  (nonmetallic) materials like cut gemstones and faceted glass, which have specular highlights much brighter than the ones RealityKit creates from just the core properties.

Here’s how to specify specular using a single value for the entire material:

```swift
material.specular = PhysicallyBasedMaterial.Specular(
    floatLiteral: 0.8
)
```

The following example demonstrates how to specify specular using a UV-mapped image texture:

```swift
if let specularResource = try? TextureResource.load(named: "entity_specular") {
    let specularTexture = MaterialParameters.Texture(specularResource)
    material.specular = PhysicallyBasedMaterial.Specular(
        texture: specularTexture
    )
}
```

You can also use specular highlights to simulate subtle reflections like the ones that occur on some types of fabric. Create these types of effects with the [`sheen`](physicallybasedmaterial/sheen.md) property, as illustrated in the following figure.

![An illustration of two spheres. The one on the right has very subtle, soft specular highlight and is labeled “With Sheen”. The one on the right has no specular highlights and is labeled “Without Sheen”.](https://docs-assets.developer.apple.com/published/359c94162d7f5fc848064f68f22585d1/applying-realistic-material-and-lighting-effects-to-entities-3%402x.png)

This example shows how to specify [`sheen`](physicallybasedmaterial/sheen.md) using a single value for the entire material:

```swift
let sheenTint = PhysicallyBasedMaterial.Color(
    red: 0.8, green: 0.8, blue: 0.8, alpha: 1.0
)
material.sheen = PhysicallyBasedMaterial.SheenColor(
    tint: sheenTint
)
```

And this example demonstrates how to specify [`sheen`](physicallybasedmaterial/sheen.md) using a UV-mapped image texture:

```swift
if let sheenResource = try? TextureResource.load(named: "entity_sheen") {
    let sheenMap = MaterialParameters.Texture(sheenResource)
    material.sheen = PhysicallyBasedMaterial.SheenColor(
        texture: sheenMap
    )
}
```

##### Use Anisotropy for Directional Highlights

By default, PBR materials are ; in other words, an entity that uses a [`PhysicallyBasedMaterial`](physicallybasedmaterial.md) reflects light uniformly in all directions, mimicking the behavior of most real-world objects. Some objects, including those with many small parallel striations such as vinyl records, CDs, or straight hair, reflect light more in some directions than others, resulting in stretched or oblong specular highlights called  highlights.

![An illustration showing 11 metallic spheres in a horizontal row. The left-most sphere is isotropic. The spheres represent increasing anisotropy from left to right, with the sphere furthest to the right displaying a long, stretched highlight.](https://docs-assets.developer.apple.com/published/2eecb2feb22234ad8501e669131a2d52/applying-realistic-material-and-lighting-effects-to-entities-4%402x.png)

In RealityKit, you adjust anisotropy using two parameters: [`anisotropyLevel`](physicallybasedmaterial/anisotropylevel-swift.property.md) and [`anisotropyAngle`](physicallybasedmaterial/anisotropyangle-swift.property.md). To control the amount of anisotropy, use [`anisotropyLevel`](physicallybasedmaterial/anisotropylevel-swift.property.md). Specifying a value of `0.0` results in an entirely isotropic appearance, while nonzero values up to `1.0` simulate the appearance of increasingly anisotropic objects. Change the angle of anisotropy to affect the direction in which the specular highlights stretch with [`anisotropyAngle`](physicallybasedmaterial/anisotropyangle-swift.property.md), which also takes a value between `0.0 `and `1.0.` `A` value of `0.0` means a rotation of 0° and a value of `1.0` indicates a rotation of 360°. To determine the [`anisotropyAngle`](physicallybasedmaterial/anisotropyangle-swift.property.md) value to use, divide the desired angle in degrees by `360.0` or the desired angle in radians by pi times 2.

```swift
let angleDegrees: Float = 125
let anisotropyAngleFromDegrees = angleDegrees / 360

let angleRadians: Float = 2.181662
let anisotropyAngleFromRadians = angleRadians / (2 * .pi)
```

The following example demonstrates how to specify anisotropy using single values for the entire material:

```swift
material.anisotropyLevel = PhysicallyBasedMaterial.AnisotropyLevel(
    floatLiteral: 0.5
)
material.anisotropyAngle = PhysicallyBasedMaterial.AnisotropyAngle(
    floatLiteral: 0.5
)
```

And this example shows how to specify anisotropy using a UV-mapped image texture for [`anisotropyLevel`](physicallybasedmaterial/anisotropylevel-swift.property.md) and a separate image for [`anisotropyAngle`](physicallybasedmaterial/anisotropyangle-swift.property.md):

```swift
if let anisoLevelResource = try? TextureResource.load(named: "entity_aniso_level") {
    let anisoLevelMap = MaterialParameters.Texture(anisoLevelResource)
    material.anisotropyLevel = PhysicallyBasedMaterial.AnisotropyLevel(
        texture: anisoLevelMap
    )
}

if let anisoAngleResource = try? TextureResource.load(named: "entity_aniso_angle") {
    let anisoAngleMap = MaterialParameters.Texture(anisoAngleResource)
    material.anisotropyAngle = PhysicallyBasedMaterial.AnisotropyAngle(
        texture: anisoAngleMap
    )
}
```

## See Also

- [struct PhysicallyBasedMaterial](physicallybasedmaterial.md)
  A material that simulates the appearance of real-world objects.
- [PhysicallyBasedMaterial.BaseColor](physicallybasedmaterial/basecolor-swift.struct.md)
  An object that defines an entity’s base color.
- [PhysicallyBasedMaterial.Roughness](physicallybasedmaterial/roughness-swift.struct.md)
  An object that defines the roughness of an entity’s surface.
- [PhysicallyBasedMaterial.Metallic](physicallybasedmaterial/metallic-swift.struct.md)
  An object that defines the reflectiveness of an entity.
- [PhysicallyBasedMaterial.Normal](physicallybasedmaterial/normal-swift.struct.md)
  An object that specifies an entity’s normal map.
- [PhysicallyBasedMaterial.Blending](physicallybasedmaterial/blending-swift.enum.md)
  The object that defines the transparency of an entity.
- [PhysicallyBasedMaterial.AmbientOcclusion](physicallybasedmaterial/ambientocclusion-swift.struct.md)
  An object that defines the ambient occlusion of an entity’s surface.
- [PhysicallyBasedMaterial.Specular](physicallybasedmaterial/specular-swift.struct.md)
  An object that defines the specular highlights of an entity.
- [PhysicallyBasedMaterial.SheenColor](physicallybasedmaterial/sheencolor.md)
  An object that defines the color of an entity’s sheen.
- [PhysicallyBasedMaterial.Clearcoat](physicallybasedmaterial/clearcoat-swift.struct.md)
  An object that defines the intensity of an entity’s clear, shiny coating.
- [PhysicallyBasedMaterial.ClearcoatRoughness](physicallybasedmaterial/clearcoatroughness-swift.struct.md)
  An object that defines the degree to which an entity’s clear, shiny coating scatters light to create soft highlights.
- [PhysicallyBasedMaterial.AnisotropyLevel](physicallybasedmaterial/anisotropylevel-swift.struct.md)
  An object that defines the degree to which an entity reflects light to create stretched or oblong highlights.
- [PhysicallyBasedMaterial.AnisotropyAngle](physicallybasedmaterial/anisotropyangle-swift.struct.md)
  An object used to define a material’s anisotropy angle.
- [PhysicallyBasedMaterial.EmissiveColor](physicallybasedmaterial/emissivecolor-swift.struct.md)
  An object that defines the color of the light an entity emits.
- [PhysicallyBasedMaterial.TextureCoordinateTransform](physicallybasedmaterial/texturecoordinatetransform-swift.typealias.md)
  An alias for the texture coordinate transform that’s appropriate for this material class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/applying-realistic-material-and-lighting-effects-to-entities)*