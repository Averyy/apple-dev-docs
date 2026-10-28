# Environment Radiance (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Returns an environment’s diffuse and specular radiance value based on real-world environment, and an IBL map that is either a developer-provided map or a default map.

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
| `Base Color` | Color3 |
| `Roughness` | Half |
| `Specular` | Half |
| `Metallic` | Half |
| `Normal` | Vector3f |

| Output | Type |
| --- | --- |
| `Diffuse Radiance` | Color3 |
| `Specular Radiance` | Color3 |

## Parameter descriptions

- **`Base Color`**: The base display color of the surface. The color under pure white light.
- **`Roughness`**: The level of roughness of the surface. This value ranges between `0` and `1.0`, with `0` representing a perfectly specular surface and `1.0` representing maximum roughness. The default value is `0`.
- **`Specular`**: The level of specular reflections that occur on the surface.
- **`Metallic`**: The indicator if a surface is metallic or not. Set this value to `1` for metallic surfaces and `0` for nonmetallic surfaces. The default value is `0.0`.
- **`Normal`**: The surface normal vector. The default value is `(0,0,0)`.

## Discussion:

The Environment Radiance node has two outputs:

- **`Diffuse Radiance`**: The diffuse radiance of the surface. Refers to light absorbed by the surface and then re-emitted in all directions.
- **`Specular Radiance`**: The specular radiance of the surface. Refers to light reflected off of the surface.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/environment-radiance-(realitykit))*