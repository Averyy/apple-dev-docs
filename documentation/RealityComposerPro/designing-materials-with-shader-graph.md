# Designing materials with Shader Graph

**Framework**: Reality Composer Pro

Create realistic materials with Reality Composer Pro’s Shader Graph.

#### Overview

Physically Based Rendering (PBR) materials accurately reproduce real-world surfaces, but they don’t support logic or nonrealistic effects such as cartoon shaders. Reality Composer Pro’s **Shader Graph** provides a visual, code-free node-based interface you can use to design materials with dynamic logic and highly stylized effects. The Shader Graph editor gives you extensive control over materials — including capabilities that otherwise require writing custom shaders.

![A screenshot of the Project Browser showing how to add a new material.](/images/RealityComposerPro/ShaderGraph@2x.png)

#### Review Graph Editor Basics

See [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md) to learn about general navigation and features in the Reality Composer Pro Graph Editor.

#### Open New Shader Graph Materials in the Shader Graph Editor

In the Project Browser, double-click a Shader Graph material to open it in the Shader Graph.

#### Create a Shader Graph Material

Two methods let you create a new Shader Graph material. To create a new Shader Graph material, Control-click a folder in the project browser and choose **New Material**. Alternatively, click (+) (Add Asset) > **New** > **Material**. Double-click the new Shader material to open it in the Shader Graph Editor. When the new material opens in the Shader Graph Editor, a default graph appears. The Graph Editor workspace appears as a tab at the top of the Viewport. From the Workspace tab bar, you can switch between workspace tabs as well as drag and drop the Graph Editor workspace to a new window.

See [`Configuring the project workspace`](realitycomposerpro-essentials-configuringprojectworkspace.md) to learn more about working in and configuring Reality Composer Pro workspaces.

#### Build Materials in the Shader Graph Editor

When you first open a material in the Shader Graph Editor, you will see 2 default nodes: **PreviewSurface** and **Output**.

- Nodes represent either a value or operation, and have inputs and outputs you can connect to build a material. They serve the same purpose as a variable, constant, or function in Metal.
- Multiple types of a node change the input and output types that it can receive — similar to overloads of a function.
- Build your material using the nodes that achieve your desired visual and geometric effects, and apply these materials to entities within your Reality Composer Pro scene. Above the Graph Editor, you will see the workspace for the material you are currently working on, along with any other open workspace tabs. The Inspector shows the properties for the currently selected node. In the example below, the Inspector is showing the properties for the PreviewSurface node, which is currently selected.

- When no node is selected, the Inspector displays the graph interfaces and Inputs (if any have been created).
- Below the Inspector panel (lower right) is a Preview of the material.
- The project browser displays the material in the project files. (Note that you can still interact with the project browser independently of what is shown in the Viewport.)

#### Create a New Shader Graph Material and Apply It

In the following walkthrough, you will create a new Shader Graph material, change the material, and then apply it to an entity. In the Project Browser, click [+] New Asset and then select Material. Notice in the Inspector that the properties for the new material are displayed, and that new the new material type defaults to Shader Graph.

1. In the Project Browser, name the material `my_sg_material.`  Notice in the Inspector that the material defaults to the type Shader Graph.
2. In the Project Browser, double-click `my_sg_material `to open the Shader Graph Editor. You will see 2 nodes: **PreviewSurface** and **Output**.
3. In the Preview Surface Node, click Emissive Color and then choose any color. Notice how the color affects the example in the preview tab. Notice that when you click (select) the node, its properties and settings also appear in the Inspector. Optional: Experiment with different values for Metallic, Clearcoat, Roughness, etc. and see how they affect the material in the Preview tab.
4. Above the viewport, click the World workspace.
5. In the Hierarchy, control-click World and then click **Add Child Entity** > **Geometry** > **Box**.
6. Click on the newly added box to select it and view the properties in the Inspector.
7. In the Inspector, under **Material Slots**, click the **Material** field and then select `my_sg_material`. The box should change to the color you set in step 4.

#### Add New Nodes to Shader Graph

To add a new node to a Shader Graph: Control-click in any empty space, press the Spacebar, or drag a connector from an existing node to any empty space to open the Node Selector.

1. Select a node from the Node Selector to add it to your graph. The basics of working in the Shader Graph Editor — adding and connecting nodes, comments, and changing properties —  are fundamentally the same as with any graph.  See [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md)  to learn how to use the Graph Editor.

#### Add a New Node to Your Shader Graph

The walkthrough guides you through adding a new node to the Shader Graph created in the first tutorial.

1. Open `my_sg_materi`al (created in the first tutorial) in the Shader Graph Editor.
2. In the **PreviewSurface** node, click the dot next to **Diffuse Color** and then drag it to an empty space.
3. In the Node Selector, select the **Noise 2D** node.
4. In the **Noise 2D node**, next to Amplitude, change the first number to 2. Notice the effect changing the Amplitude has on the material in the preview tab.
Try experimenting with changing other values and watch how they affect your material.

