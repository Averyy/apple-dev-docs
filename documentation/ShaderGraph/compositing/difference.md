# Difference

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs the distance between foreground and background values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Overview

abs(B - F)

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Difference` node subtracts two inputs and takes the absolute value of the result, represented by the equation `abs(B - F)`. It uses the `Mix` input to determine the weight of the foreground in the blend. Higher values closer to `1` output a more intense difference, while lower values closer to `0` dim the effect. Below is an example of a node graph that uses the difference node to blend two images together into a single material:

![None](https://docs-assets.developer.apple.com/published/df0b2a945ff0248fd2850cac564a8a26/DifferenceGraph.png)

Below are two images and the resulting blended texture applied to a cube.

![None](https://docs-assets.developer.apple.com/published/262c61aaa1f893b613b75080338aaad7/DifferenceMaterial.png)

## See Also

- [Premultiply](compositing/premultiply.md)
  Multiplies the RGB channels of the input by the alpha channel.
- [Unpremultiply](compositing/unpremultiply.md)
  Divides the RGB channels of the input by the alpha channel.
- [Additive Mix](compositing/additive-mix.md)
  Adds foreground and background values.
- [Subtractive Mix](compositing/subtractive-mix.md)
  Subtracts foreground from background values.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/difference)*