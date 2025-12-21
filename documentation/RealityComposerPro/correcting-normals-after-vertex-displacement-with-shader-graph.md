# Correcting normals after vertex displacement with Shader Graph

**Framework**: Reality Composer Pro

Approximate new vertex normals for materials that displace a mesh’s vertices.

#### Overview

Vertex displacement shaders can create a myriad of dynamic effects, such as water, terrain, and undulating surfaces. However, displacing vertex positions without correcting the vertex normals can result in incorrect lighting, as shown in the examples below:

Assuming the vertices of your mesh have correct normals predisplacement, and the displacement is a continuous function of the vertex positions in model space, you can correct the normals of your vertex displacement shader by sampling the displacement of neighboring points along the surface of the mesh and approximating a new normal direction with the cross product.

For each vertex in the mesh, find two neighboring points on the surface of the mesh that are in orthogonal directions to one another. Approximate the new normal direction by displacing these points with the same function that displaces the original vertex, and then take the cross product between the new vectors pointing toward them. See [`Loading entities with ShaderGraph materials`](loading-entities-with-shadergraph-materials.md) to download a sample project containing this shader along with many others.

#### Create a Displacement Node Graph

Start by creating a node graph that takes a position input in `object` or `model` space and outputs a model position offset vector. See [`Creating a vertex displacement material with Shader Graph`](creating-a-vertex-displacement-material-with-shader-graph.md) for one such example, replicated below:

