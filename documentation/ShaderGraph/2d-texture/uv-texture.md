# UV Texture

**Framework**: ShaderGraph  
**Kind**: subscript

A MaterialX version of USD UV Texture reader.

#### Parameter Types

#### Parameter Descriptions

#### Output Descriptions

#### Discussion

The Wrap parameters for the node tell the node how to handle S and T values outside of the normal range of `0-1`. These inputs take one of four values to determine there behavior.

- black: Texture coordinates outside the normal range return black.
- clamp: Texture coordinates outside the normal range are clamped to the normal range. Any values greater than `1` will be set to `1` and any values less than `0` will be set to `0`
- periodic: Texture coordinates outside the normal range will “wrap around”. This is effectively equivalent to modulo 1 being applied to the coordinates.

## See Also

- [Image](2d-texture/image.md)
  A texture referencing a 2D image file.
- [Tiled Image](2d-texture/tiled-image.md)
  Samples data from an image with provisions for offsetting and tiling in UV space.
- [Transform 2D](2d-texture/transform-2d.md)
  A node that applies an affine transformation to a 2d input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-texture/uv-texture)*