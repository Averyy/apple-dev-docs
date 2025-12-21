# Creating a vertex displacement material with Shader Graph

**Framework**: Reality Composer Pro

Animate the vertices of a mesh over time with 3D Perlin noise by creating a Shader Graph material.

#### Overview

Moving the vertices of a mesh with a shader is a valuable technique to have in your shader toolbox. Using this technique, you can procedurally distort the shape of a mesh and animate it over time, all without having to author explicit frame-by-frame animations. Moving the vertices displaces them from their original positions, so this effect is known as , as shown in the example below:

To create a shader graph material that displaces the vertices of a mesh over time, apply a positional offset to each vertex with a [`Geometry Modifier`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/realitykit/geometry-modifier-(realitykit)) node and a [`Noise 3D`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/3d-procedural/noise-3d) node. You can control the amplitude, scale, and rate of displacement with shader uniforms. See [`Loading entities with ShaderGraph materials`](loading-entities-with-shadergraph-materials.md) to download a sample project containing this shader along with many others.

#### Prepare a Displacement Node Graph

House the vertex displacement logic in a reusable [`NodeGraph`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/material/nodegraph) by following these steps:

1. Create a custom Shader Graph material (Insert > Material > Shader Graph).
2. Open the Shader Graph Editor by clicking the Shader Graph button.
3. Add a `NodeGraph` node by clicking the New Node button or pressing the tab key and searching for “Node Graph”.
4. Name the `NodeGraph` node “Displacement”.
5. Add a new input to the Displacement node graph by selecting it and clicking the New Input button in the Inspector.
6. Name the new input “Position” and give it a type of `Vector3 (Float)`.
7. Add a new output to the Displacement node graph by selecting it and clicking the New Output button in the Inspector.
8. Name the new output “ModelPositionOffset” and give it a type of `Vector3 (Float)`.

The following images show the Displacement node graph and its Inspector:

#### Set Up the Geometry Modifier

Add a [`Geometry Modifier`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/realitykit/geometry-modifier-(realitykit)) node to offset the vertex positions by the output of the Displacement node graph:

1. Add a [`Position`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/geometric/position) node.
2. Connect the output of the `Position` node to the `Position` input of the Displacement node graph.
3. Add a `Geometry Modifier` node.
4. Connect the `Model Position Offset` output of the Displacement node graph to the `Model Position Offset` input of a `Geometry Modifier` node.
5. Connect the `Out` output of the `Geometry Modifier` node to the `Custom Geometry Modifier` input of the `Outputs` node.

The main shader body is as follows:

