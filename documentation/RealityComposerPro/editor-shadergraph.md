# Designing materials with Shader Graph

**Framework**: Reality Composer Pro

Create realistic materials with Shader Graph’s node editor in Reality Composer Pro.

#### Overview

You can create two types of materials in Reality Composer Pro:

- [`PhysicallyBasedMaterial`](https://developer.apple.com/documentation/RealityKit/PhysicallyBasedMaterial)
- [`ShaderGraphMaterial`](https://developer.apple.com/documentation/RealityKit/ShaderGraphMaterial)

Physically Based Rendering (PBR) materials are great for reproducing real-world surfaces. However, they lack the ability to contain logic or represent nonrealistic materials, like cartoon shaders. Shader Graph, on the other hand, provides the tools to create shaders with dynamic logic and stylized effects.

You can build and edit Shader Graph materials using the Shader Graph editor. The Shader Graph editor has nodes that provide you a tremendous amount of control over materials, along with capabilities that would otherwise require writing Metal shaders. To explore all the nodes that are available, see [`ShaderGraph`](https://developer.apple.com/documentation/ShaderGraph).

![A screenshot that shows a complex graph of nodes in the Shader Graph tab, creating a 3D material of a mountain landscape. The graph contains three texture nodes containing a texture file, a normals file, and a height map, which are applied to the final output node.](https://docs-assets.developer.apple.com/published/1994cf8e5f506e92a38542f52d2c41a8/RCPro-ShaderGraphWindow%402x.png)

##### Change Material Attributes Using Nodes

The materials you build in the editor can affect both the look of an entity and its shape. If you build a node graph and connect it to the Custom Surface pin on the output node, that node graph controls the surface appearance of the model and roughly equates to writing Metal code in a fragment shader. If you build a node graph and connect it to the Custom Geometry Modifier output pin, those nodes control the shape of the entity, which equates to Metal code running in a vertex shader.

Nodes represent values and operations and serve the same purpose as either a variable, constant, or function in Metal. If you need the sine of a value, for example, connect the value’s output node to the input pin of a [`Sin`](https://developer.apple.com/documentation/ShaderGraph/Math/Sin) node. Add new nodes to the graph by double-clicking the background of the Shader Graph view, or click the New Node button on the right side of the screen.

> ❗ **Important**: Shader Graph contains nodes that either have a specific output that it can connect to, or perform an operation such as calculation or logic. If a node name starts with Geometry Modifier, you can only connect it to the Geometry Modifier output pin. If the node’s name starts with Surface, you can only connect it to the Custom Surface output pin. Nodes, like `Sin`  or [`If Equal`](https://developer.apple.com/documentation/ShaderGraph/Logic/If-Equal), aren’t tied to specific outputs and just perform an operation.

##### Update Material Values at Runtime

One of the major benefits of using Shader Graph is the ablility to change values on your custom materials while your app runs. Shader Graph creates , which are parameters you can set and read from Swift to change your material at runtime.

Some examples of how you can use promoted inputs for your materials are:

- If your material has emission that you want to turn on and off, you can create a Boolean input parameter and implement conditional logic based on its value.
- To smoothly interpolate between two colors, you can create a `Float` input parameter and use it to control how to interpolate between the two colors.

You can Control-click on a constant node and select Promote to turn it into a promoted input. You can also turn a promoted input back into a constant by Control-clicking it and selecting Demote in the contextual menu.

To change the value of an input parameter from Swift code, use [`setParameter(name:value:)`](https://developer.apple.com/documentation/RealityKit/ShaderGraphMaterial/setParameter(name:value:)), passing the name of the parameter and the new value. Notice that parameter names are case sensitive, so the `name` string must exactly match what you call the parameter in Shader Graph.

For more on building materials with Shader Graph, refer to the related [`Loading entities with ShaderGraph materials`](loading-entities-with-shadergraph-materials.md). For examples of Shader Graph use in a completed sample, see [`Diorama`](https://developer.apple.com/documentation/visionOS/diorama) and [`Happy Beam`](https://developer.apple.com/documentation/visionOS/happybeam).

## See Also

- [Importing and organizing content in your project](editor_projectbrowser.md)
  Manage content in your Reality Composer Pro project with the Project Browser.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/editor_shadergraph)*