# Image 2D Read (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Direct texture read.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Image 2D Read (vector4f)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Vector4f |
| `X` | Int32 |
| `Y` | Int32 |
| `Lod` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Image 2D Read (color4)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Color4 |
| `X` | Int32 |
| `Y` | Int32 |
| `Lod` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

## Parameter description

- **`File`**: The image file to use for the texture.
- **`Default`**: The default value to use if the ​`File`​ parameter fails to resolve.
- **`X`**: The X position of the pixel that the node reads.
- **Y**: The Y position of the pixel that the node reads.
- **`Lod`**: The specific LOD level that the node samples from.

## Discussion

The `Image 2D Read` node performs a straight read from a 2D texture without a sampler. Use this node if you have a texture that’s just data.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/image-2d-read-(realitykit))*