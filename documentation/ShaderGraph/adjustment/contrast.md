# Contrast

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Increases or decreases contrast of values using a linear slope multiplier.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Contrast (float)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Amount` | Float |
| `Pivot` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Contrast (vector3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Amount` | Float |
| `Pivot` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Contrast (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Amount` | Vector2f |
| `Pivot` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Contrast (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Amount` | Color4 |
| `Pivot` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Contrast (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Amount` | Vector4f |
| `Pivot` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Contrast (vector3h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Amount` | Half |
| `Pivot` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Contrast (color4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Amount` | Float |
| `Pivot` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Contrast (half)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Amount` | Half |
| `Pivot` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Contrast (vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Amount` | Vector3h |
| `Pivot` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Contrast (vector2f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Amount` | Float |
| `Pivot` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Contrast (vector4h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Amount` | Half |
| `Pivot` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Contrast (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Amount` | Vector3f |
| `Pivot` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Contrast (vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Amount` | Vector2h |
| `Pivot` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Contrast (vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Amount` | Vector4h |
| `Pivot` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Contrast (color3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Amount` | Float |
| `Pivot` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Contrast (vector2h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Amount` | Half |
| `Pivot` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Contrast (vector4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Amount` | Float |
| `Pivot` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Contrast (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Amount` | Color3 |
| `Pivot` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

#### Parameter descriptions

- **`In`**: The input value to modify.
- **`Amount`**: The linear slope multiplier that increases or decreases the contrast. A value between `0.0` and `1.0` decreases the contrast of the `In` parameter, while a value greater than `1.0` increases it.
- **`Pivot`**: The center value of the contrast adjustment. As contrast increases, values of the `In` parameter get further away from this value. As contrast decreases, values of the `In` parameter get closer to this value.

#### Discussion

Below is an example of a node graph that uses the `Contrast` node to make a black and white arrow texture more gray and closer in color.

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ContrastGraph.png)

Below, the resulting texture applies to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ContrastMaterial.png)

In the image above, the value of `Pivot` is `0.2`, which represents a dark gray. Because the value of `Amount` is also `0.2`, the contrast of the input decreases while the color value of the texture moves closer to the `Pivot` input. As a result, the output texture of the node becomes a gray version of the original black and white arrow texture.

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
- [Range](./range.md)
  Remaps incoming values from one range to another.
- [HSV Adjust](./hsv-adjust.md)
  Adjusts the hue, saturation and value of an RGB color by a vector .
- [Saturate](./saturate.md)
  Adjusts the saturation of a color.
- [Step (RealityKit)](./step-%28realitykit%29.md)
  Outputs a 1 or a 0 depending on whether the input is greater than or less than the edge value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/adjustment/contrast)*