# Mix

**Framework**: ShaderGraph  
**Kind**: subscript

Mixes foreground and background inputs, weighting based on mix value.

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Mix node blends two input values together, represented by the equation `F * m + B(1 - m)`.  If the `Mix` value is `1`, the output is identical to the `Foreground` value. If the value is `0`, the output is identical to the `Background` value. The closer the `Mix` value is to `0` or `1`, the closer the output will be to the corresponding input. Use the Mix node to blend between two different textures and create transtions or effects, interpolate between two colors, or mix shader parameters. Below is an example of a simple node graph that uses the Mix node to blend two images together into a single material.

![None](https://docs-assets.developer.apple.com/published/b3384b6745c8bc85f86c162a23029dde/MixGraph.png)

Below are the original two images and the resulting mixed texture applied to a cube with `Mix` values of `0.1`, `0.5`, and `0.9`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/mix)*