# Burn

**Framework**: ShaderGraph  
**Kind**: subscript

A blend operation that darkens the foreground layer using the background.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Overview

1 - (1 - B) / F

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Burn` node darkens each area in the background based on the darkness of the corresponding area in the foreground, represented by the equation `1 - (1 - B) / F`. Below is an example of a node graph that uses the `Burn` node to darken a brick texture:

![None](https://docs-assets.developer.apple.com/published/47249df37324d4d19ad18877480395f9/BurnGraph.png)

Use a [`Noise 2D`](2d-procedural/noise-2d.md) node to generate Perlin noise, and use the output of that texture as the foreground in the `Burn` node. This process darkens the background brick texture according to the procedural pattern. Below, the resulting texture applies to a cube:

![None](https://docs-assets.developer.apple.com/published/566f3dfbd55a92bb27315df1e62c5540/BurnMaterial.png)

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
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/burn)*