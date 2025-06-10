# Mask

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs areas of background that overlap with the alpha of foreground.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The Mask node determines its output using the alpha channels of the foreground and background inputs. The RGB componentt of the output is `B*f` and the alpha component of the output is `b*f`. Below is a simple node graph that uses the Mask node to blend a wood and rock texture:

![None](https://docs-assets.developer.apple.com/published/f6af153ade32c2f2a77ced0dfcd39ca2/MaskGraph.png)

Below are the two original images, the image representation of the alpha of the foreground, and the resulting blended texture applied to a cube:

![None](https://docs-assets.developer.apple.com/published/631d442b75841a9df3778a63597acecf/MaskMaterial2.png)

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
- [Matte](compositing/matte.md)
  A merge operation that layers premultiplied foreground over background.
- [Out](compositing/out.md)
  Outputs areas of foreground that do not overlap with background.
- [Over](compositing/over.md)
  A merge operation that layers foreground over background, using the alpha of the foreground.
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/mask)*