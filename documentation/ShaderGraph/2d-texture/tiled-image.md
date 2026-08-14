# Tiled Image

**Framework**: ShaderGraph  
**Kind**: subscript

Samples data from an image with provisions for offsetting and tiling in UV space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

- **`File`**: The image file to use for the texture.
- **`Default`**: A default value to use if the ​file​ reference fails to resolve.
- **`Texture Coordinates`**: The 2D coordinate at which the data is read for mapping the texture onto a surface. The default uses the current UV coordinates, in which U is the horizontal axis and V is the vertical axis.
- **`UV Tiling`**: The tiling rate for the given image along the U and V axes. The tiling rate is mathematically equivalent to multiplying the incoming texture coordinates by the given vector value. The rate controls how often the `File` repeats in the texture.
- **`UV Offset`**: The offset for the given image along the U and V axes. The offset is mathematically equivalent to subtracting the given vector value from the incoming texture coordinates.
- **`Real World Image Size`**: The real-world size represented by the ​file​ image.
- **`Real World Tile Size`**: The real-world size of a single square `0-1` UV tile.
- **`Filter Type`**: The type of texture filtering to use.

#### Discussion

The `Tiled Image` material node maps a texture onto a surface with a repeating tiled pattern. It allows you to specify a texture image and control its tiling and real-world size properties.

The `UV Tiling` parameter repeats the given file input to produce an image. The `Real World Image Size` parameter determines the image’s size. The resulting image is then applied to a single square 0-1 UV tile. The `Real World Tile Size` parameter determines the size of this tile. The size of the tile and the size of the image may differ. If the image size is larger than the tile it wants to be applied to, the resulting texture only shows part of the image. If the size of the tile is larger than the image, the image repeats in the resulting texture.

> **Note**: If your goal is to repeat the image, use the `UV Tiling` parameter. While you can create a repeating texture by using the `Real World Image Size` and `Real World Tile Size` parameters, use the size parameters to model real-world dimensions of the image and the surface that it’s applied to.

Below is an example of a simple node graph that uses the Tiled Image node:

![nil](/images/ShaderGraph-Docs/TiledImage1.png)

If the `UV Tiling` parameter is `(2,2)`, the pattern repeats twice horizontally and twice vertically:

![nil](/images/ShaderGraph-Docs/TiledImage2.png)

## See Also

- [Image](2d-texture/image.md)
  A texture referencing a 2D image file.
- [UV Texture](2d-texture/uv-texture.md)
  A MaterialX version of USD UV Texture reader.
- [Transform 2D](2d-texture/transform-2d.md)
  A node that applies an affine transformation to a 2d input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-texture/tiled-image)*