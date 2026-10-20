# Overlay

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

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

**Overlay (float)**:

| Input | Type |
| --- | --- |
| `Foreground` | Float |
| `Background` | Float |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Overlay (color4f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Color4 |
| `Background` | Color4 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Overlay (color3f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Color3 |
| `Background` | Color3 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Overlay (half)**:

| Input | Type |
| --- | --- |
| `Foreground` | Half |
| `Background` | Half |
| `Mix` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

#### Parameter descriptions

- **`Foreground`**: The foreground input. Represented by `F` in the mathmatical equation.
- **`Background`**: The background input. Represented by `B` in the mathmatical equation.
- **`Mix`**: The weight of the blend operation. The higher the value of `Mix`, the more apparent the effect of the blend operation. The default value is `1`. Values outside of the range `0-1` produce an undefined effect outside of the node’s intended function.

#### Discussion

The `Overlay` node has one of two effects:

- If `F+B` is less than `0.5`, then the node outputs a value of `2*F*B`.
- If `F+B` is greater than or equal to `0.5`, then it outputs`1-(1-F)(1-B)`, which creates the same visual effect as the [`Screen`](./screen.md) node. Visually the node makes dark areas of the blended texture even darker and light areas of the blended texture even lighter.

Below is an example of a simple node graph that uses the `Overlay` node to blend two images together into a single material:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/OverlayGraph.png)

Below are two images and their resulting blended texture applied to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/OverlayMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ScreenMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/OverlayMaterial2.png)

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
- [Disjoint Over](./disjoint-over.md)
  A merge operation that layers foreground over background color, but assumes no overlap in partially transparent areas covered by both.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/overlay)*