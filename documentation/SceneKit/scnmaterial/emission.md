# emission

**Framework**: SceneKit  
**Kind**: property

An object that defines the color emitted by each point on a surface.

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
var emission: SCNMaterialProperty { get }
```

#### Discussion

You can use an  texture to simulate parts of a surface that glow with their own light. SceneKit does not treat the material as a light source—rather, the emission property determines colors for a material independent of lighting. (To create an object that appears to glow, you may wish to combine a geometry with an emissive map and additional [`SCNLight`](scnlight.md) objects added to the scene.)

By default, the emissive property’s [`contents`](scnmaterialproperty/contents.md) object is a black color, causing the property to have no visible effect. Setting the emissive property’s contents to any solid color adds a uniform color to the material independent of lighting. To create a selective glow effect, set the property’s contents to an image or other texture-mapped content whose glowing areas use bright colors and whose other areas use darker colors. In the darker-color portions of the emissive map (and portions with reduced opacity), the other visual properties of the material contribute to its appearance under scene lighting.

The figure below shows a material (with a texture for its [`diffuse`](scnmaterial/diffuse.md) property) before and after providing an emissive map image.

![None](https://docs-assets.developer.apple.com/published/24977252ee2eb3caa547493793cdc33e/media-2934165%402x.png)

## See Also

- [var specular: SCNMaterialProperty](scnmaterial/specular.md)
  An object that manages the material’s specular response to lighting.
- [var reflective: SCNMaterialProperty](scnmaterial/reflective.md)
  An object that defines the reflected color for each point on a surface.
- [var multiply: SCNMaterialProperty](scnmaterial/multiply.md)
  An object that provides color values that are multiplied with pixels in a material after all other shading is complete.
- [var ambient: SCNMaterialProperty](scnmaterial/ambient.md)
  An object that manages the material’s response to ambient lighting.
- [var transparent: SCNMaterialProperty](scnmaterial/transparent.md)
  An object that determines the opacity of each point in a material.
- [var normal: SCNMaterialProperty](scnmaterial/normal.md)
  An object that defines the nominal orientation of the surface at each point for use in lighting.
- [var displacement: SCNMaterialProperty](scnmaterial/displacement.md)
- [var selfIllumination: SCNMaterialProperty](scnmaterial/selfillumination.md)
  An object that provides color values representing the global illumination of the surface.
- [var ambientOcclusion: SCNMaterialProperty](scnmaterial/ambientocclusion.md)
  An object that provides color values to be multiplied with the ambient light affecting the material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/emission)*