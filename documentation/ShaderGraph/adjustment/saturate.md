# Saturate

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Adjusts the saturation of a color.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Saturate (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Amount` | Float |
| `Luma Coefficients` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Saturate (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Amount` | Float |
| `Luma Coefficients` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

#### Parameter descriptions

- **`In`**: The input color to adjust the saturation of.
- **`Amount`**: The multiplier to apply to the saturation; the default value is `1.0`.
- **`Luma Coefficients`**: The luma coefficients of the color space. The possible values for this node are the luma coefficients for the color spaces `acescg`, `rec202/rec2100`, or `rec709`. The default value is the luma coefficients for `acescg`, which are `(0.2722287, 0.6740818, 0.0536895)`.

#### Discussion

The `Saturate` node performs a linear interpolation between the incoming color value and the luminance of the incoming color value. Setting the value of the `Amount` parameter to `0` adjusts the output to a grayscale of the input equal to the value that the [`Luminance`](./luminance.md) outputs.

> **Note**: The effect of this node isn’t equivalent to adjusting saturation with the [`HSV Adjust`](./hsv-adjust.md) node. The `Saturate` node takes into account a colorspace when processing its modifications.

Below is an example of a simple node graph that uses the Saturate node to modify the saturation of an image:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SaturateGraph.png)

Below, the resulting texture applies to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/BrickTexture.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SaturateMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SaturateMaterial2.png)

## See Also

### Nodes
- [Remap](./remap.md)
  Linearly remaps incoming values from one range to another.
- [Smooth Step](./smooth-step.md)
  Outputs a smooth remapping from low-high to 0-1.
- [Luminance](./luminance.md)
  Outputs a grayscale value containing the luminance of the incoming RGB color in all color channels.
- [RGB to HSV](./rgb-to-hsv.md)
  Converts a color from RGB to HSV space.
- [HSV to RGB](./hsv-to-rgb.md)
  Converts a color from HSV to RGB space.
- [Contrast](./contrast.md)
  Increases or decreases contrast of values using a linear slope multiplier.
- [Range](./range.md)
  Remaps incoming values from one range to another.
- [HSV Adjust](./hsv-adjust.md)
  Adjusts the hue, saturation and value of an RGB color by a vector .
- [Step (RealityKit)](./step-%28realitykit%29.md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/saturate)*