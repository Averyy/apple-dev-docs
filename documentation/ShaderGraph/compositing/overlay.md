# Overlay

**Framework**: ShaderGraph  
**Kind**: subscript

A blend operation that multiplies dark areas and screens light areas.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Overview

2 * F * B if F < 0.5; 1 - (1 - F)(1 - B) if F >= 0.5

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Overlay` node has one of two effects:

- If `F+B` is less than `0.5`, then the node outputs a value of `2*F*B`.
- If `F+B` is greater than or equal to `0.5`, then it outputs`1-(1-F)(1-B)`, which creates the same visual effect as the [`Screen`](compositing/screen.md) node. Visually the node makes dark areas of the blended texture even darker and light areas of the blended texture even lighter.

Below is an example of a simple node graph that uses the `Overlay` node to blend two images together into a single material:

![None](https://docs-assets.developer.apple.com/published/7ceec91d585b58948afa1611c167fc34/OverlayGraph.png)

Below are two images and their resulting blended texture applied to a cube:

![None](https://docs-assets.developer.apple.com/published/e2d08d8613e4333f8d28526d6c713847/OverlayMaterial2.png)

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
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/overlay)*