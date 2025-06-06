# Outside

**Framework**: ShaderGraph  
**Kind**: subscript

Multiplies (1 - mask) to all channels of the input.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

Below is an example of a simple node graph that uses the Outside node to apply a mask to a brick texture.

![None](https://docs-assets.developer.apple.com/published/fa72f1155b0049c8effbed2bbc869017/OutsideGraph.png)

Below, the resulting texture applies to a cube.

![None](https://docs-assets.developer.apple.com/published/38b4a6a44aa78ba48dc64c3a582f6f37/OutsideMaterial.png)

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
- [Out](compositing/out.md)
  Outputs areas of foreground that do not overlap with background.
- [Over](compositing/over.md)
  A merge operation that layers foreground over background, using the alpha of the foreground.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/outside)*