# Cube Image Gradient (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript

A texturecube with RealityKit properties and a specified LOD gradient.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Overview

Level of detail gradient. Input image must be in KTX file format

#### Parameter Types

#### Parameter Descriptions

- **`File`**: The image file to use for the texture.
- **`U Wrap Mode`**: The way the node handles U values outside of the range of `0-1`. The default value is `clamp_to_edge`.
- **`V Wrap Mode`**: The way the node handles V values outside of the range of `0-1`. The default value is `clamp_to_edge`.
- **`Border Color`**: A color that fills in areas of a material’s surface not covered by the material property’s image contents. The default value is `transparent_black`.
- **`Mag Filter`**: The magnification filtering mode the node uses to render the image contents at a size larger than the original image. For example, the texture coordinates at a point near the camera may correspond to a small fraction of a pixel in the texture image. This node uses the `Mag Filter` to determine the color of the sampled texel at that point. The default value is `linear`.
- **`Min Filter`**: The minimizing filtering mode the node uses to render the image contents at a size smaller than the original image. For example, the texture coordinates at a point far from the camera may correspond to an area of several pixels in the texture image. This node uses the `Min Filter` to determine the color of the sampled texel at that point. The default value is `linear`.
- **`Mip Filter`**: The mipmap filtering mode the node uses when rendering the image contents using mipmapping. Useful when rendering an image at a size smaller than the original image. If the value of this parameter is `None`, the node won’t use mipmapping. The default value is `linear`.
- **`Max Anisotropy`**: The amount of anisotropic texture filtering applied when rendering the texture’s image contents. Used when rendering the image contents at an extreme angle relative to the camera. This parameter is used only in conjunction with mipmapping, so it only has an effect if `Mip Filter` isn’t `None`. The default value is `1`.
- **`Max Lod Clamp`**: The maximum level of detail allowed for the rendered image contents. As an object gets closer to the camera, the level of detail used to render the texture of that object increases up to the maximum defined by this parameter. The default value is `65504`.
- **`Min Lod Clamp`**: The minimum level of detail allowed for the rendered image contents. As an object gets farther from the camera, the level of detail used to render the texture of that object decreases to the minimum defined by this parameter. The default value is `0`.
- **`Default`**: The default value to use if the ​`File​` parameter fails to resolve.
- **`Texture Coordinates`**: The 2D coordinate at which the data is read to map the texture onto a surface. The default is the current UV coordinates, in which U is the horizontal axis and V is the vertical axis.
- **`Dynamic Min Lod Clamp`**: The minimum level of detail allowed for the rendered image contents. Similar to the `Min Lod Clamp` parameter, except you can change this parameter dynamically at runtime.
- **`Gradientcube D Pdx`**: The rate of change of the surface geometry in the X direction of the sampled surface or texture.
- **`Gradientcube D Pdy`**: The rate of change of the surface geometry in the Y direction of the sampled surface or texture.

#### Discussion

The `Cube Image Gradient` node produces a texture using the contents of the image file specified in the `File` parameter. It has a variety of parameters that affect the properties of the rendered textures.

> **Note**: Create the input file in a `.ktx` format or the node won’t work properly.

The possible values for the wrap mode parameters are:

- **`clamp_to_border`**: The node sets texture coordinates outside the normal range to the color specified by the `Border Color` parameter.
- **`clamp_to_edge`**: The node clamps texture coordinates outside the normal range to the normal range. The node sets any values greater than `1` to `1`, and any values less than `0` to `0`. This means the colors on the edge of the image extend to fill the rest of the texture.
- **`clamp_to_zero`**: The node sets texture coordinates outside the normal range to a color of value of `0` or black. This is equivalent to the `clamp_to_border` option with a border color of `transparent_black`.
- **`mirrored_repeat`**: The node mirrors texture coordinates outside the normal range.
- **`repeat`**: The node causes texture coordinates outside the normal range to “wrap around.” This behavior is equivalent to the node applying modulo 1 to the coordinates.

> ⚠️ **Warning**: You can only use `clamp-to-zero` if the `Border Color` parameter is set to `transparent_black`; otherwise, the behavior of the node is undefined.

The possible values for `Mag Filter` and `Min Filter` are:

- **`linear`**: The filter uses linear interpolation of the closest values to determine the rendered contents.
- **`nearest`**: The filter uses the nearest value to determine the rendered contents.

The `Mip Filter` parameter has the same possible values as noted above with the addition of allowing for the value of `None`, which specifies that it doesn’t use mipmapping.

For an example of how to use this node, see [`Cube Image (RealityKit)`](realitykit/cube-image-(realitykit).md).

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/realitykit/cube-image-gradient-(realitykit))*