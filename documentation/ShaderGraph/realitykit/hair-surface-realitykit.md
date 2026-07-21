# Hair Surface (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

A surface shader that defines properties for a RealityKit Hair material.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

#### Parameter Types

#### Discussion

The Hair Surface node produces a custom surface based on its input parameters. Connect the output of the Hair Surface node to the `Custom Surface` output of your material.

#### Parameter Descriptions

- **`Base Color`**: The base display color of the surface. The color of an object under pure white light.
- **`Opacity`**: The level of opaqueness of the surface. If the value of this parameter is `1.0`, the surface is fully opaque. If the value is less than `1.0`, the surface appears translucent. If the value is `0.0`, the surface is completely transparent. The default value is `1.0`.
- **`Opacity Threshold`**: The threshold for whether a portion of the surface renders based on its opacity level. A value of `0.0` means that no additional masking occurs. If the value is greater than `0.0`, the node renders only areas of the surface with an `Opacity` value greater than the value of this parameter. This parameter can be enabled or disabled. This parameter can be on or off; the default is off.
- **`Ambient Occlusion`**: The degree of ambient lighting that the surface receives. This value simulates soft shadows and subtle shading. The default value is `1.0`.
- **`Normal`**: The normal vector in tangent space. For hair, use a normal that points outward from the hair volume. The default value is `(0,0,1)`.
- **`Tangent`**: The tangent vector in tangent space. For hair, this represents the direction along the hair strand. The default value is `(0,1,0)`.
- **`Primary Specular Color`**: The color of the primary specular highlight of the material. The default value is `(1,1,1)`.
- **`Primary Specular`**: The brightness of the primary specular highlight of the material. The default value is `0.5`.
- **`Primary Roughness`**: The level of roughness of the primary specular highlight. This value ranges between `0.0` and `1.0`, with lower values producing a sharper highlight and `1.0` indicating maximum roughness. The default value is `0.3`.
- **`Primary Shift`**: The amount of primary specular highlight shift along the direction of the normal. Primary specular highlight typically shifts towards the hair tip. The default value is `0.0`.
- **`Secondary Specular Color`**: The color of the secondary specular highlight of the material. The default value is `(0,0,0)`.
- **`Secondary Specular`**: The brightness of the secondary specular highlight of the material. The default value is `0.0`.
- **`Secondary Roughness`**: The level of roughness of the secondary specular highlight. This value ranges between `0.0` and `1.0`, with lower values producing a sharper highlight and `1.0` indicating maximum roughness. The default value is `0.0`.
- **`Secondary Shift`**: The amount of secondary specular highlight shift along the direction of the normal. Secondary specular highlight typically shifts towards the hair root. The default value is `0.0`.
- **`Backlit Color`**: The color of the backlit scattering of the material. The default value is `(0,0,0)`.
- **`Backlit Power`**: The falloff exponent of the backlit scattering of the material. Use higher values for hair styles with less volume and lower values for hair styles with more volume, where light scatters through more strands. The default value is `10.0`.
- **`Backlit Scale`**: The intensity of the backlit scattering of the material. This value ranges between `0.0` and `1.0`. The default value is `0.0`.
- **`Shadow Density`**: The density of the shadow cast by the material. This value ranges between `0.0` and `1.0`, with `1.0` producing a fully dense shadow and `0.0` producing no shadow. Intermediate values require the surface to have varying opacity to take effect. The default value is `1.0`.
- **`Has Premultiplied Alpha`**: A Boolean value that informs the node if input parameters have a premultiplied alpha. The default value is `false`.

## See Also

- [Unlit Surface (RealityKit)](realitykit/unlit-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Unlit material.
- [PBR Surface (RealityKit)](realitykit/pbr-surface-(realitykit).md)
  A surface shader that defines properties for a RealityKit Physically Based Rendering material.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/hair-surface-(realitykit))*