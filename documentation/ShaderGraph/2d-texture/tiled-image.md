# Tiled Image

**Framework**: Shadergraph  
**Kind**: subscript

Samples data from an image with provisions for offsetting and tiling in UV space.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Tiled Image material node maps a texture onto a surface with a repeating tiled pattern. It allows you to specify a texture image and control its tiling and real-world size properties. The `UV Tiling` parameter repeats the given file input to produce an image. This image’s size is determined by the `Real World Image Size` parameter. The resulting image is then applied to a single square 0-1 UV tile. The size of this tile is determined by the `Real World Tile Size` parameter. The size of the tile and the size of the image may differ. Therefore, if the image size is larger than the tile it wants to be applied to, the resulting texture will only show part of the image. On the other hand, if the size of the tile is larger than the image, you will see the image repeated in the resulting texture.

> **Note**: While you can create a repeating texture by using the `Real World Image Size` and `Real World Tile Size` parameters, if your only goal is repeating the image, use the `UV Tiling` parameter. Use the size parameters to model real-world dimensions of the image and the surface to which it is applied to.

Below is an example of a simple node graph that uses the Tiled Image node.

![nil](https://docs-assets.developer.apple.com/published/b1e7815b71b078c16fab9f0895dff0c2/TiledImage1.png)

If the `UV Tiling` parameter is (2,2) the pattern repeats twice horizontally and twice vertically.

![nil](https://docs-assets.developer.apple.com/published/4852a827f845f57e396ff75ac1dad7b8/TiledImage2.png)

## See Also

- [Image](2d-texture/image.md)
  A texture referencing a 2D image file.
- [UV Texture](2d-texture/uv-texture.md)
  A MaterialX version of USD UV Texture reader.
- [Transform 2D](2d-texture/transform-2d.md)
  A node that applies an affine transformation to a 2d input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-texture/tiled-image)*