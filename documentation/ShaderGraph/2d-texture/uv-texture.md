# UV Texture

**Framework**: ShaderGraph  
**Kind**: subscript

A MaterialX version of USD UV Texture reader.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

#### Output Descriptions

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