#### Change Material Attributes with Nodes

Materials you build in the editor affect both the look of an entity and its shape.

- If you build a node graph and connect it to the **Surface Shader** pin on the output node, that node graph controls the surface appearance of the model and roughly equates to writing Metal code in a fragment shader.
- If you instead connect a node graph to the **Geometry Modifier** output pin, those nodes control the shape of the entity, which equates to Metal code running in a vertex shader. Nodes represent values and operations and serve the same purpose as either a variable, constant, or function in Metal. To get the `Sin`[`https://developer.apple.com/documentation/ShaderGraph/Math/Sin`](https://developer.apple.comhttps://developer.apple.com/documentation/ShaderGraph/Math/Sin)[`https://developer.apple.com/documentation/ShaderGraph/Math/Sin`](https://developer.apple.comhttps://developer.apple.com/documentation/ShaderGraph/Math/Sin) of a value, for example, connect the value’s output pin to the input pin of a [`https://developer.apple.com/documentation/ShaderGraph/Math/Sin`](https://developer.apple.comhttps://developer.apple.com/documentation/ShaderGraph/Math/Sin).

Shader Graph contains nodes that either connect to a specific output or perform an operation, such as calculation or logic. If a node’s name starts with **Geometry Modifier,** you can only connect it to the **Geometry Modifier** output pin. If a node’s name starts with **Surface,** you can only connect it to the **Custom Surface** output pin. Nodes like `Sin` or  [`If Equal`](https://developer.apple.com/documentation/shadergraph/logic/if-equal) aren’t tied to specific outputs and just perform an operation.

> 💡 **Tip**: Node connections must be between compatible input and output types. For example, a boolean output can’t connect to a matrix input.

##### Update Material Values at Runtime

Shader Graph lets you change values on your custom materials while your app runs. Shader Graph creates **promoted inputs**, which are parameters you can set and read from Swift to change your material at runtime. Using the Input Inspector, you can set three types of material parameters through the input metadata:

- **Uniform** — A uniform is a material input that drives runtime behavior. The system polls uniform input each frame and updates the shader without recompilation. This corresponds to [`Material.Parameters`](https://developer.apple.com/documentation/realitykit/material/parameters).

> **Note**: By default, graph inputs are uniform. However, you can add metadata via the Inspector (or Control-click on the pin) and then use the demote or promote editor commands.

- **Constant** — A constant can only be adjusted when editing in the Shader Graph. This is a value which is baked into the shader. This value is opaque at runtime and immutable. Within the context of the editor constant input, it is driven from the UI and is useful for tweaking values without entering the graph editor for the material asset. All subgraph inputs are constant.

> **Note**: Setting an input as constant is the same as authoring a constant node. See [`Procedural`](https://developer.apple.com/documentation/shadergraph/procedural) for more detailed information.

- **Function Constant** — Use function constants to optimize shader performance. You access and set this material input at runtime, which causes the shader to fully recompile. After recompilation, the system bakes this value into the shader. In the API, these correspond to [`MTLFunctionConstantValues`](https://developer.apple.com/documentation/metal/mtlfunctionconstantvalues). For more information, see `MTLFunctionConstantValues`.

##### Explore Promoted Input Examples

Use promoted inputs to:

- **Turn a material’s emission on and off:** Create a Boolean input parameter and implement conditional logic based on its value.
- **Smoothly interpolate between two colors:** Create a `Float` input parameter and use it to control the interpolation between the two colors.

##### Configure Shader Graph Node Options

The following options apply to nodes used in Shader Graphs.

- **Increase Half Precision** — For each selected shader-graph node whose connectors are half-precision, this option swaps the node for the equivalent member of its generic group whose half connectors are upgraded to float. Note that column and row size are preserved while non-half connectors must match exactly. Also logs an info message and skips the node if no float counterpart exists. Note that this option does not apply to input, output, or subgraph nodes.
- **Decrease Float Precision** — Converts a standard 32-bit float precision number to a half precision (16-bit) float. You typically decrease float precision to improve performance, optimize memory usage, or constrain floating-point accuracy.
- **Apply Color Dithering (True/False)** — When you set Shader to Shader Graph, this option turns color dithering on or off — a technique that uses patterns of tiny dots (stippling) to create the illusion of smooth gradients, color blending, or transparency.
- **Blend Mode** — When you set Shader to Shader Graph, this option specifies the blend mode to use: - Opaque
- Alpha
- Add

> **Note**: Blend Mode overrides the default behavior. If you don’t set a blend mode, the system infers one based on the parameters connecting to the surface.

## See Also

- [Building materials in Reality Composer Pro](building-materials-in-reality-composer-pro.md)
  Apply surface properties to 3D entities to control how they look in your scene.
- [Applying materials to an asset](applying-materials-to-an-asset.md)
  Assign and configure surface materials on 3D model assets in Reality Composer Pro.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/designing-materials-with-shader-graph)*