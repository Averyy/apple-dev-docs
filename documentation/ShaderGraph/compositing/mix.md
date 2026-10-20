# Mix

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Mixes foreground and background inputs, weighting based on mix value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Overview

F * m + B(1 - m)

#### Parameter Types

**Mix (float)**:

| Input | Type |
| --- | --- |
| `Foreground` | Float |
| `Background` | Float |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Mix (color3f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Color3 |
| `Background` | Color3 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Mix (vector3h)**:

| Input | Type |
| --- | --- |
| `Foreground` | Vector3h |
| `Background` | Vector3h |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Mix (half)**:

| Input | Type |
| --- | --- |
| `Foreground` | Half |
| `Background` | Half |
| `Mix` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Mix (vector2h)**:

| Input | Type |
| --- | --- |
| `Foreground` | Vector2h |
| `Background` | Vector2h |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Mix (vector2f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Vector2f |
| `Background` | Vector2f |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Mix (color4f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Color4 |
| `Background` | Color4 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Mix (vector3f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Vector3f |
| `Background` | Vector3f |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Mix (vector4f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Vector4f |
| `Background` | Vector4f |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Mix (vector4h)**:

| Input | Type |
| --- | --- |
| `Foreground` | Vector4h |
| `Background` | Vector4h |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

#### Parameter descriptions

- **`Foreground`**: The foreground input.
- **`Background`**: The background input.
- **`Mix`**: The weight that determines what the output value is closer to. The default value is `0`. Values outside of the range `0-1` produce an undefined effect outside of the node’s intended function.

#### Discussion

The Mix node blends two input values together, represented by the equation `F * m + B(1 - m)`.  If the `Mix` value is `1`, the output is identical to the `Foreground` value. If the value is `0`, the output is identical to the `Background` value. The closer the `Mix` value is to `0` or `1`, the closer the output will be to the corresponding input. Use the Mix node to blend between two different textures and create transtions or effects, interpolate between two colors, or mix shader parameters. Below is an example of a simple node graph that uses the Mix node to blend two images together into a single material:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/MixGraph.png)

Below are the original two images and the resulting mixed texture applied to a cube with `Mix` values of `0.1`, `0.5`, and `0.9`:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/MixMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/MixMaterial2.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/MixMaterial3.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/MixMaterial4.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/MixMaterial5.png)

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/mix)*