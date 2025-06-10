# Screen

**Framework**: ShaderGraph  
**Kind**: subscript

A blend operation that lightens areas that are darker than white.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Overview

1 - (1 - F)(1 - B)

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Screen` node inverts the color values of both the foreground and background and multiplies those values together. Then the node inverts the colors again, as represented by the equation: `1 - (1 - F)(1 - B)`. The resulting visual effect is always equally bright or brighter than the original textures. Below is an example of a simple node graph that uses the `Screen` node to blend two images together into a single material:

![None](https://docs-assets.developer.apple.com/published/28a0a55b18ecac5972bd5ed2e21eebeb/ScreenGraph.png)

Below are two images and their resulting blended texture applied to a cube:

![None](https://docs-assets.developer.apple.com/published/5a84eb39e40779bc1d9fb68d07252bf4/ScreenMaterial3.png)

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
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/screen)*