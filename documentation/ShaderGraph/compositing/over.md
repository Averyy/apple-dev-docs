# Over

**Framework**: ShaderGraph  
**Kind**: subscript

A merge operation that layers foreground over background, using the alpha of the foreground.

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

The `Over` node determines its output using the alpha channels of the foreground and background inputs. The RGB component of the output is `F+B(1-f)` and the alpha component of the output is `f+b(1-f)`. The lower the alpha of the foreground, the more the background blends into the foreground. Below is a simple node graph that uses the `Over` node to blend a wood and rock texture:

![None](https://docs-assets.developer.apple.com/published/503d8805c54670aacb2736562f018f3a/OverGraph.png)

Below are the two original images, the image representation of the alpha of the foreground, and the resulting blended texture applied to a cube:

![None](https://docs-assets.developer.apple.com/published/5c3c4fbe9151465a0b07c0df62c429df/OverMaterial.png)

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
- [Inside](compositing/inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/over)*