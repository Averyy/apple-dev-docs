# Out

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs areas of foreground that do not overlap with background.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Out node determines its output using the alpha channels of the foreground and background inputs. The RGB componenet of the output is `F*(1-b)` and the alpha component of the output is `f*(1-b)`. The visual effect of this node is that within the output, the node preserves the foreground values that don’t overlap with the background alpha. Below is a simple node graph that uses the Out node to blend a tile and rock texture.

![None](https://docs-assets.developer.apple.com/published/04e78fb41d59011bd10ba19b9c34b3b1/OutGraph.png)

Below are the two original images, the image representation of the alpha of the background, and the resulting blended texture applied to a cube.

![None](https://docs-assets.developer.apple.com/published/0e71e7aadb26f829170a47817bc44bae/OutMaterial.png)

## See Also

- [Premultiply](compositing/premultiply.md)
  Multiplies the RGB channels of the input by the alpha channel.
- [Unpremultiply](compositing/unpremultiply.md)
  Divides the RGB channels of the input by the alpha channel.
- [Additive Mix](compositing/additive-mix.md)
  Adds foreground and background values.
- [Subtractive Mix](compositing/subtractive-mix.md)
  Subtracts foreground from background values.
- [Difference](compositing/difference.md)
  Outputs the distance between foreground and background values.
- [Burn](compositing/burn.md)
  A blend operation that darkens the foreground layer using the background.
- [Dodge](compositing/dodge.md)
  A blend operation that lightens the background layer depending on the foreground.
- [Screen](compositing/screen.md)
  A blend operation that lightens areas that are darker than white.
- [Overlay](compositing/overlay.md)
  A blend operation that multiplies dark areas and screens light areas.
- [Disjoint Over](compositing/disjoint-over.md)
  A merge operation that layers foreground over background color, but assumes no overlap in partially transparent areas covered by both.
- [In](compositing/in.md)
  Outputs areas of foreground that overlap with the alpha of background.
- [Mask](compositing/mask.md)
  Outputs areas of background that overlap with the alpha of foreground.
- [Matte](compositing/matte.md)
  A merge operation that layers premultiplied foreground over background.
- [Over](compositing/over.md)
  A merge operation that layers foreground over background, using the alpha of the foreground.
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/out)*