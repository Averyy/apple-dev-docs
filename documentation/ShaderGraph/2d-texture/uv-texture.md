# UV Texture

**Framework**: ShaderGraph  
**Kind**: subscript

A MaterialX version of USD UV Texture reader.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

- **Bias**: The bias the node applies to all components of the texture. The node adds this parameter to the texture after multiplying it by the scale.
- **Fallback**: The value to use if the texture can’t be read from the file.
- **File**: The image file to use for the texture.
- **Scale**: The scale the node applies to all components of the texture. The node multiplies the texture value by this parameter.
- **St**: The 2D coordinate at which the data is read for mapping the texture onto a surface. This node maps from `st` to `uv` image space. The `(0,0)` coordinate in `st` image space maps to the `(0,0)` coordinate in the `uv` space which represents the lower-left–hand corner. The `(1,1)` coordinate in `st` image space maps to the `(1,1)` coordinate in `uv` space which represents the upper-right–hand corner.
- **Wrap S**: The way that the node handles `S` values outside of the range of `0-1`.
- **Wrap T**: The way that the node handles `T` values outside of the range of `0-1`.

#### Output Descriptions

- **RGBA**: The `Color4` output of the texture that contains a red, green, blue, and alpha component.
- **RGB**: The standard `Color3` output of the texture that contains a red, green, and blue component.
- **Read**: Only the red component of the texture.
- **Green**: Only the green component of the texture.
- **Blue**: Only the blue component of the texture.
- **Alpha**: Only the alpha component of the texture.

#### Discussion

The `Wrap` parameters for the node tell the node how to handle `S` and `T` values outside of the normal range of `0-1`. These inputs take one of four values to determine their behavior.

- black: Texture coordinates outside the normal range return black.
- clamp: Texture coordinates outside the normal range clamp to the normal range. Any values greater than `1` are set to `1`, and any values less than `0` are set to `0`
- periodic: Texture coordinates outside the normal range are normalized into a range of `0-1`, tiling the image. This is effectively equivalent to applying modulo 1 to the coordinates.

## See Also

- [Image](2d-texture/image.md)
  A texture referencing a 2D image file.
- [Tiled Image](2d-texture/tiled-image.md)
  Samples data from an image with provisions for offsetting and tiling in UV space.
- [Transform 2D](2d-texture/transform-2d.md)
  A node that applies an affine transformation to a 2d input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-texture/uv-texture)*