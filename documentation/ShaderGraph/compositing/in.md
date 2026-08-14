# In

**Framework**: ShaderGraph  
**Kind**: subscript

Outputs areas of foreground that overlap with the alpha of background.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

- **`Foreground`**: The `color4` foreground input. `F` represents the RGB component of this parameter. `f` represents the alpha component of this parameter.
- **`Background`**: The `color4` background input. `B` represents the RGB component of this parameter. `b`represents the alpha component of this parameter.
- **`Mix`**: The weight of the blend operation. The higher the value of `Mix`, the more apparent the effect of the blend operation. The default value is `1`. Values outside of the range `0-1` produce an undefined effect outside of the node’s intended function.

#### Discussion

The in node determines its output using the alpha channels of the foreground and background inputs. The RGB component of the output is `F*b` and the alpha component of the output is `f*b`. Visually this means that within the output, the foreground values that overlap with the background alpha are preserved. Below is a simple node graph that uses the In node to blend a tile and rock texture.

![None](/images/ShaderGraph-Docs/InGraph.png)

Below are the two original images, the image representation of the alpha of the background, and the resulting blended texture applied to a cube.

![None](/images/ShaderGraph-Docs/InMaterial.png)

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