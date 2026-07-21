# Geometry Modifier (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

A function that manipulates the location of a model’s vertices, run once per vertex.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

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

### Discussion

The Geometry Modifier node can be used to cause a material to affect the geometry of any object to which it’s applied, in addition to the objects texture. Connect the output of the Geometry modifier node to the `Custom Geometry Modifier` output of your material. Below is an example of a simple node graph that uses the Geometry Modifier node to alter the *Y* model positions of vertices.

![None](https://docs-assets.developer.apple.com/published/00136a30e1f473e17c13809511e24380/GeometryModifierGraph.png)

Use the Noise 2D node to procedurally generate an amount to offset the *Y* position of each vertex. You can also use the noise to add shadows to the texture in order to show the change in model position more clearly. Below, the resulting material applies to a plane.

## See Also

- [Unlit Surface (RealityKit)](realitykit/unlit-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Unlit material.
- [PBR Surface (RealityKit)](realitykit/pbr-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Physically Based Rendering material.
- [Hair Surface (RealityKit)](realitykit/hair-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Hair material.
- [Occlusion Surface (RealityKit)](realitykit/occlusion-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Occlusion material that does not receive dynamic lighting.
- [Shadow Receiving Occlusion Surface (RealityKit)](realitykit/shadow-receiving-occlusion-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Occlusion material that receives dynamic lighting.
- [View Direction (RealityKit)](realitykit/view-direction-(realitykit).md)
  A vector from a position in the scene to the view reference point.
- [Camera Position (RealityKit)](realitykit/camera-position-(realitykit).md)
  The position of the camera in the scene.
- [Geometry Modifier Model To World (RealityKit)](realitykit/geometry-modifier-model-to-world-(realitykit).md)
  The model-to-world transformation Matrix4x4 (Float).
- [Geometry Modifier World To Model (RealityKit)](realitykit/geometry-modifier-world-to-model-(realitykit).md)
  The world-to-model transformation Matrix4x4 (Float).
- [Geometry Modifier Normal To World (RealityKit)](realitykit/geometry-modifier-normal-to-world-(realitykit).md)
  The normal-to-world transformation Matrix3x3 (Float).
- [Geometry Modifier Model To View (RealityKit)](realitykit/geometry-modifier-model-to-view-(realitykit).md)
  The model-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier View To Projection (RealityKit)](realitykit/geometry-modifier-view-to-projection-(realitykit).md)
  The view-to-projection transformation Matrix4x4 (Float).
- [Geometry Modifier Projection To View (RealityKit)](realitykit/geometry-modifier-projection-to-view-(realitykit).md)
  The projection-to-view transformation Matrix4x4 (Float).
- [Geometry Modifier Vertex ID (RealityKit)](realitykit/geometry-modifier-vertex-id-(realitykit).md)
  The integer index of the vertex.
- [Surface Model To World (RealityKit)](realitykit/surface-model-to-world-(realitykit).md)
  The model-to-world transformation Matrix4x4 (Float).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/geometry-modifier-(realitykit))*