![A screenshot of the vertex displacement Shader Graph the aforementioned article describes. Three uniform input Float nodes, Amplitude, Frequency, and Rate, connect to their respective inputs on the Displacement node graph node: Amplitude, Frequency, and Rate. A Position node connects to the Position input of the Displacement node graph. The Model Position Offset output of the Displacement node graph connects to the Model Position Offset input of a Geometry Modifier node, whose output connects to the Custom Geometry Modifier input of the Outputs node. The output of a Preview Surface node connects to the Custom Surface input of the Outputs node.](https://docs-assets.developer.apple.com/published/30f7de982ad5145dd33f8c49af86bc02/correcting-normals-3%402x.png)

In this example, the Displacement node graph is as follows:

![A screenshot of the contents of the Displacement node graph described above. A uniform input Float node with the name Amplitude node connects to a Convert node, which connects to the Amplitude input of a Noise 3D node. A uniform input Vector3 (Float) node with the name Position connects to the top input of a Multiply node. A uniform input Float node with the name Frequency connects to the bottom input of the same Multiply node. The output of the Multiply node connects to the top input of an Add node. A uniform input Float node with the name Rate connects to the top input of another Multiply node. A Time node connects to the bottom input of that same Multiply node. The output of that Multiply node connects to the bottom input of the Add node. The output of the Add node connects to the Position input of the Noise 3D node. The Out output of the Noise 3D node connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/e509912b2147204bdae3ed4397d78e76/correcting-normals-4%402x.png)

#### Set Up the Offset and Normal Node Graph

Create the outline for a node graph that calculates the model position offset and the new normal direction in tandem:

1. Select the Displacement node graph and all of its inputs.
2. Control-click on one of the selected nodes and choose Compose Node Graph from the contextual menu.
3. Name the new [`NodeGraph`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/material/nodegraph) node “OffsetAndNormal”.
4. Add a new output of type `Vector3 (Float)` to the OffsetAndNormal node graph and name it “Normal”.
5. Connect the `Normal` output of the OffsetAndNormal node graph to the `Normal` input of the `Geometry Modifier` node.
6. Open the OffsetAndNormal node graph and optionally rename its inputs and outputs.

The main body of the shader is shown here:

![A screenshot of the Shader Graph described above. Three uniform input Float nodes, Amplitude, Frequency, and Rate, connect to their respective inputs on the OffsetAndNormal node graph node: Amplitude, Frequency, and Rate. The Model Position Offset and Normal outputs of the OffsetAndNormal node graph connect to their respective inputs on a Geometry Modifier node: Model Position Offset and Normal. The output of the Geometry Modifier node connects to the Custom Geometry Modifier input of the Outputs node. The output of a Preview Surface node connects to the Custom Surface input of the Outputs node.](https://docs-assets.developer.apple.com/published/13ea8241027eb546d11173c3c7df9f78/correcting-normals-5%402x.png)

See the interior of the OffsetAndNormal node graph below:

![A screenshot of the contents of the OffsetAndNormal node graph described above. Three uniform input Float nodes, Amplitude, Frequency, and Rate, connect to their respective inputs on the Displacement node graph node: Amplitude, Frequency, and Rate. A Position node connects to the Position input of the Displacement node graph. The Model Position Offset output of the Displacement node graph connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/37775ec921391954b14b1502db267668/correcting-normals-6%402x.png)

#### Set Up the Neighbors Node Graph

Prepare a new node graph to calculate two orthogonal neighboring positions at a given distance away from a given vertex position:

1. Inside the OffsetAndNormal node graph, add a new `NodeGraph` node and name it “Neighbors”.
2. Add a new input of type `Float` to the Neighbors node and name it “Distance”.
3. Add a new input of type `Vector3 (Float)` to the Neighbors node and name it “Position”.
4. Add a new output of type `Vector3 (Float)` to the Neighbors node graph and name it “Neighbor1Position”.
5. Add a new output of type `Vector3 (Float)` to the Neighbors node graph and name it “Neighbor2Position”.
6. Connect the Position node to the `Position` input of the Neighbors node.
7. Set the `Distance` input value of the Neighbors node to a small value, such as 0.01.

The interior of the OffsetAndNormal node graph is as follows:

![A screenshot of the contents of the OffsetAndNormal node graph described above. Three uniform input Float nodes, Amplitude, Frequency, and Rate, connect to their respective inputs on the Displacement node graph node: Amplitude, Frequency, and Rate. A Position node connects to the Position input of the Displacement node graph, as well as the Position input of a Neighbors node graph. The Model Position Offset output of the Displacement node graph connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/86588ae02ff669ce9993d45f9d659e18/correcting-normals-7%402x.png)

> **Note**: The ideal value for the distance parameter depends on the size of your mesh in model space. Adjust the distance input value manually to get the desired results.

#### Find Neighboring Positions Along the Surface

Calculate two orthogonal neighbor positions inside the Neighbors node graph:

1. Add a [`Normal`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/geometric/normal) node and set its `Space` to `object`.
2. Calculate a vector orthogonal to the normal (tangent to the surface) by taking the cross product of the `Normal` node with an arbitrary unit vector, such as (1, 0, 0), using a [`Cross Product`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/cross-product) node. Name it “Tangent”.
3. Compute the cross product of the Tangent `Cross Product` node with the Normal node and name it “Bitangent”. This produces a second vector orthogonal to the normal, but also tangent to the surface of the mesh.
4. Normalize the output of both the Tangent and the Bitangent `Cross Product` nodes with [`Normalize`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/normalize) nodes.
5. Multiply the output of both the `Normalize` nodes by the `Distance` input with [`Multiply`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/multiply) nodes.
6. Compute the two neighbor positions by adding the `Position` input to the result of both the `Multiply` nodes with [`Add`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/add) nodes.
7. Connect the output of the `Add` nodes to the `Neighbor1Position` and `Neighbor2Position` outputs.

The interior of the Neighbors node graph is as follows:

![A screenshot of the Shader Graph described above. A Normal node connects to the top input of a Cross Product node with the name Tangent. The bottom input of the Tangent Cross Product node is the vector (1.00, 0.00, 0.00). The output of the Tangent Cross Product node connects to the top input of a Cross Product node with the name Bitangent. The Normal node connects to the bottom input of the Bitangent Cross Product node. The outputs of the Tangent and Bitangent Cross Product nodes connect to Normalize nodes, which connect to the top input of Multiply nodes, whose bottom input comes from a uniform input Float node with the name Distance. The outputs of the Multiply nodes connect to the bottom inputs of two Add nodes, whose top input comes from a uniform input Vector3 (Float) node with the name Position. The output of the Add nodes connect to the Neighbor1Position and Neighbor2Position inputs of the Outputs node.](https://docs-assets.developer.apple.com/published/b39bbf5cfdd96cdb2c10ef4257040e72/correcting-normals-8%402x.png)

While this node graph outputs orthogonal neighboring positions under most circumstances, it fails when the normal vector is similar or equal to the arbitrary unit vector you take the cross product with to get the tangent. One approach to remedying this issue is to compute the similarity between the normal and the arbitrary unit vector with a dot product, and then linearly interpolate toward a different arbitrary unit vector by the similarity value before computing the first tangent, as shown here:

![A screenshot of the Shader Graph described above. A Normal node connects to the bottom input of a Dot Product node with the name Similarity. The top input of the Dot Product node is a Vector3 (Float) node with the name ArbitraryVector1 and a value of (1.00, 0.00, 0.00). The output of the Similarity Dot Product node connects to an Abs node, which connects to the Mix input of a Mix node. ArbitraryVector1 connects to the Background input of the Mix node, while a Vector3 (Float) node with the name ArbitraryVector2 and a value of (0.00, 1.00, 0.00) connects to the Foreground input. The Mix node connects to the top input of a Cross Product node with the name Tangent. The bottom input of the Tangent Cross Product node is the vector (1.00, 0.00, 0.00). The output of the Tangent Cross Product node connects to the top input of a Cross Product node with the name Bitangent. The Normal node connects to the bottom input of the Bitangent Cross Product node. The outputs of the Tangent and Bitangent Cross Product nodes connect to Normalize nodes, which connect to the top input of Multiply nodes, whose bottom input comes from a uniform input Float node with the name Distance. The outputs of the Multiply nodes connect to the bottom inputs of two Add nodes, whose top input comes from a uniform input Vector3 (Float) node with the name Position. The output of the Add nodes connect to the Neighbor1Position and Neighbor2Position inputs of the Outputs node.](https://docs-assets.developer.apple.com/published/39beae7a289f89337339b99d5ee538db/correcting-normals-9%402x.png)

#### Sample the Displacement at the Neighboring Positions

Calculate the model position offset at both of the neighboring positions by making instances of your Displacement node graph:

1. Create two instances of your Displacement node graph (in the Inspector, Control-click > Create Instance), naming one “DisplacementNeighbor1” and the other “DisplacementNeighbor2”.
2. Connect the `Neighbor1Position` output of the Neighbors node graph to the `Position` input of the DisplacementNeighbor1 node graph instance.
3. Connect the `Neighbor2Position` output of the Neighbors node graph to the `Position` input of the DisplacementNeighbor2 node graph instance.

Perform these steps inside the OffsetAndNormal node graph, connecting the Amplitude, Rate, and Scale input nodes to the corresponding inputs of each Displacement node, as shown in the image below:

![A screenshot of the contents of the OffsetAndNormal node graph described above. Three uniform input Float nodes, Amplitude, Frequency, and Rate, connect to their respective inputs on the Displacement node graph node and its two instances: DisplacementNeighbor1 and DisplacementNeighbor2. A Position node connects to the Position input of the Displacement node graph, as well as the Position input of a Neighbors node graph. The Neighbor1 Position output of the Neighbors node connects to the Position input of the DisplacementNeighbor1 node graph, while the Neighbor2 Position output connects to the Position input of the DisplacementNeighbor2 node graph. The Model Position Offset output of the Displacement node graph connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/a11f31e3a370673438e133acc4c04970/correcting-normals-10%402x.png)

> **Note**: By creating instances of your Displacement node graph, any changes you make to the original Displacement node graph automatically update all instances to match.

#### Compute the New Normal Direction

Calculate the new normal direction by taking the cross product between the directions from the displaced vertex position to the displaced neighbor positions:

1. For each of the three displacement nodes, get the displaced position by adding the same value connected to the `Position` input of the node to the `Model Position Offset` output of the node with an `Add` node.
2. Calculate the vectors pointing from the displaced vertex position to the displaced neighbor positions by subtracting the original displaced vertex position from the displaced neighbor positions with [`Subtract`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/subtract) nodes.
3. Take the cross product between the vectors with a `Cross Product` node to get the new normal direction. Name it “Normal”.
4. Normalize the normal direction with a `Normalize` node.
5. Connect the normalized normal direction to the `Normal` output.

The resulting node graph is as follows:

![A screenshot of the contents of the OffsetAndNormal node graph described above. Three uniform input Float nodes, Amplitude, Frequency, and Rate, connect to their respective inputs on the Displacement node graph node and its two instances: DisplacementNeighbor1 and DisplacementNeighbor2. A Position node connects to the Position input of the Displacement node graph, as well as the Position input of a Neighbors node graph. The Neighbor1Position output of the Neighbors node connects to the Position input of the DisplacementNeighbor1 node graph, while the Neighbor2Position output connects to the Position input of the DisplacementNeighbor2 node graph. The value connecting to the Position input of each of the three Displacement node graphs connects to the top input of three Add nodes, whose bottom input comes from the Model Position Offset output of their respective Displacement node graph. The output of the two Add nodes, which connect to the DisplacementNeighbor node graphs, connect to the top input of two Subtract nodes, whose bottom input comes from the output of the Add node that connects to the original Displacement node graph. The output of the Subtract nodes connect to the top and bottom input of a Cross Product node, which connects to a Normalize node, which in turn connects to the Normal input of the Outputs node. The Model Position Offset output of the Displacement node graph connects to the Model Position Offset input of the Outputs node.](https://docs-assets.developer.apple.com/published/fb8c1b4a3c03edccccb84f6116b8d119/correcting-normals-11%402x.png)

The following videos show the result of correcting the normals for a shader displacing the vertices of a plane mesh:

## See Also

- [Designing materials with Shader Graph](editor_shadergraph.md)
  Create realistic materials with Shader Graph’s node editor in Reality Composer Pro.
- [Loading entities with ShaderGraph materials](loading-entities-with-shadergraph-materials.md)
  Bring entities that contain materials created with Reality Composer Pro for use in your visionOS app.
- [Creating a Fresnel outline effect with Shader Graph](creating-a-fresnel-outline-effect-with-shader-graph.md)
  Highlight a model by adding an outline effect.
- [Creating a vertex displacement material with Shader Graph](creating-a-vertex-displacement-material-with-shader-graph.md)
  Animate the vertices of a mesh over time with 3D Perlin noise by creating a Shader Graph material.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/correcting-normals-after-vertex-displacement-with-shader-graph)*