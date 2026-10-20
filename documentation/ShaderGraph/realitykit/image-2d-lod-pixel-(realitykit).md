# Image 2D LOD Pixel (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

A texture with RealityKit properties, a explicit level of detail, and pixel texture coordinates.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Overview

Explicit level of detail. Pixel texture coordinates

#### Parameter Types

#### Parameter Descriptions

- **`File`**: The image file to use for the texture.
- **`U Wrap Mode`**: The way the node handles *U* values outside of the range of `0-1`. The default value is `clamp_to_edge`.
- **`V Wrap Mode`**: The way the node handles *V* values outside of the range of `0-1`. The default value is `clamp_to_edge`.
- **`Border Color`**: A color that fills in areas of a material’s surface not covered by the material property’s image contents. The default value is `transparent_black`.
- **`Filter`**: Both the magnification and the minification filter the node uses to render the image contents at a size larger or smaller than the original image.
- **`Max Anisotropy`**: The amount of anisotropic texture filtering applied when rendering the texture’s image contents. Used when rendering the image contents at an extreme angle relative to the camera. This parameter is used only in conjunction with mipmapping, so it only has an effect if `Mip Filter` isn’t `None`. The default value is `1`.
- **`Max Lod Clamp`**: The maximum level of detail allowed for the rendered image contents. As an object gets closer to the camera, the level of detail used to render the texture of that object increases up to the maximum defined by this parameter. The default value is `65504`.
- **`Min Lod Clamp`**: The minimum level of detail allowed for the rendered image contents. As an object gets farther from the camera, the level of detail used to render the texture of that object decreases to the minimum defined by this parameter. The default value is `0`.
- **`Default`**: The default value to use if the ​`File​` parameter fails to resolve.
- **`Texture Coordinates`**: The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is the current *UV* coordinates, in which *U* is the horizontal axis and *V* is the vertical axis.
- **`Lod`**: The specific LOD level that the node will sample from.
- **`Offset`**: The integer values added to the texture coordinates before looking up each pixel. The value must be within the range `-8-7`. The default value is `0`.

#### Discussion

The Image 2D LOD Pixel node produces a texture using the contents of the image file specified in the `File` parameter. It has a multitude of parameters that affect the properties of the rendered textures.

For the wrap mode parameters, the possible values are:

- **`clamp_to_border`**: The node sets texture coordinates outside the normal range to the color specified by the `Border Color` parameter.
- **`clamp_to_edge`**: The node clamps texture coordinates outside the normal range to the normal range. The node will set any values greater than `1` to `1`, and any values less than `0` to `0`. This means the color’s on the edge of the image will extend to fill the rest of the texture.
- **`clamp_to_zero`**: The node sets texture coordinates outside the normal range to a color of value of `0` or black. This is equivalent to the `clamp_to_border` option with a border color of `transparent_black`.
- **`mirrored_repeat`**: The node mirrors texture coordinates outside the normal range.
- **`repeat`**: The node will cause texture coordinates outside the normal range to “wrap around.” This behavior is effectively equivalent to the node applying modulo 1 to the coordinates.

> ⚠️ **Warning**: You can only use the clamp-to-zero option if the `Border Color` parameter is set to `transparent_black`; otherwise, the behavior of the node is undefined.

For the `Filter` parameters, the possible values are:

- **`linear`**: The filter uses linear interpolation of the closest values in order to determine the rendered contents.
- **`nearest`**: The filter uses the nearest value in order to determine the rendered contents.

For an example on how to use this node, see the bottom of the [`Image 2D (RealityKit)`](realitykit/image-2d-(realitykit).md) node page.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/image-2d-lod-pixel-(realitykit))*