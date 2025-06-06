# In

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs areas of foreground that overlap with the alpha of background.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The in node determines its output using the alpha channels of the foreground and background inputs. The RGB component of the output is `F*b` and the alpha component of the output is `f*b`. Visually this means that within the output, the foreground values that overlap with the background alpha are preserved. Below is a simple node graph that uses the In node to blend a tile and rock texture.

![None](https://docs-assets.developer.apple.com/published/339bc485ee3fd52253f3d2f18f3372dd/InGraph.png)

Below are the two original images, the image representation of the alpha of the background, and the resulting blended texture applied to a cube.

![None](https://docs-assets.developer.apple.com/published/a5f6c8440c7e605eff2c54d690b10383/InMaterial.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/in)*