# Designing materials with Shader Graph

**Framework**: Reality Composer Pro

Create realistic materials with Reality Composer Pro’s Shader Graph.

#### Overview

Physically Based Rendering (PBR) materials accurately reproduce real-world surfaces, but they don’t support logic or nonrealistic effects such as cartoon shaders. Reality Composer Pro’s **Shader Graph** provides a visual, code-free node-based interface you can use to design materials with dynamic logic and highly stylized effects.

The Shader Graph editor gives you extensive control over materials — including capabilities that otherwise require writing custom shaders.

![A screenshot of the Project Browser showing how to add a new material.](https://docs-assets.developer.apple.com/published/b2574806a6f2e316b464429b6c7d2708/ShaderGraph%402x.png)

##### Review Prerequisite Concepts

See [`Working with the Graph Editor`](realitycomposerpro-essentials-grapheditoroverview.md) to learn about general navigation and features in the Reality Composer Pro Graph Editor.

##### Create a Shader Graph Material

Two methods let you create a new Shader Graph material.

> **Note**: Newly created materials default to the Shader type. For more information about different types of materials and their properties, see [`Applying materials to an asset`](applying-materials-to-an-asset.md).

To create a new Shader Graph material, Control-click a folder in the project browser and choose **New Material**. Alternatively, click **(+)** (Add Asset) > New > Material. Either method creates a material whose shader setting defaults to Shader Graph. Double-click the new Shader material to open it in the Shader Graph Editor.

When the new material opens in the Shader Graph Editor, a default graph appears.

The Graph Editor workspace appears as a tab at the top of the Viewport.

From the Workspace tab bar, you can switch between workspace tabs as well as drag and drop the Graph Editor workspace to a new window.

See [`Configuring the project workspace`](realitycomposerpro-essentials-configuringprojectworkspace.md) to learn more about working in and configuring Reality Composer Pro workspaces.

##### Add New Nodes to a Shader Graph

Working in the Shader Graph Editor is fundamentally the same as with any graph.

##### Change Material Attributes with Nodes

Materials you build in the editor affect both the look of an entity and its shape.

If you build a node graph and connect it to the **Surface Shader** pin on the output node, that node graph controls the surface appearance of the model and roughly equates to writing Metal code in a fragment shader. If you instead connect a node graph to the **Geometry Modifier** output pin, those nodes control the shape of the entity, which equates to Metal code running in a vertex shader.

Nodes represent values and operations and serve the same purpose as either a variable, constant, or function in Metal.

To get the sine of a value, for example, connect the value’s output pin to the input pin of a [`Sin`](https://developer.apple.com/documentation/ShaderGraph/Math/Sin) node.

Shader Graph contains nodes that either connect to a specific output or perform an operation, such as calculation or logic. If a node’s name starts with **Geometry Modifier,** you can only connect it to the **Geometry Modifier** output pin. If a node’s name starts with **Surface,** you can only connect it to the **Custom Surface** output pin. Nodes like `Sin` or [`If Equal`](https://developer.apple.com/documentation/ShaderGraph/Logic/If-Equal) aren’t tied to specific outputs and just perform an operation.

> 💡 **Tip**: Node connections must be between compatible input and output types. For example, a boolean output can’t connect to a matrix input.

##### Update Material Values at Runtime

Shader Graph lets you change values on your custom materials while your app runs. Shader Graph creates **promoted inputs**, which are parameters you can set and read from Swift to change your material at runtime.

Using the Input Inspector, you can set three types of material parameters through the input metadata:

- **Uniform** — A uniform is a material input that drives runtime behavior. The system polls uniform input each frame and updates the shader without recompilation. This corresponds to [`Material.Parameters`](https://developer.apple.com/documentation/RealityKit/Material/Parameters).

> **Note**: By default, graph inputs are uniform. However, you can add metadata via the Inspector (or Control-click on the pin) and then use the demote or promote editor commands.

- **Constant** — A constant can only be adjusted when editing in the Shader Graph. This is a value which is baked into the shader. This value is opaque at runtime and immutable. Within the context of the editor constant input, it is driven from the UI and is useful for tweaking values without entering the graph editor for the material asset. All subgraph inputs are constant.

> **Note**: Setting an input as constant is the same as authoring a constant node. See [`Procedural`](https://developer.apple.com/documentation/ShaderGraph/Procedural) for more detailed information.

- **Function Constant** — Use function constants to optimize shader performance. You access and set this material input at runtime, which causes the shader to fully recompile. After recompilation, the system bakes this value into the shader. In the API, these correspond to [`MTLFunctionConstantValues`](https://developer.apple.com/documentation/Metal/MTLFunctionConstantValues). For more information, see `MTLFunctionConstantValues`.

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
  Apply surface properties such as color, roughness, and transparency to 3D entities in your scene.
- [Applying materials to an asset](applying-materials-to-an-asset.md)
  Work with materials in Reality Composer Pro to enhance the appearance of your model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/designing-materials-with-shader-graph)*