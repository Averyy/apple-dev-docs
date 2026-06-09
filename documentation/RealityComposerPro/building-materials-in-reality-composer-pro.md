# Building materials in Reality Composer Pro

**Framework**: Reality Composer Pro

Apply surface properties such as color, roughness, and transparency to 3D entities in your scene.

#### Overview

Materials define how an object’s surface interacts with light. Properties such as color, roughness, metallic finish, and transparency determine whether an asset looks like shiny metal, rough wood, or translucent glass.

##### Choose a Material Type

Reality Composer Pro offers several material types you can use to achieve virtually any effect:

- **Physically Based** — Physically based materials simulate how surfaces interact with light in the real world. For more detailed information about physically based materials, see [`PhysicallyBasedMaterial`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial).
- **Occlusion** — Occlusion materials create invisible surfaces that hide virtual content behind them, letting virtual objects appear to pass behind real-world surfaces or other invisible boundaries.
- **Portal** — Portal materials simulate looking through a window, a gateway, or a rip in space into another location.
- **Shader Graph** — Shader Graph materials use a visual, node-based workflow to design surface properties such as color, roughness, matte, metallic, and more. These are the materials you work with in the Shader Graph Editor to create virtually any type of material and its unique properties.
- **Unlit** — Unlit materials don’t respond to lights in the scene. Their color and brightness remain consistent regardless of the environment’s lighting conditions.

Each type of material has different properties and settings you can apply to it. For a description of each material property, see [`Applying materials to an asset`](applying-materials-to-an-asset.md).

##### Create a Material Asset

You can create a material in two ways. In the Project Browser, Control-click anywhere in your project, then select **New** > **Material**. The new material defaults to the Shader Graph material type. After creating the material, double-click it in the Project Browser to open it in the **Shader Graph Editor**.

> **Note**: Double-clicking a material that isn’t a Shader Graph type doesn’t open it in the Shader Graph Editor.

Alternatively, in the Project Browser, click **+** and then select Material.

![A screenshot of the Project Browser showing how to add a new material.](https://docs-assets.developer.apple.com/published/8a9021fd3cb47d130a246c0eeb6bf916/AddAsset%402x.png)

When you add a new geometry entity (Plane, Sphere, or Box) to the scene hierarchy, Reality Composer Pro automatically assigns `default_material` under Material Slots in the Inspector and classifies it as a **Shader Graph**.

![A screenshot showing the default material assigned to a new geometry entity.](https://docs-assets.developer.apple.com/published/eb8d0e4ea90d18aa655f66243ac794c9/addNewGeometry%402x.png)

You can click `default_material` to select another material, or change Shader Graph to another option.

> **Note**: If you change `default_material`, those changes affect every new geometry entity that uses this material.

##### View Material Properties

The Inspector shows different information depending on where you select a material.

> **Note**: Any inputs marked as **public** in Shader Graph appear in the material inspector in both the Project Browser and scene hierarchy.

##### Inspect Materials in the Scene Hierarchy

In the Hierarchy:

- You can click on a model and view the material applied to the model in the Inspector.
- You can also click on a material and then click on the material in the Inspector to view its properties.

![A screenshot showing a material selected in the scene hierarchy.](https://docs-assets.developer.apple.com/published/7906d11d625ab5bf9be2e05615ce20fa/DefaultMaterial%402x.png)

##### Inspect Materials in the Project Browser

Click a material in the Project Browser to view and change its shader type and basic properties in the Inspector.

If you double-click a material in the Project Browser and the material is a Shader Graph material, the material opens in the Shader Graph Editor.

![A screenshot showing a material selected in the Project Browser.](https://docs-assets.developer.apple.com/published/48b5a1e062fdf6833851d5e1866e0372/ShaderGraph-ShaderGraph%402x.png)

##### Inspect Materials Through the Viewport

You can’t select a material directly in the viewport. However, selecting an entity displays its components and material properties in the Inspector.

> 💡 **Tip**: You can reassign a material from the Model Component. Under **Model Component** > **Material Slots**, click the Material field and select a different material.

From the Inspector, you can change the assigned material and adjust the same basic material properties available when viewing the material through the Project Browser.

##### Open a Shader Material in the Shader Graph Editor

You can extensively edit and customize materials with the Shader set to Shader Graph using logic, physics, and a wide range of options not available to other shader types.

The **Shader Graph** is a node-based material editor in Reality Composer Pro. With it, you can use a visual, node-based interface to build out node graphs to achieve virtually any material effect you can imagine without writing custom code.

- Nodes represent either a value or operation, and have inputs and outputs you can connect to build a material. They serve the same purpose as a variable, constant, or function in Metal.
- Multiple types of a node change the input and output types that it can receive — similar to overloads of a function.
- Build your material using the nodes that achieve your desired visual and geometric effects, and apply these materials to entities within your Reality Composer Pro scene.

> **Note**: Shader Graph uses MaterialX conventions to improve interoperability with content creation applications that can read and author MaterialX within USD files.

##### Build Materials in the Shader Graph Editor

When you open a basic material in the Shader Graph Editor, the editor displays a layout similar to the following:

**Graph Editor** (top) Above the Graph Editor, the workspace shows the current material and any other open workspace tabs.

**Inspector** (right panel) The Inspector shows properties for the selected node — in this example, the `PreviewSurface` node.

> **Note**: When no node is selected, the Inspector displays the **graph interfaces**.

The Inspector panel also includes a Preview of the material.

**Project Browser** (bottom) The Project Browser shows the material in the project files. You can interact with the Project Browser independently of what appears in the viewport.

## See Also

- [Applying materials to an asset](applying-materials-to-an-asset.md)
  Work with materials in Reality Composer Pro to enhance the appearance of your model.
- [Designing materials with Shader Graph](designing-materials-with-shader-graph.md)
  Create realistic materials with Reality Composer Pro’s Shader Graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/building-materials-in-reality-composer-pro)*