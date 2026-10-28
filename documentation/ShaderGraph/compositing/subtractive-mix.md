# Subtractive Mix

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Subtracts foreground from background values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Overview

B - F

## Parameter Types

**Subtractive Mix (float)**:

| Input | Type |
| --- | --- |
| `Foreground` | Float |
| `Background` | Float |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Subtractive Mix (color4f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Color4 |
| `Background` | Color4 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Subtractive Mix (color3f)**:

| Input | Type |
| --- | --- |
| `Foreground` | Color3 |
| `Background` | Color3 |
| `Mix` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Subtractive Mix (half)**:

| Input | Type |
| --- | --- |
| `Foreground` | Half |
| `Background` | Half |
| `Mix` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

## Parameter descriptions

- **`Foreground`**: The foreground input, represented by `F` in the mathematical equation.
- **`Background`**: The background input, represented by `B` in the mathematical equation.
- **`Mix`**: The weight of the blend effect. The higher the `Mix`, the greater the intensity of the blend operation, and the more the effect is visually apparent. The default value is `1`. Values outside of the range `0-1` produce an undefined effect outside of the node’s intended function.

## Discussion

The `Subtractive Mix` node subtracts two inputs and uses the `Mix` input to determine the weight of the foreground in the blend, represented by the equation `B - F`. Higher values closer to `1` output a more intense subtractive mix, while lower values closer to `0` dim the effect.

Below is an example of a simple node graph that uses the subtractive mix node to blend two images into a single material:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SubtractiveMixGraph.png)

Below are two images and the resulting blended texture applied to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/MixMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/BrickTexture.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SubtractiveMixMaterial.png)

## See Also

### Nodes
- [Premultiply](./premultiply.md)
  Multiplies the RGB channels of the input by the alpha channel.
- [Unpremultiply](./unpremultiply.md)
  Divides the RGB channels of the input by the alpha channel.
- [Additive Mix](./additive-mix.md)
  Adds foreground and background values.
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
- [Inside](./inside.md)
  Multiplies a mask to all channels of the input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/compositing/subtractive-mix)*