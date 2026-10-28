# Step (RealityKit)

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Overview

0 if X < Edge, otherwise it returns 1.0

## Parameter Types

**Step (float)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Edge` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Step (vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Edge` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Step (half)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Edge` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Step (vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Edge` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Step (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Edge` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Step (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Edge` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Step (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Edge` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Step (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Edge` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Step (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Edge` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Step (vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Edge` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

## Parameter descriptions

- **`In`**: The input value.
- **`Edge`**: The deciding value to which to compare the input.

## Discussion

The Step node takes the `In` value and compares it to the `Edge` parameter. If the value is less than `Edge`, the node returns `0`. Otherwise, it returns `1`.

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
- [Saturate](./saturate.md)
  Adjusts the saturation of a color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/step-(realitykit))*