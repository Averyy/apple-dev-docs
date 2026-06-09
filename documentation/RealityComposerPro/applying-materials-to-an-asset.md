# Applying materials to an asset

**Framework**: Reality Composer Pro

Work with materials in Reality Composer Pro to enhance the appearance of your model.

#### Overview

A material defines the surface properties of a rendered 3D object.

- A **Physically Based** material closely approximates the way light reflects off real-world objects. You can use physically based materials to create highly realistic-looking objects for your scenes. They let you quickly author a material without the need to create a Shader Graph.
- The Reality Composer Pro Shader Graph lets you author custom looks for materials.

Reality Composer Pro displays materials in the active scene in the hierarchy with a paintbrush icon.

In the Project Browser, materials appear with a thumbnail.

When you select a **physically based** (PBR) material in the hierarchy view, its properties and settings open in the Inspector, where you can adjust the general properties for the material, such as Roughness, Opacity, and Emissive Color.

> 💡 **Tip**: If an imported USDZ file contains Shader Graph materials, Reality Composer Pro creates those as well. You can also create materials manually, either to change the appearance of an entity loaded from a USDZ file or to use PBR rendering with procedurally created entities.

##### Configure General Material Options

> **Note**: Available options can vary depending on the type of material.

**Shader** Sets the material shader to one of the following:

- Physically Based
- Occlusion
- Portal
- Unlit
- Shader Graph

> **Note**: The visible options described in this section can vary depending on which Shader you select in this drop-down.

**Face Culling** Face culling optimizes rendering by discarding the hidden faces of a polygon. This option determines whether the shader displays front, back, or no faces.

Options include Back, Front, or None.

**Material** Contains a list of arguments that define the overall appearance of the material.

**Reads Depth (toggle)** When toggled on, the material performs a depth test by reading the RealityKit depth buffer.

**Writes Depth (toggle)** When toggled on, the material writes its depth into the RealityKit depth buffer.

**The following options apply when you set the Shader type to Physically Based.**

**Blend Mode** The transparency of an entity (Opaque or Transparent).

> 💡 **Tip**: Available options change depending on which Blend Mode you select.

**Opacity Scale** Available when Blend Mode is set to Transparent. Sets how transparent the material is. A value of `0.0` makes the material and attached object fully transparent, and a value of `1.0` makes the material and attached object fully opaque.

**Opacity Texture** Available when Blend Mode is set to Transparent.

**Base Color Texture** Foundational image file that defines the flat, physical color of a surface without any lighting or shadow information. Determines the fundamental color of materials such as brick, wood, or cloth.

**Roughness Texture** The texture that controls how much light scatters across a surface to make objects look polished and glossy, or dry, chalky, and matte. A value of `1.0` makes the material rough, and a value of `0.0` removes all roughness to make a smooth material.

**Metallic Texture** A mask that controls how light reflects. It determines which parts of an object’s surface react like metal and which act like non-metals (such as wood, stone, or plastic).

**Normal Texture** A texture that simulates fine surface detail by perturbing how light interacts with each point on a surface. Normal maps create the appearance of bumps, grooves, and ridges without adding geometry.

**Clearcoat Texture** The transparent highlights that simulate a clear, shiny coating over an underlying material on an entity.

**Clearcoat Roughness Texture** The degree to which an entity’s clear, shiny coating scatters light to create soft highlights.

**Emissive Texture** The color of the light the entity emits. This makes a surface appear to glow or self-illuminate, regardless of surrounding light.

**Specular Texture** A grayscale image that affects the intensity of light reflections on non-metallic surfaces to control how shiny or dull a material looks at different angles.

**Ambient Occlusion Texture** Sets the degree of ambient lighting that the material receives to simulate soft shadows and subtle shading.

**Base Color Tint** Base color tint for the selected material. You can select a color or use a texture file. Four preset types are also available:

- Display - P3
- Linear Display - P3
- sRGB
- Linear sRGB

> 💡 **Tip**: If you define both a base color tint and a base color texture for the same material, the tint color tints the texture.

**Roughness Scale (0-1)** Numerical value that controls how smooth or rough a material’s surface is, which determines how light scatters when it hits the surface.

**Metallic Scale (0-1)** Numerical value that determines whether a material surface behaves as metal or a non-metal.

**Metallic** Sets how metallic the material is. A value of `0.0` removes any metallic attributes, and a value of `1.0` makes the material fully metallic.

**Opacity Threshold** A threshold below which RealityKit ignores opacity. A value of `0.0` means no additional masking occurs. If the value is greater than `0.0`, the material renders areas where the Opacity value is greater than the Opacity Threshold value.

**Lighting Model** When you set Shader to Shader Graph, this option specifies the lighting model to use.

- Lit
- Hair
- Unlit
- Clearcoat

> 💡 **Tip**: You can replace images, colors, or values for any of the PBR attributes with another image, color, or value of your choosing. Any changes you make to a material affect any entity bound to that material.

![A screenshot of the Inspector view showing material properties.](https://docs-assets.developer.apple.com/published/e50329a716d03b305844afd25212d299/PBRProperties%402x.png)

## See Also

- [Building materials in Reality Composer Pro](building-materials-in-reality-composer-pro.md)
  Apply surface properties such as color, roughness, and transparency to 3D entities in your scene.
- [Designing materials with Shader Graph](designing-materials-with-shader-graph.md)
  Create realistic materials with Reality Composer Pro’s Shader Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/applying-materials-to-an-asset)*