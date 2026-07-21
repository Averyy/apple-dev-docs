# PBR Surface (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

A surface shader that defines properties for a RealityKit Physically Based Rendering material.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

- **`Base Color`**: The base display color of the surface. The color of an object under pure white light.
- **`Emissive Color`**: The self-illumination color of the surface. The color the surface displays as if it’s self-lit.
- **`Normal`**: The normal vector in tangent space. The default is `(0,0,1)`.
- **`Roughness`**: The level of roughness of the surface. This value ranges between `0` and `1.0`, with `0` outputting a perfectly specular surface and `1.0` indicating maximum roughness. The default is `0.5`.
- **`Metallic`**: Indicates whether a surface is metallic. Set this value to `1` for metallic surfaces, and to `0` for nonmetallic surfaces. The default is `0.0`.
- **`Ambient Occlusion`**: The degree of ambient lighting that the surface receives. This value simulates soft shadows and subtle shading.
- **`Specular`**: The brightness of the specular highlight of the material.
- **`Opacity`**: The level of opaqueness of the surface. If the value of this parameter is `1.0`, the surface is fully opaque. If the value is less than `1.0`, the surface appears translucent. If the value is `0`, the surface is completely transparent. The default is `1.0`.
- **`Opacity Threshold`**: The threshold for whether a portion of the surface renders based on its opacity level. A value of `0.0` means that no additional masking occurs. If the value is greater than `0.0`, the node renders only areas of the surface with an `Opacity` value greater than the value of this parameter. This parameter can be turned on or off. The default value is `0.0`.
- **`Clearcoat`**: A second clear reflective layer on the surface. This property produces a glossy finish. The default is `0.0`.
- **`Clearcoat Roughness`**: The level of roughness of the surfaces clearcoat layer. The default is `0.01`.
- **`Has Premultiplied Alpha`**: A Boolean value to let the node know if input parameters have a premultiplied alpha.

#### Discussion

The PBR Surface node produces a custom surface based on its input parameters. Connect the output of the PBR Surface node to the `Custom Surface` output of your material.

Below is an example material that uses only the `PBR Surface` node to produce a gold-like texture and apply it to a sphere:

## See Also

- [Unlit Surface (RealityKit)](realitykit/unlit-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Unlit material.
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
- [Surface Model To View (RealityKit)](realitykit/surface-model-to-view-(realitykit).md)
  The model-to-view transformation Matrix4x4 (Float).


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/pbr-surface-(realitykit))*