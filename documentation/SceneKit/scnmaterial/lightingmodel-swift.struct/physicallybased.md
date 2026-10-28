# physicallyBased

**Framework**: SceneKit  
**Kind**: property  
**Role**: Type Property

Shading based on a realistic abstraction of physical lights and materials.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
static let physicallyBased: SCNMaterial.LightingModel
```

```c
extern SCNLightingModel const SCNLightingModelPhysicallyBased;
```

## Discussion

Physically-based shading incorporates a refined model of the interactions between real-world lights and materials. Using modern GPU hardware and algorithms, this model can produce more realistic results than the loose abstractions of traditional shading, while also offering a set of material properties that is easier for artists to work with. Especially when combined with environmental lighting (see the [`SCNScene`](../../scnscene.md) [`lightingEnvironment`](../../scnscene/lightingenvironment.md) property) and high dynamic range cameras (see the [`SCNCamera`](../../scncamera.md) [`wantsHDR`](../../scncamera/wantshdr.md) property), physically-based shading can produce realistic results similar to those seen in recent animated feature films.

Physically based shading relies primarily on three material properties:

- The [`diffuse`](../diffuse.md) property (called albedo in some authoring tools) provides the “base” color of a material.
- The [`roughness`](../roughness.md) property (inverted and called smoothness in some authoring tools) is an approximation of the microscopic detail in a real-world surface. By approximating these “microfacets” as a single term, this property helps produce lighting calculations that resemble the energy-conserving laws of real-world physics, resulting in more realistic variation between matte and shiny surfaces.
- The [`metalness`](../metalness.md) property approximates other aspects of a physical surface, such as index of refraction, tendency to produce sharp reflections, and tendency to produce Fresnel reflections at grazing angles, which together produce an overall metallic or nonmetallic (also called dielectric) appearance.

In addition, you can add surface detail to a physically based material with the [`normal`](../normal.md) and [`ambientOcclusion`](../ambientocclusion.md) properties, and modulate the contribution of environmental lighting with the [`selfIllumination`](../selfillumination.md) property.

Physically based materials ignore the [`ambient`](../ambient.md), [`specular`](../specular.md), and [`reflective`](../reflective.md) material properties and the [`shininess`](../shininess.md), [`fresnelExponent`](../fresnelexponent.md), and [`locksAmbientWithDiffuse`](../locksambientwithdiffuse.md) parameters.

> **Note**:  Physically based rendering requires a Metal renderer. When displaying a material in a view whose [`renderingAPI`](../../scnscenerenderer/renderingapi.md) value is not [`SCNRenderingAPI.metal`](../../scnrenderingapi/metal.md), SceneKit falls back to rendering that material with the [`blinn`](./blinn.md) lighting model. (Metal rendering is not supported in Simulator or Xcode Playgrounds when targeting iOS or tvOS, and is not available at all in watchOS, so this fallback always occurs in those environments.)

## See Also

### Type Properties
- [static let blinn: SCNMaterial.LightingModel](./blinn.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Blinn-Phong  formula.
- [static let constant: SCNMaterial.LightingModel](./constant.md)
  Uniform shading that incorporates ambient lighting only.
- [static let lambert: SCNMaterial.LightingModel](./lambert.md)
  Shading that incorporates ambient and diffuse properties only.
- [static let phong: SCNMaterial.LightingModel](./phong.md)
  Shading that incorporates ambient, diffuse, and specular properties, where specular highlights are calculated using the Phong  formula.
- [static let shadowOnly: SCNMaterial.LightingModel](./shadowonly.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/lightingmodel-swift.struct/physicallybased)*