![A Position node connects to the Position input of the Displacement node graph node, whose Model Position Offset output connects to the Model Position Offset input of a Geometry Modifier node. The output of the Geometry Modifier node connects to the Custom Geometry Modifier input of the Outputs node. The output of a Preview Surface node connects to the Custom Surface input of the Outputs node.](https://docs-assets.developer.apple.com/published/34d3d3d3aecf118ac3db51e71fd48a4a/vertex-displacement-3%402x.png)

In this example, the `Space` of the `Position` node is set to `object` so that the displacement effect remains consistent regardless of the model’s position, orientation, or scale in world space, but you can use `world` instead if you want your displacement effect to depend on these factors.

#### Displace the Vertices

One way to displace the vertices in a mesh is by utilizing output of a [`Noise 3D`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/3d-procedural/noise-3d) node:

1. Open the Displacement node graph by double-clicking it or selecting it in the Navigator.
2. Add a `Noise 3D` node.
3. Connect the output of the `Position` node to the `Position` input of the `Noise 3D` node.
4. Connect the `Out` output of the `Noise 3D` node to the `Model Position Offset` parameter of Outputs.

The following image shows the interior of the Displacement node graph:

![A screenshot of the interior of the Displacement node graph described above. A uniform input Vector3 (Float) node connects to the Position input of a Noise 3D node, whose output connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/68b0ae678a22a8640132734601bcf10a/vertex-displacement-4%402x.png)

You can see the result of the shader in the Shader Graph Preview window, as shown below:

![A screenshot of the Shader Graph preview window rendering a cube mesh. This technique displaces the mesh's vertices by noise so its shape appears distorted.](https://docs-assets.developer.apple.com/published/f70da6e204f45337ae96744128656f75/vertex-displacement-4-5%402x.png)

In the example shown here, the `Noise 3D` node generates vertex offsets with Perlin noise, which distorts the shape of the mesh in a smooth yet random manner. To distort the shape of the surface differently, you can experiment with other noise functions, such as [`Fractal Noise 3D`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/3d-procedural/fractal-noise-3d) or [`Worley Noise 3D`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/3d-procedural/worley-noise-3d), or you can displace the vertices with your own custom logic.

#### Control the Amplitude of Displacement

Control the degree to which the shader offsets the vertices by adjusting the `Amplitude` parameter of the `Noise 3D` node:

1. Add a new input to the Displacement node graph of type `Float` and name it “Amplitude”.
2. Add a [`Convert`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/data/convert) node and set its type to `Convert (float vector3f)`.
3. Connect the output of the `Amplitude` node to the input of the `Convert` node.
4. Connect the output of the `Convert` node to the `Amplitude` input of the `Noise 3D` node.

The following image shows the interior of the Displacement node graph:

![A screenshot of the interior of the Displacement node graph described above. A uniform input Float node with the name Amplitude connects to a Convert node, which in turn connects to the Amplitude input of a Noise 3D node. A uniform input Vector3 (Float) node connects to tht Position input of the same Noise 3D node. The output of the Noise 3D node connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/10d4e868a4d997e25d8370098b3b6643/vertex-displacement-5%402x.png)

You can increase the value of the `Amplitude` node to increase the amount the shader displaces the vertices by, as shown in the three examples below:

#### Control the Scale of Displacement

Control the scale at which the shader offsets the vertices by multiplying the position by a constant factor before sampling the `Noise 3D` node:

1. Add a new input to the Displacement node graph of type `Float` and name it “Scale”.
2. Multiply the output of the `Position` node by the output of the `Scale` node with a [`Multiply`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/multiply?changes=lat_3___7__3) node.
3. Connect the output of the `Multiply` node to the `Position` input of the `Noise 3D` node.

The following image shows the interior of the Displacement node graph:

![A screenshot of the interior of the Displacement node graph described above. A uniform input Float node with the name Amplitude node connects to a Convert node, which connects to the Amplitude input of a Noise 3D node. A uniform input Vector3 (Float) node with the name Position connects to the top input of a Multiply node. A uniform input Float node with the name Scale connects to the bottom input of the same Multiply node. The output of the Multiply node connects to the Position input of the Noise 3D node. The Out output of the Noise 3D node connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/0e5f0d6985cfa9173ed27ddb7a3fc318/vertex-displacement-6%402x.png)

You can increase the value of the `Scale` node to increase the scale at which the shader displaces the vertices, as shown in the three examples below:

#### Displace the Vertices Over Time

Animate the vertices by moving the position over time, following these steps:

1. Add a [`Time`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/application/time-(float)) node.
2. Add the output of the `Multiply` node, multiplying the `Position` by the `Scale` to the `Time` with an [`Add`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/add) node.
3. Connect the output of the `Add` node to the `Position` input of the `Noise 3D` node.

The following image shows the interior of the Displacement node graph:

![A screenshot of the interior of the Displacement node graph described above. A uniform input Float node with the name Amplitude node connects to a Convert node, which connects to the Amplitude input of a Noise 3D node. A uniform input Vector3 (Float) node with the name Position connects to the top input of a Multiply node. A uniform input Float node with the name Scale connects to the bottom input of the same Multiply node. The output of the Multiply node connects to the top input of an Add node. A Time node connects to the bottom input of the same Add node. The output of the Add node connects to the Position input of the Noise 3D node. The Out output of the Noise 3D node connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/b9824fbb629f5aad4b80def508c8ac51/vertex-displacement-7%402x.png)

The vertices of the mesh move over time, as shown below:

#### Control the Rate of Displacement

Control the rate at which the shader displaces the vertices over time by multiplying the time by a constant factor:

1. Add a new input of type `Float` and name it “Rate”.
2. Multiply the output of the `Time` node by the output of the `Rate` node with a `Multiply` node.
3. Connect the output of the `Multiply` node to the bottom input of the `Add` node.

The following image shows the interior of the Displacement node graph:

![A screenshot of the interior of the Displacement node graph described above. A uniform input Float node with the name Amplitude node connects to a Convert node, which connects to the Amplitude input of a Noise 3D node. A uniform input Vector3 (Float) node with the name Position connects to the top input of a Multiply node. A uniform input Float node with the name Scale connects to the bottom input of the same Multiply node. The output of the Multiply node connects to the top input of an Add node. A uniform input Float node with the name Rate connects to the top input of another Multiply node. A Time node connects to the bottom input of that same Multiply node. The output of that Multiply node connects to the bottom input of the Add node. The output of the Add node connects to the Position input of the Noise 3D node. The Out output of the Noise 3D node connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/e509912b2147204bdae3ed4397d78e76/vertex-displacement-8%402x.png)

You can adjust the `Rate` value to control the speed of the vertex displacement animation, as shown in the three examples below:

#### Create Uniform Inputs

Back in the main graph of your shader, create uniform inputs for each of the input properties of the `Displacement` node — `Amplitude`, `Scale`, and `Rate` — so that you can adjust these properties at the material level:

Creating uniform inputs also allows you to adjust the shader properties in code with the [`setParameter(name:value:)`](https://developer.apple.comhttps://developer.apple.com/documentation/realitykit/shadergraphmaterial/setparameter(name:value:)) method, for example.

#### Correct the Normal Directions

When displacing the vertices of a mesh, you may notice that the way the mesh reacts to lighting no longer appears correct. This is typically the result of displacing the vertex positions without also modifying the vertex normals to match. For an obvious example, apply the material to the plane mesh in the preview window and observe how flat it looks despite its vertices moving:

See [`Correcting normals after vertex displacement with Shader Graph`](correcting-normals-after-vertex-displacement-with-shader-graph.md) for information on how you can approximate and correct the normal directions, as shown in the following video:

## See Also

- [Designing materials with Shader Graph](editor_shadergraph.md)
  Create realistic materials with Shader Graph’s node editor in Reality Composer Pro.
- [Loading entities with ShaderGraph materials](loading-entities-with-shadergraph-materials.md)
  Bring entities that contain materials created with Reality Composer Pro for use in your visionOS app.
- [Creating a Fresnel outline effect with Shader Graph](creating-a-fresnel-outline-effect-with-shader-graph.md)
  Highlight a model by adding an outline effect.
- [Correcting normals after vertex displacement with Shader Graph](correcting-normals-after-vertex-displacement-with-shader-graph.md)
  Approximate new vertex normals for materials that displace a mesh’s vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-a-vertex-displacement-material-with-shader-graph)*