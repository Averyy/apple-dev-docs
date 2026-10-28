# Unlit Surface (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A surface shader that defines properties for a RealityKit Unlit material.

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
| `Color` | Color3 |
| `Opacity` | Float |
| `Opacity Threshold` | Float |
| `Apply Post Process Tone Map` | Bool |
| `Has Premultiplied Alpha` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Token |

## Parameter descriptions

- **`Color`**: The base color of the surface.
- **`Opacity`**: The level of opaqueness of the surface. If the value of this parameter is `1.0`, the surface is fully opaque. If the value is less than `1.0`, the surface appears translucent. If the value is `0`, the surface is completely transparent. The default value is `1.0`.
- **`Opacity Threshold`**: The threshold for whether the node renders a portion of the surface based on its opacity level. A value of `0.0` means that no additional masking occurs. If the value is greater than `0.0`, the node renders only areas of the surface with an `Opacity` value greater than the value of this parameter. This parameter can be turned on or off. The default value is `0.0`.
- **`Apply Post Process Tone Map`**: A Boolean value that tells the node whether to apply the post process tone map.
- **`Has Premultiplied Alpha`**: A Boolean value that tells the node if it has a premultiplied alpha.

## Discussion

The `Unlit Surface` node produces a custom surface based on its input parameters. Connect the output of the `Unlit Surface` node connect to the `Custom Surface` output of your material.

## See Also

### Nodes
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
- [Surface Model To View (RealityKit)](./surface-model-to-view-%28realitykit%29.md)
  The model-to-view transformation Matrix4x4 (Float).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/unlit-surface-(realitykit))*