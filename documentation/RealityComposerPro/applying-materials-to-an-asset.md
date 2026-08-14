# Applying materials to an asset

**Framework**: Reality Composer Pro

Assign and configure surface materials on 3D model assets in Reality Composer Pro.

#### Overview

A material defines the surface properties of a rendered 3D object. Reality Composer Pro supports five material types: Physically Based, Unlit, Occlusion, Portal, and Shader Graph. The Inspector shows different properties based on which material is selected.

- **Physically Based** — Closely approximates the way light reflects off real-world objects, letting you quickly author realistic-looking surfaces without a Shader Graph.

- **Unlit** —  Unlit materials do not respond to scene lighting. Their color appears exactly as specified, regardless of virtual or real-world illumination.
- **Occlusion** —Occlusion materials render as invisible while still occluding geometry behind them in the depth buffer.
- **Portal **— Portal materials work with the Portal component to render the contents of a separate world through a mesh surface, creating the visual effect of a window or doorway into another scene.

- **Shader Graph** — Lets you author fully custom looks using a node-based visual editor.

Reality Composer Pro displays materials in the active scene hierarchy with a paintbrush icon, and in the Project Browser with a thumbnail.

> 💡 **Tip**: If an imported USDZ file contains Shader Graph materials, Reality Composer Pro creates those as well. You can also create materials manually, either to change the appearance of an entity loaded from a USDZ file or to use PBR rendering with procedurally created entities.

#### Apply a Material to an Asset

Apply a material to an asset or entity through the Inspector, under the Material Slots section.

In the Hierarchy, click an entity (such as a model). Alternatively, click an entity in the Viewport.

When you select a **Physically Based** (PBR) material in the hierarchy view, its properties and settings open in the Inspector. There you can adjust properties such as Roughness, Opacity, and Emissive Color.

In the Inspector, under **Material Slots**, click the material field next to **Material**. The field may be blank or set to `default_material`. Select a material from the list.

#### Configure General Material Options

Available options vary depending on the type of material.

**Shader** Sets the material shader. Choose the type that best matches your authoring intent:

- **Physically Based** — Use for realistic, light-responsive surfaces such as metal, wood, or fabric.
- **Occlusion** — Use to hide objects while still displaying their shadows.
- **Portal** — Use to create windows or openings into another space.
- **Unlit** — Use for surfaces that should not respond to scene lighting, such as emissive surfaces or UI overlays.
- **Shader Graph** — Use to create fully custom material looks beyond the built-in presets.

The visible options in this section vary depending on which Shader you select in the Shader drop-down menu.

**Face Culling** Face culling optimizes rendering by discarding the hidden faces of a polygon. This option determines whether the shader displays front, back, or no faces.

Options include Back, Front, or None.

**Material** Contains a list of arguments that define the overall appearance of the material.

**Reads Depth (toggle)** When toggled on, the material performs a depth test by reading the RealityKit depth buffer.

**Writes Depth (toggle)** When toggled on, the material writes its depth into the RealityKit depth buffer.

#### Configure Physically Based Material Options

The following properties appear when you set **Shader** to **Physically Based**.

**Blend Mode** Controls the transparency of an entity. Options are Opaque or Transparent.

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

**Metallic Scale (0-1)** Numerical value that determines whether a material surface behaves as metal or a non-metal. A value of `0.0` removes any metallic attributes, and a value of `1.0` makes the material fully metallic.

**Opacity Threshold** A threshold below which RealityKit ignores opacity. A setting of `0.0` means no additional masking occurs. If set above `0.0`, the material renders areas where the Opacity is greater than the Opacity Threshold.

#### Configure Shader Graph Material Options

The following property appears when you set **Shader** to **Shader Graph**.

**Lighting Model** Specifies the lighting model to use. Different sub-properties will be displayed depending on the lighting model selected. The Lighting Model selector is most useful when you have a Lit material and want to override specific rendering attributes without changing the surface output node.

- Unspecified -  Unspecified lets RealityKit infer the lighting model from the surface output node in the graph.

- Lit -  Lit produces standard PBR-style shading.

- Unlit - Unlit skips lighting and shows the surface color directly.

- Hair - Hair uses an anisotropic model tuned for hair strands.

- Clearcoat - Clearcoat adds a separate transparent specular layer on top of the base material, simulating coatings such as automotive paint or lacquer.

> 💡 **Tip**: You can replace images, colors, or values for any of the PBR attributes with another image, color, or value of your choosing. Any changes you make to a material affect any entity bound to that material.

![A screenshot of the Inspector view showing material properties.](/images/RealityComposerPro/PBRProperties@2x.png)

## See Also

- [Building materials in Reality Composer Pro](building-materials-in-reality-composer-pro.md)
  Apply surface properties to 3D entities to control how they look in your scene.
- [Designing materials with Shader Graph](designing-materials-with-shader-graph.md)
  Create realistic materials with Reality Composer Pro’s Shader Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/applying-materials-to-an-asset)*