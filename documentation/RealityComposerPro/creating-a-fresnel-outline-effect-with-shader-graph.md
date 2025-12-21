# Creating a Fresnel outline effect with Shader Graph

**Framework**: Reality Composer Pro

Highlight a model by adding an outline effect.

#### Overview

Emphasizing the edges of a model with an outline is an effective way to highlight and call attention to it, especially when it’s the target of a person’s gaze or interaction.

One way to add an outline to a model is to approximate the Fresnel effect, wherein the angle between the view direction and the surface normal of a model affects the shading around its edges. Specifically, you can highlight the edges of a model by taking the dot product between the view direction and the surface normal direction and applying an emissive color to the areas where the dot product is close to zero (that is, the vectors are perpendicular). See [`Loading entities with ShaderGraph materials`](loading-entities-with-shadergraph-materials.md) to download a sample project containing this shader along with many others.

> **Note**: Creating an outline with the Fresnel effect works best with models that have smooth, curved surfaces, and doesn’t perform well with flat models such as planes and cubes.

#### Prepare the Fresnel Node Graph

Set up a reusable [`NodeGraph`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/material/nodegraph) to house your Fresnel logic by following these steps:

1. Create a custom Shader Graph material (Insert > Material > Shader Graph).
2. Open the Shader Graph Editor by clicking the Shader Graph button.
3. Add a `NodeGraph` node by clicking the New Node button or pressing the tab key and searching for “Node Graph”.
4. Name the `NodeGraph` node “Fresnel”.
5. Add a new input to the Fresnel node graph by selecting it and clicking the New Input button in the Inspector.
6. Name the new input “Falloff” and give it a type of `Float`.
7. Add a new output to the Fresnel node graph by selecting it and clicking the New Output button in the Inspector.
8. Name the new output “Out” and give it a type of `Float`.

The following image shows the main body of the Shader Graph material:

![A screenshot of the Shader Graph described above. On the left is a NodeGraph node with the name Fresnel, followed by a Preview Surface node whose Out output connects to the Custom Surface input of the Outputs node on the right.](https://docs-assets.developer.apple.com/published/3e515877419992c4d0c38a5c3efd5af4/fresnel-1%402x.png)

#### Compose the Fresnel Logic

Approximate the Fresnel effect by taking the dot product between the view direction and the normal direction in the Fresnel node graph:

1. Add a [`View Direction`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/realitykit/view-direction-(realitykit)#Parameter-description) node and set its Space to `world`.
2. Add a [`Normal`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/geometric/normal) node and set its Space to `world`.
3. Take the dot product between the `View Direction` and `Normal` with a [`Dot Product`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/dot-product) node.
4. Connect the output of the `Dot Product` node to the input of a [`Clamp`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/clamp) node and set its `high` value to `1.0`.
5. Connect the output of the `Clamp` node to the input of a [`One Minus`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/one-minus-(realitykit)) node.
6. Connect the output of the `One Minus` node to the top input of a [`Power`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/power) node.
7. Connect the `Falloff` input to the bottom input of the `Power` node.
8. Connect the output of the `Power` node to the `Out` output.

The interior of the Fresnel node graph is as follows:

![A screenshot of the Shader Graph described above. The output of a View Direction node connects to the top input of a Dot Product node. The output of a Normal node connects to the bottom input of the same Dot Product node. The output of the Dot Product node connects to the In input of a Clamp node, whose output connects to a One Minus node, which in turn connects to the top input of a Power node. A uniform input Float node with the name Falloff connects to the bottom input of the same power node. The output of the Power node connects to the Out input of Outputs.](https://docs-assets.developer.apple.com/published/db0db000449a8ab0d30f3e9b2f14a54a/fresnel-2%402x.png)

The following images show the result of each stage of the Fresnel node graph if it were fully connected:

In this case, the view direction and the normal direction are parallel at the center of the sphere, and become more perpendicular to each other toward the edges of the sphere, meaning the dot product ranges from a value of 1 at the center to a value of 0 near the edges. You can flip this by subtracting 1 from the dot product, and increase the rate of falloff by taking that value to a power.

#### Create an Outline Effect with the Fresnel Node

One way to create an outline effect with the `Fresnel` node is by employing its output to apply an emissive color around the edges of a model. In the main graph of your shader:

1. Add a new uniform input of type `Float` and name it “OutlineFalloff”.
2. Connect the OutlineFalloff node to the `Falloff` input of the Fresnel node graph.
3. Add a new uniform input of type `Color3 (Float)` and name it “OutlineColor”.
4. Connect the OutlineColor node to the top input of a [`Multiply`](https://developer.apple.comhttps://developer.apple.com/documentation/shadergraph/math/multiply) node.
5. Connect the `Out` output of the Fresnel node graph to the bottom input of the `Multiply` node.
6. Connect the output of the `Multiply` node to the `Emissive Color` input of the `Preview Surface` node.

The resulting graph is as follows:

![A screenshot of the Shader Graph described above. The output of a uniform input Color3 (Float) node with the name OutlineColor connects to the top input of a Multiply node. The Out output of the Fresnel node graph node connects to the bottom input of the same Multiply node. The output of the Multiply node connects to the Emissive Color input of a Preview Surface node, whose Out output connects to the Custom Surface input of the Outputs node.](https://docs-assets.developer.apple.com/published/4be1e29221f0ec7b53fc119bc4f307c0/fresnel-6%402x.png)

You can adjust the `OutlineColor` input to change the color of the outline, and you can adjust the `OutlineFalloff` to control the rate of falloff for the Fresnel effect, as shown in the three examples below:

## See Also

- [Designing materials with Shader Graph](editor_shadergraph.md)
  Create realistic materials with Shader Graph’s node editor in Reality Composer Pro.
- [Loading entities with ShaderGraph materials](loading-entities-with-shadergraph-materials.md)
  Bring entities that contain materials created with Reality Composer Pro for use in your visionOS app.
- [Creating a vertex displacement material with Shader Graph](creating-a-vertex-displacement-material-with-shader-graph.md)
  Animate the vertices of a mesh over time with 3D Perlin noise by creating a Shader Graph material.
- [Correcting normals after vertex displacement with Shader Graph](correcting-normals-after-vertex-displacement-with-shader-graph.md)
  Approximate new vertex normals for materials that displace a mesh’s vertices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitycomposerpro/creating-a-fresnel-outline-effect-with-shader-graph)*