# Building materials in Reality Composer Pro

**Framework**: Reality Composer Pro

Apply surface properties to 3D entities to control how they look in your scene.

#### Overview

Materials define how an object’s surface interacts with light. Properties such as color, roughness, metallic finish, and transparency determine whether an asset looks like shiny metal, rough wood, or translucent glass.

#### Choose a Material Type

Reality Composer Pro offers several material types you can use to achieve virtually any effect:

- **Physically Based** — Physically based materials simulate how surfaces interact with light in the real world. See [`PhysicallyBasedMaterial`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial) for more information.
- **Occlusion** — Occlusion materials create invisible surfaces that hide virtual content behind them, letting virtual objects appear to pass behind real-world surfaces or other invisible boundaries. See [`OcclusionMaterial`](https://developer.apple.com/documentation/RealityKit/OcclusionMaterial) for more information.
- **Portal** — Portal materials simulate looking through a window, a gateway, or a rip in space into another location. See [`PortalMaterial`](https://developer.apple.com/documentation/RealityKit/PortalMaterial) for more information.
- **Shader Graph** — Shader Graph materials are custom materials created in a visual, node-based workflow. Unlike PBR or Unlit, Shader Graph materials support arbitrary logic, animation, and runtime parameter changes. These are the materials you work with in the Shader Graph Editor to create virtually any type of material and its unique properties. See [`ShaderGraphMaterial`](https://developer.apple.com/documentation/RealityKit/ShaderGraphMaterial) for more information.
- **Unlit** — Unlit materials don’t respond to lights in the scene. Their color and brightness remain consistent regardless of the environment’s lighting conditions. See [`UnlitMaterial`](https://developer.apple.com/documentation/RealityKit/UnlitMaterial) for more information.

#### Create a Material Asset

You can create a material in two ways.

In the Project Browser, Control-click anywhere in your project, then select **New** > **Material**. The new material defaults to the Shader Graph material type. After creating the material, double-click it in the Project Browser to open it in the **Shader Graph Editor**.

![A screenshot of the Project Browser showing how to add a new material.](https://docs-assets.developer.apple.com/published/8a9021fd3cb47d130a246c0eeb6bf916/AddAsset%402x.png)

Another way to create a material in the Project Browser is to click **[+]** and then select **Material**.

> **Note**: Clicking (selecting) material assets that are not Shader Graph or Portal materials shows the material properties in the Inspector, where you can edit the properties specific to the type of shader. Double-click Portal or Shader Graph materials to open them in the Graph Editor.

> **Note**: When you add a new Geometry Entity (Plane, Sphere, or Box) to the Scene Hierarchy, Reality Composer Pro automatically assigns `default_material` under Material Slots in the Inspector and classifies it as a **Shader Graph**. You can click `default_material` to select another material, or change Shader Graph to another option.

![A screenshot showing the default material assigned to a new geometry entity.](https://docs-assets.developer.apple.com/published/eb8d0e4ea90d18aa655f66243ac794c9/addNewGeometry%402x.png)

> **Note**: If you change `default_material`, those changes affect every new geometry entity that uses this material.

#### Create a Physically Based Material and Apply It to an Entity

In this example, you create a new Physically Based material, change its color, and apply it to an entity.

1. In the Project Browser, click **[+]** New Asset and select **Material**. The Inspector shows the new material’s properties; the material type defaults to **Shader Graph**. Name the material `my_pbr_material` in the Project Browser.
2. In the Inspector, click the **Shader** field and select **Physically Based**. The Inspector updates to show the properties specific to Physically Based materials.
3. Click **Base Color Tint** and choose a new color — try yellow. The color updates in the preview tab.
4. In the Hierarchy, control-click **World** and choose **Add Child Entity** > **Geometry** > **Box**. Click the newly added box to select it and view its properties in the Inspector.
5. In the Inspector, under **Material Slots**, click the **Material** field and select `my_pbr_material`. The box updates to the color you set for the material.

#### View and Change Material Properties

You can view and interact with materials in the Hierarchy, Project Browser, Viewport, and the Inspector.

- Materials in the currently active scene appear in the Hierarchy as a paintbrush icon.
- Materials appear in the Project Browser as a thumbnail.

When you select a material, its properties appear in the Inspector, where you can view or change the material properties.

You can preview changes made to materials in the preview tab and in the Viewport.

#### Inspect Materials in the Hierarchy

In the Hierarchy:

- Select a material in the Hierarchy to change the material that the instance is pointing to.
- You can click a model and then view the material applied to it in the Inspector.

![A screenshot showing a material selected in the scene hierarchy.](https://docs-assets.developer.apple.com/published/7906d11d625ab5bf9be2e05615ce20fa/DefaultMaterial%402x.png)

#### Inspect Materials in the Project Browser

In the Project Browser:

- Select (click) a material in the Project Browser to directly edit its properties and settings in the Inspector.
- Double-click a Shader Graph material to open the Shader Graph Editor. See [`Designing materials with Shader Graph`](designing-materials-with-shader-graph.md) to learn about working with Shader Graph materials.

![A screenshot showing a material selected in the Project Browser.](https://docs-assets.developer.apple.com/published/48b5a1e062fdf6833851d5e1866e0372/ShaderGraph-ShaderGraph%402x.png)

#### Inspect Materials in the Viewport

You can’t select a material directly in the viewport. However, selecting an entity displays its components and material properties in the Inspector.

> 💡 **Tip**: You can reassign a material from the Model Component. Under **Model Component** > **Material Slots**, click the Material field and select a different material.

#### Inspect Materials in the Inspector

In the Inspector, you can:

- Change the physical properties (metallic, roughness, and other surface properties) for a Physically Based material.
- Change the assigned material and adjust the same basic material properties available when viewing the material through the Project Browser.
- Change properties for Portal, Occlusion, and Unlit materials.
- Change general properties for a Shader Graph material.
- Double-click a Shader Graph material to open it in the Shader Graph Editor, which allows you extensive control for a fully custom material. See [`Designing materials with Shader Graph`](designing-materials-with-shader-graph.md) to learn more.
- Apply a material to a selected entity, such as a model.

#### Review Material Property Options

Each type of material has different properties and settings you can apply to it. When you first create a new material or select one in the Hierarchy or Project Browser, the Inspector shows these properties, where you can view and edit them.

Depending on which view you’re interacting with and the type of material, you see different information and material properties in the Inspector. Each type of shader material has its own set of options — not every type of material has all of the following options. For example, Reads Depth does not apply to Occlusion materials.

##### Shader

Sets the material shader to one of the following:

- Physically Based
- Occlusion
- Portal
- Unlit
- Shader Graph

##### Face Culling

Face culling optimizes rendering by discarding the hidden faces of a polygon. Determines if the shader displays front, back, or no faces. See [`CustomMaterial.FaceCulling`](https://developer.apple.com/documentation/RealityKit/CustomMaterial/FaceCulling-swift.typealias) for more information.

Options include Back, Front, or None.

##### Material

Contains a list of arguments that define the overall appearance of the material.

##### Reads Depth Toggle

When toggled on, the material performs a depth test by reading RealityKit’s depth buffer.

##### Writes Depth Toggle

When toggled on, the material writes its depth into RealityKit’s depth buffer.

##### Physically Based Material Options

The following options apply when the Shader type is set to **Physically Based**. See [`PhysicallyBasedMaterial`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial) in the Apple Developer Documentation for more information.

##### Blend Mode

The transparency of an entity (Opaque or Transparent). See [`CustomMaterial.Blending`](https://developer.apple.com/documentation/RealityKit/CustomMaterial/Blending-swift.enum) for more information.

> **Note**: Available options change depending on which Blend Mode is selected.

##### Opacity Scale

Available when Blend Mode = Transparent. Sets the opacity of the material. A value of 0.0 makes the material fully transparent, and a value of 1.0 makes the material fully opaque. See [`CustomMaterial.Opacity`](https://developer.apple.com/documentation/RealityKit/CustomMaterial/Opacity) for more information.

##### Opacity Texture

Available when Blend Mode = Transparent.

##### Base Color Texture

Foundational image file that defines the flat, physical color of a surface without any lighting or shadow information. Determines the fundamental color of materials like brick, wood, or cloth. See [`PhysicallyBasedMaterial.BaseColor`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/BaseColor-swift.struct) for more information.

##### Roughness Texture

The texture that determines how much light scatters across a surface, making objects look polished and glossy or dry, chalky, and matte. A value of 1.0 makes the material rough, and a value of 0.0 removes all roughness to make a smooth material. See [`PhysicallyBasedMaterial.Roughness`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/Roughness-swift.struct) for more information.

##### Metallic Texture

A mask that controls how light is reflected. It determines which parts of an object’s surface react like metal and which act like non-metals (like wood, stone, or plastic). See [`PhysicallyBasedMaterial.Metallic`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/Metallic-swift.struct) for more information.

##### Normal Texture

A UV-mapped image that encodes surface normals to simulate fine surface details without adding geometry. See [`PhysicallyBasedMaterial.Normal`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/Normal-swift.struct) for more information.

##### Clearcoat Texture

The transparent highlights that simulate a clear, shiny coating over an underlying material on an entity. See [`PhysicallyBasedMaterial.Clearcoat`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/Clearcoat-swift.struct) for more information.

##### Clearcoat Roughness Texture

The degree to which an entity’s clear, shiny coating scatters light to create soft highlights. See [`PhysicallyBasedMaterial.ClearcoatRoughness`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/ClearcoatRoughness-swift.struct) for more information.

##### Emissive Texture

The color of the light the entity emits. This makes a surface appear to glow or self-illuminate, regardless of surrounding light. See [`PhysicallyBasedMaterial.EmissiveColor`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/EmissiveColor-swift.struct) for more information.

##### Specular Texture

A grayscale image that affects the intensity of light reflections on non-metallic surfaces to control how shiny or dull a material looks at different angles. See [`PhysicallyBasedMaterial.Specular`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/Specular-swift.struct) for more information.

##### Ambient Occlusion Texture

Sets the degree of ambient lighting that the material receives to simulate soft shadows and subtle shading. See [`PhysicallyBasedMaterial.AmbientOcclusion`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/AmbientOcclusion-swift.struct) for more information.

##### Base Color Tint

Tints the base color for the material. You can select a color or use a texture file. Four preset types are also available:

- Display - P3
- Linear Display - P3
- sRGB
- Linear sRGB

See [`PhysicallyBasedMaterial.BaseColor`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial/BaseColor-swift.struct) for more information.

> **Note**: If both Base Color Tint and Base Color Texture are defined for the same material, the system uses the tint color to tint the texture.

##### Roughness Scale 0 1

Numerical value that determines how smooth or rough a material’s surface is, which determines how light scatters when it hits it.

##### Metallic Scale 0 1

Numerical value that controls how metallic the material surface appears. A value of 0.0 removes any metallic attributes, and a value of 1.0 makes the material fully metallic.

##### Opacity Threshold

A threshold below which RealityKit ignores opacity. A value of 0.0 means no additional masking occurs. If the value is greater than 0.0, the material renders areas where the Opacity value is greater than the Opacity Threshold value.

##### Shader Graph Material Options

The following options apply when the Shader type is set to **Shader Graph**.

##### Lighting Model

Specifies the lighting model to use. See [`CustomMaterial.LightingModel`](https://developer.apple.com/documentation/RealityKit/CustomMaterial/LightingModel-swift.enum) for more information.

- Lit
- Unlit
- Clearcoat

You can replace images, colors, or values for any of the PBR attributes with another image, color, or value of your choosing. Any changes you make to a material affect any entity bound to that material.

## See Also

- [Applying materials to an asset](applying-materials-to-an-asset.md)
  Assign and configure surface materials on 3D model assets in Reality Composer Pro.
- [Designing materials with Shader Graph](designing-materials-with-shader-graph.md)
  Create realistic materials with Reality Composer Pro’s Shader Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-materials-in-reality-composer-pro)*