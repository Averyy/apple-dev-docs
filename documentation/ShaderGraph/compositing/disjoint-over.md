# Disjoint Over

**Framework**: ShaderGraph  
**Kind**: subscript

A merge operation that layers foreground over background color, but assumes no overlap in partially transparent areas covered by both.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Disjoint Over node performs one of two mixes based on the alpha channels of the foreground and background inputs. If `f+b<=1`, then the RGB component of the output is `F+B`. If `f+b>1`, then the RGB component of the output is `F+b(1-f)/b`. The alpha component of the output for this node is always the smaller value between `f+b` or 1. Below is a simple node graph that uses the Disjoint Over node to blend a tile and rock texture.

![None](https://docs-assets.developer.apple.com/published/eca8c920080f8f96111adac027da05b0/DisjointOverGraph.png)

The graph remaps the alpha of the rock texture from a range of `0-1` to a range of `-1-2` in order to show more of the effect of both possible modes of the blend. Below are the two original images and their resulting blended texture applied to a cube.

![None](https://docs-assets.developer.apple.com/published/c81d51bd455f4890ce12bcdfa39e05a9/DisjointOverMaterial3.png)

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
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/disjoint-over)*