# Disjoint Over

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A merge operation that layers foreground over background color, but assumes no overlap in partially transparent areas covered by both.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

| Input | Type |
| --- | --- |
| `Foreground` | Color4 |
| `Background` | Color4 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

#### Parameter descriptions

- **`Foreground`**: The `color4` foreground input. `F` represents the RGB component of this parameter. `f` represents the alpha component of this parameter.
- **`Background`**: The `color4` background input. `B` represents the RGB component of this parameter. `b`represents the alpha component of this parameter.
- **`Mix`**: The weight of the blend operation. The higher the value of `Mix`, the more apparent the effect of the blend operation. The default value is `1`. Values outside of the range `0-1` produce an undefined effect outside of the node’s intended function.

#### Discussion

The Disjoint Over node performs one of two mixes based on the alpha channels of the foreground and background inputs. If `f+b<=1`, then the RGB component of the output is `F+B`. If `f+b>1`, then the RGB component of the output is `F+b(1-f)/b`. The alpha component of the output for this node is always the smaller value between `f+b` or 1. Below is a simple node graph that uses the Disjoint Over node to blend a tile and rock texture:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/DisjointOverGraph.png)

The graph remaps the alpha of the rock texture from a range of `0-1` to a range of `-1-2` in order to show more of the effect of both possible modes of the blend. Below are the two original images and their resulting blended texture applied to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/DisjointOverMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/DisjointOverMaterial2.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/DisjointOverMaterial3.png)

## See Also

### Nodes
- [Premultiply](./premultiply.md)
  Multiplies the RGB channels of the input by the alpha channel.
- [Unpremultiply](./unpremultiply.md)
  Divides the RGB channels of the input by the alpha channel.
- [Additive Mix](./additive-mix.md)
  Adds foreground and background values.
- [Subtractive Mix](./subtractive-mix.md)
  Subtracts foreground from background values.
- [Difference](./difference.md)
  Outputs the distance between foreground and background values.
- [Burn](./burn.md)
  A blend operation that darkens the foreground layer using the background.
- [Dodge](./dodge.md)
  A blend operation that lightens the background layer depending on the foreground.
- [Screen](./screen.md)
  A blend operation that lightens areas that are darker than white.
- [Overlay](./overlay.md)
  A blend operation that multiplies dark areas and screens light areas.
- [In](./in.md)
  Outputs areas of foreground that overlap with the alpha of background.
- [Mask](./mask.md)
  Outputs areas of background that overlap with the alpha of foreground.
- [Matte](./matte.md)
  A merge operation that layers premultiplied foreground over background.
- [Out](./out.md)
  Outputs areas of foreground that do not overlap with background.
- [Over](./over.md)
  A merge operation that layers foreground over background, using the alpha of the foreground.
- [Inside](./inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/disjoint-over)*