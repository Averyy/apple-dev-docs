# Applying RealityKit materials to your assets

**Framework**: Reality Composer Pro

Work with materials in Reality Composer Pro to enhance the appearance of your model.

#### Overview

When you import a USDZ model into Reality Composer Pro, it creates a RealityKit material for every material the asset contains. Reality Composer Pro displays any materials in the active scene in the hierarchy view, represented by a paintbrush icon.

![A screenshot of Reality Composer Pro’s navigator view with a USDZ file named cup_saucer_set displayed. In the cup_saucer_set hierarchy, a folder named Looks is opened and a material is highlighted.](https://docs-assets.developer.apple.com/published/6bb0261de4ccb56bdf9c59948519a566/RCPro-MaterialHierarchy.png)

If you select a material in the hierarchy view, you can edit it and adjust its values — such as Roughness, Opacity, and Emissive Color — using the inspector, as shown in the screenshot below.

![A screenshot of a material in Reality Composer Pro’s inspector view. The material contains three sections named References, Material, and Advanced. Material contains a list of the following arguments: Shader, Face Culling, Diffuse Color, Roughness, Metallic, Opacity, and Normal. Advanced contains a list of the following arguments: Clearcoat, Clearcoat Roughness, Emissive Color, Index of Refraction, Ambient Occlusion, and Opacity Threshold.](https://docs-assets.developer.apple.com/published/9c1ad6ca53a6f62f6465e8a1e5b476fc/RCPro-MaterialInspector-PBR%402x.png)

A material’s inspector view contains three sections: References, Material, and Advanced. The References section lists any entities using the selected material, and allows you to add or remove references. The Material section contains a list of arguments that define the overal appearance of the material.

- ****Shader****: Sets the material shader to either a Physically Based type or a Shader Graph type.
- ****Face Culling****: Determines if the shader displays front, back, or no faces.
- ****Diffuse Color****: Sets the color of the material. You can select a color or utilize a texture file.
- ****Roughness****: Sets how smooth or rough the material is. A value of `1.0` makes the material rough, and a value of `0.0` removes all roughness to make a smooth material.
- ****Metallic****: Sets how metallic the material is. A value of `0.0` removes any metallic attributes, and a value of `1.0` makes the material fully metallic.
- ****Opacity****: Sets how transparent the material is. A value of `0.0` makes the material and attached object fully opaque, and a value of `1.0` makes the material and attached object fully visible.
- ****Normal****: Sets the surface details of the material. An imported asset may come with a normal texture map to change the way light reacts on the material without adding additional polygons.

The Advanced section includes additional arguments you can use to fine-tune certain aspects of the selected material.

- ****Clearcoat****: Sets the material to have a clear reflective layer on top. A value of `0.0` disables the Clearcoat layer.
- ****Clearcoat Roughness****: Sets how smooth or rough the Clearcoat layer is, similar to the Roughness parameter.
- ****Emissive Color****: Sets the self-illumination color of the material. Providing a color or a texture file enables the material to emit its own light with any attached entities acting as the light source. A value of `0,0,0` disables Emissive Color.
- ****Index of Refraction****: Sets how much of a Fresnel reflection effect the material has.
- ****Ambient Occlusion****: Sets the degree of ambient lighting that the material receives to simulate soft shadows and subtle shading.
- ****Opacity Threshold****: Sets whether a portion of the material renders based on its opacity level. A value of `0.0` means no additional masking occurs. If the value is greater than `0.0`, the material renders areas where the Opacity value is greater than the Opacity Threshold value.

> 💡 **Tip**: The library in Reality Composer Pro contains materials for several common real-world surfaces like metal, wood, and denim that you can import into your project.

If you select a Physically Based Rendering (PBR) material in the hierarchy view, you can edit it using the inspector. You can replace images, colors, or values for any of the PBR attributes with another image, color, or value of your choosing. Any changes you make to a material affect any entity that’s bound to that material. You can also create new materials from scratch by clicking the Add button (+) at the bottom of the scene hierarchy and choosing Material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/applying-realitykit-materials-on-imported-assets)*