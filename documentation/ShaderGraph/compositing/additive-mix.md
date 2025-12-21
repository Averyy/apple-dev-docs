# Additive Mix

**Framework**: ShaderGraph  
**Kind**: subscript

Adds foreground and background values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Overview

B + F

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Additive Mix` node combines two inputs and uses the `Mix` input to determine the weight of the foreground in the blend, represented by the equation `B + F`. Higher values closer to `1` intensify the effect of the mix, while lower values closer to `0` dim the effect. Below is an example of a node graph that uses the `Additive Mix` node to blend two images together into a single material:

![None](https://docs-assets.developer.apple.com/published/795f41ac899dbe8062aa2c8326b12153/AdditiveMixGraph.png)

Below are two images and their resulting blended texture applied to a cube:

![None](https://docs-assets.developer.apple.com/published/1ce8d8ad8c57d334565a0b00269c0ed0/AdditiveMixMaterial.png)

## See Also

- [Premultiply](compositing/premultiply.md)
  Multiplies the RGB channels of the input by the alpha channel.
- [Unpremultiply](compositing/unpremultiply.md)
  Divides the RGB channels of the input by the alpha channel.
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
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/additive-mix)*