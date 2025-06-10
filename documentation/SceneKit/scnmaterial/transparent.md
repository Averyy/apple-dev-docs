# transparent

**Framework**: SceneKit  
**Kind**: property

An object that determines the opacity of each point in a material.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var transparent: SCNMaterialProperty { get }
```

#### Discussion

Use this property to selectively make parts of a material appear transparent. You can uniformly adjust the opacity of a material using its [`transparency`](scnmaterial/transparency.md) property, or of all the content attached to a node using the node’s [`opacity`](scnnode/opacity.md) property.

By default, the transparent property’s [`contents`](scnmaterialproperty/contents.md) object is a fully opaque black color, causing the property to have no visible effect. Setting the transparent property’s contents to any solid color uniformly fades the opacity of the material based on that color’s opacity value. To make parts of a material appear transparent, set the property’s contents to an image or other texture-mapped content whose alpha channel defines areas of full or partial opacity.

The figure below shows a semitransparent material before and after providing a texture image for its transparent property. (To make the transparency effect more visible, a blue sphere is shown behind the transparent material.)

![None](https://docs-assets.developer.apple.com/published/18728322bdfbb6ca75704b7d1745b286/media-2934166%402x.png)

The [`transparencyMode`](scnmaterial/transparencymode.md) property controls how SceneKit interprets color information from the transparent property’s contents.

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
- [var multiply: SCNMaterialProperty](scnmaterial/multiply.md)
  An object that provides color values that are multiplied with pixels in a material after all other shading is complete.
- [var shininess: CGFloat](scnmaterial/shininess.md)
  The sharpness of specular highlights. Animatable.
- [var fresnelExponent: CGFloat](scnmaterial/fresnelexponent.md)
  A factor affecting the material’s reflectivity. Animatable.
- [var locksAmbientWithDiffuse: Bool](scnmaterial/locksambientwithdiffuse.md)
  A Boolean value that determines whether the material responds identically to both ambient and diffuse lighting. Animatable.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnmaterial/transparent)*