# Image 3D (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A texture with RealityKit properties.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

#### Overview

Adjustable level of detail

#### Parameter Types

**Image 3D (vector4f)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `U Wrap Mode` | String |
| `V Wrap Mode` | String |
| `W Wrap Mode` | String |
| `Border Color` | String |
| `Mag Filter` | String |
| `Min Filter` | String |
| `Mip Filter` | String |
| `Max Anisotropy` | Int32 |
| `Max Lod Clamp` | Float |
| `Min Lod Clamp` | Float |
| `Default` | Vector4f |
| `Texture Coordinates` | Vector3f |
| `Bias` | Float |
| `Dynamic Min Lod Clamp` | Float |
| `Offset` | Integer3 |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Image 3D (color4)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `U Wrap Mode` | String |
| `V Wrap Mode` | String |
| `W Wrap Mode` | String |
| `Border Color` | String |
| `Mag Filter` | String |
| `Min Filter` | String |
| `Mip Filter` | String |
| `Max Anisotropy` | Int32 |
| `Max Lod Clamp` | Float |
| `Min Lod Clamp` | Float |
| `Default` | Color4 |
| `Texture Coordinates` | Vector3f |
| `Bias` | Float |
| `Dynamic Min Lod Clamp` | Float |
| `Offset` | Integer3 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Image 3D (color3)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `U Wrap Mode` | String |
| `V Wrap Mode` | String |
| `W Wrap Mode` | String |
| `Border Color` | String |
| `Mag Filter` | String |
| `Min Filter` | String |
| `Mip Filter` | String |
| `Max Anisotropy` | Int32 |
| `Max Lod Clamp` | Float |
| `Min Lod Clamp` | Float |
| `Default` | Color3 |
| `Texture Coordinates` | Vector3f |
| `Bias` | Float |
| `Dynamic Min Lod Clamp` | Float |
| `Offset` | Integer3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

> ❗ **Important**: This node requires a device with a [`MTLGPUFamily.apple6`](../../Metal/mtlgpufamily/apple6.md) or later GPU and may not be available on certain devices. To determine GPU feature support at runtime, see [Detecting GPU features and Metal software versions](../../Metal/detecting-gpu-features-and-metal-software-versions.md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/image-3d-(realitykit))*