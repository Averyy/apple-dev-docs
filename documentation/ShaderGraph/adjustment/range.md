# Range

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Remaps incoming values from one range to another.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Range (float)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `In Low` | Float |
| `In High` | Float |
| `Gamma` | Float |
| `Out Low` | Float |
| `Out High` | Float |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Range (color3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `In Low` | Float |
| `In High` | Float |
| `Gamma` | Float |
| `Out Low` | Float |
| `Out High` | Float |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Range (vector3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `In Low` | Float |
| `In High` | Float |
| `Gamma` | Float |
| `Out Low` | Float |
| `Out High` | Float |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Range (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `In Low` | Color4 |
| `In High` | Color4 |
| `Gamma` | Color4 |
| `Out Low` | Color4 |
| `Out High` | Color4 |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Range (vector4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `In Low` | Float |
| `In High` | Float |
| `Gamma` | Float |
| `Out Low` | Float |
| `Out High` | Float |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Range (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `In Low` | Color3 |
| `In High` | Color3 |
| `Gamma` | Color3 |
| `Out Low` | Color3 |
| `Out High` | Color3 |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Range (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `In Low` | Vector3f |
| `In High` | Vector3f |
| `Gamma` | Vector3f |
| `Out Low` | Vector3f |
| `Out High` | Vector3f |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Range (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `In Low` | Vector4f |
| `In High` | Vector4f |
| `Gamma` | Vector4f |
| `Out Low` | Vector4f |
| `Out High` | Vector4f |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Range (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `In Low` | Vector2f |
| `In High` | Vector2f |
| `Gamma` | Vector2f |
| `Out Low` | Vector2f |
| `Out High` | Vector2f |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Range (color4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `In Low` | Float |
| `In High` | Float |
| `Gamma` | Float |
| `Out Low` | Float |
| `Out High` | Float |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Range (vector2f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `In Low` | Float |
| `In High` | Float |
| `Gamma` | Float |
| `Out Low` | Float |
| `Out High` | Float |
| `Do Clamp` | Bool |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

## Parameter descriptions

- **`In`**: The input value to remap.
- **`In Low`**: The low-end value of the input range; the default is `0.0`.
- **`In High`**: The high-end value of the input range; the default is `1.0`.
- **`Gamma`**: The inverse exponent to apply to the input value. The inverse exponent is applied after first mapping the input range to the range `0..1`. The default is `1.0`.
- **`Out Low`**: The low-end value of the output range. The default is `0.0`.
- **`Out High`**: The high-end value of the output range. The default is `1.0`.
- **`Do Clamp`**: The Boolean value that indicates if the output is clamped. If `true`, the output clamps to the range defined by the `Out Low` and `Out High` parameters. The default is `False`.

## Discussion

The `Range` node takes a range of incoming values and converts them to another range. The node also provides the option to apply a gamma correction, which occurs in the middle of the transformation process. The gamma value is the inverse exponent the node applies to the  incoming values. For example, a value of `2` raises the incoming values to the power of `1/2`, effectively calculating the square root. The node also provides the option to clamp the output, which means any values below the `Out Low` parameter are set to the value of `Out Low`, and any values above the `Out High` parameter are set to value of `Out High`.

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
- [HSV Adjust](./hsv-adjust.md)
  Adjusts the hue, saturation and value of an RGB color by a vector .
- [Saturate](./saturate.md)
  Adjusts the saturation of a color.
- [Step (RealityKit)](./step-%28realitykit%29.md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/range)*