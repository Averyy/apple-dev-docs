# multiply

**Framework**: SceneKit  
**Kind**: property

An object that provides color values that are multiplied with pixels in a material after all other shading is complete.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
var multiply: SCNMaterialProperty { get }
```

#### Discussion

After combining a material’s other visual properties with lighting and other information about a scene, Scene kit multiplies the color of each rendered pixel by the color this property provides. You can use this property to darken or tint a surface independent of the effects of lighting and other properties, or to add precomputed lighting to a scene via a shadow map.

By default, the multiply property’s [`contents`](scnmaterialproperty/contents.md) object is a white color, causing the property to have no visible effect.

The figure below shows a material (with textures for its [`diffuse`](scnmaterial/diffuse.md) and [`emission`](scnmaterial/emission.md) properties) before and after setting the multiply property’s contents to a solid color. Notice that the multiply color modulates even the bright areas added by the emissive map.

![None](https://docs-assets.developer.apple.com/published/47babc79d9d4af6d7b3e1df58cddb862/media-2934159%402x.png)

## See Also

- [var normal: SCNMaterialProperty](scnmaterial/normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var emission: SCNMaterialProperty](scnmaterial/emission.md)
  An object that defines the color emitted by each point on a surface.
- [var diffuse: SCNMaterialProperty](scnmaterial/diffuse.md)
  An object that manages the material’s diffuse response to lighting.
- [var ambient: SCNMaterialProperty](scnmaterial/ambient.md)
  An object that manages the material’s response to ambient lighting.
- [var specular: SCNMaterialProperty](scnmaterial/specular.md)
  An object that manages the material’s specular response to lighting.
- [var reflective: SCNMaterialProperty](scnmaterial/reflective.md)
  An object that defines the reflected color for each point on a surface.
- [var transparent: SCNMaterialProperty](scnmaterial/transparent.md)
  An object that determines the opacity of each point in a material.
- [var shininess: CGFloat](scnmaterial/shininess.md)
  The sharpness of specular highlights. Animatable.
- [var fresnelExponent: CGFloat](scnmaterial/fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](scnmaterial/locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/multiply)*