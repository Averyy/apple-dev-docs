# Camera Index Switch (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Render different results for each eye in a stereoscopic render.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Camera Index Switch (integer)**:

| Input | Type |
| --- | --- |
| `Mono` | Int32 |
| `Left` | Int32 |
| `Right` | Int32 |

| Output | Type |
| --- | --- |
| `Out` | Int32 |

**Camera Index Switch (float)**:

| Input | Type |
| --- | --- |
| `Mono` | Float |
| `Left` | Float |
| `Right` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Camera Index Switch (vector4h)**:

| Input | Type |
| --- | --- |
| `Mono` | Vector4h |
| `Left` | Vector4h |
| `Right` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Camera Index Switch (vector2f)**:

| Input | Type |
| --- | --- |
| `Mono` | Vector2f |
| `Left` | Vector2f |
| `Right` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Camera Index Switch (vector4f)**:

| Input | Type |
| --- | --- |
| `Mono` | Vector4f |
| `Left` | Vector4f |
| `Right` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Camera Index Switch (color3f)**:

| Input | Type |
| --- | --- |
| `Mono` | Color3 |
| `Left` | Color3 |
| `Right` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Camera Index Switch (vector3h)**:

| Input | Type |
| --- | --- |
| `Mono` | Vector3h |
| `Left` | Vector3h |
| `Right` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Camera Index Switch (half)**:

| Input | Type |
| --- | --- |
| `Mono` | Half |
| `Left` | Half |
| `Right` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Camera Index Switch (vector3f)**:

| Input | Type |
| --- | --- |
| `Mono` | Vector3f |
| `Left` | Vector3f |
| `Right` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Camera Index Switch (color4f)**:

| Input | Type |
| --- | --- |
| `Mono` | Color4 |
| `Left` | Color4 |
| `Right` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Camera Index Switch (vector2h)**:

| Input | Type |
| --- | --- |
| `Mono` | Vector2h |
| `Left` | Vector2h |
| `Right` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

## Parameter descriptions

- **`Mono`**: The value to return if using a single renderer.
- **`Left`**: The value to return if seeing the texture through the left eye of a stereoscopic render.
- **`Right`**: The value to return if seeing the texture through the right eye of a stereoscopic render.

## Discussion

Use the `Camera Index Switch` node to render stereoscopic images. On most devices, this node returns its `Mono` input parameter. On Apple Vision Pro, this node outputs either `Left` or `Right`, depending on which eye the texture renders through.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/camera-index-switch-(realitykit))*