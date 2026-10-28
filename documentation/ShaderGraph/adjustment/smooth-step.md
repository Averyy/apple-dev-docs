# Smooth Step

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Outputs a smooth remapping from low-high to 0-1.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Smooth Step (float)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Smooth Step (vector3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Smooth Step (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Low` | Vector4f |
| `High` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Smooth Step (vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Low` | Vector2h |
| `High` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Smooth Step (color3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Smooth Step (vector3h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Smooth Step (half)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Low` | Half |
| `High` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Smooth Step (vector4h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Smooth Step (color4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Smooth Step (vector2h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Smooth Step (vector2f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Smooth Step (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Low` | Color3 |
| `High` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Smooth Step (vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Low` | Vector4h |
| `High` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Smooth Step (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Low` | Vector3f |
| `High` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Smooth Step (vector4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Smooth Step (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Low` | Vector2f |
| `High` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Smooth Step (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Low` | Color4 |
| `High` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Smooth Step (vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Low` | Vector3h |
| `High` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

## Parameter descriptions

- **`In`**: The input value to remap.
- **`Low`**: The low end value of the input range; the default value is `0.0`.
- **`High`**: The high end value of the input range; the default value is `1.0`.

## Discussion

The `Smooth Step` node outputs a smooth remapping using Hermite interpolation. Any input with a value lower than the `Low` parameter results in an output of `0`. Any input with a value higher than the `High` parameter results in an output of `1`.

## See Also

### Nodes
- [Remap](./remap.md)
  Linearly remaps incoming values from one range to another.
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
- [Saturate](./saturate.md)
  Adjusts the saturation of a color.
- [Step (RealityKit)](./step-%28realitykit%29.md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/smooth-step)*