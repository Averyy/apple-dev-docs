# Geometry Modifier (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A function that manipulates the location of a model’s vertices, run once per vertex.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

| Input | Type |
| --- | --- |
| `Model Position Offset` | Vector3f |
| `Color` | Color4 |
| `Normal` | Vector3f |
| `Bitangent` | Vector3f |
| `Uv0` | Vector2f |
| `Uv1` | Vector2f |
| `Uv2` | Vector4f |
| `Uv3` | Vector4f |
| `Uv4` | Vector4f |
| `Uv5` | Vector4f |
| `Uv6` | Vector4f |
| `Uv7` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Token |

## Parameter descriptions

- **`Model Position Offset`**: The offset to each vertices model position.
- **`Color`**: The color of each vertex.
- **`Normal`**: The normal vector for each vertex.
- **`Bitangent`**: The bitangent vector for each vertex.
- **`Uv0`**: A set of texture coordinates for each vertex.
- **`Uv1`**: A set of texture coordinates for each vertex.
- **`User Attribute`**: A user-defined attribute to apply to each vertex of the object.
- **`User Attribute Half4 0`**: A user-defined attribute the node attaches to each vertex of the object.
- **`User Attribute Half4 1`**: A user-defined attribute the node attaches to each vertex of the object.
- **`User Attribute Half4 2`**: A user-defined attribute the node attaches to each vertex of the object.
- **`User Attribute Half4 3`**: A user-defined attribute the node attaches to each vertex of the object.
- **`User Attribute Half2 0`**: A user-defined attribute the node attaches to each vertex of the object.
- **`User Attribute Half2 1`**: A user-defined attribute the node attaches to each vertex of the object.

## Discussion

The Geometry Modifier node can be used to cause a material to affect the geometry of any object to which it’s applied, in addition to the objects texture. Connect the output of the Geometry modifier node to the `Custom Geometry Modifier` output of your material. Below is an example of a simple node graph that uses the Geometry Modifier node to alter the *Y* model positions of vertices.

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/GeometryModifierGraph.png)

Use the Noise 2D node to procedurally generate an amount to offset the *Y* position of each vertex. You can also use the noise to add shadows to the texture in order to show the change in model position more clearly. Below, the resulting material applies to a plane.

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/GeometryModifierMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/GeometryModifierMaterial2.png)

## See Also

### Nodes
- [Unlit Surface (RealityKit)](./unlit-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Unlit material.
- [PBR Surface (RealityKit)](./pbr-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Physically Based Rendering material.
- [Hair Surface (RealityKit)](./hair-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Hair material.
- [Occlusion Surface (RealityKit)](./occlusion-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Occlusion material that does not receive dynamic lighting.
- [Shadow Receiving Occlusion Surface (RealityKit)](./shadow-receiving-occlusion-surface-%28realitykit%29.md)
  A surface shader that defines properties for a RealityKit Occlusion material that receives dynamic lighting.
- [View Direction (RealityKit)](./view-direction-%28realitykit%29.md)
  A vector from a position in the scene to the view reference point.
- [Camera Position (RealityKit)](./camera-position-%28realitykit%29.md)
  The position of the camera in the scene.
- [Geometry Modifier Model To World (RealityKit)](./geometry-modifier-model-to-world-%28realitykit%29.md)
  The model-to-world transformation Matrix4x4 (Float).
- [Geometry Modifier World To Model (RealityKit)](./geometry-modifier-world-to-model-%28realitykit%29.md)
  The world-to-model transformation Matrix4x4 (Float).
- [Geometry Modifier Normal To World (RealityKit)](./geometry-modifier-normal-to-world-%28realitykit%29.md)
  The normal-to-world transformation Matrix3x3 (Float).
- [Geometry Modifier Model To View (RealityKit)](./geometry-modifier-model-to-view-%28realitykit%29.md)
  The model-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier View To Projection (RealityKit)](./geometry-modifier-view-to-projection-%28realitykit%29.md)
  The view-to-projection transformation Matrix4x4 (Float).
- [Geometry Modifier Projection To View (RealityKit)](./geometry-modifier-projection-to-view-%28realitykit%29.md)
  The projection-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier Vertex ID (RealityKit)](./geometry-modifier-vertex-id-%28realitykit%29.md)
  The integer index of the vertex.
- [Surface Model To World (RealityKit)](./surface-model-to-world-%28realitykit%29.md)
  The model-to-world transformation Matrix4x4 (Float).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/geometry-modifier-(realitykit))*