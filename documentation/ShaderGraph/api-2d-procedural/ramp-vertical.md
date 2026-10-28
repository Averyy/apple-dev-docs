# Ramp Vertical

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A top-to-bottom linear value ramp (gradient) generator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Ramp Vertical (float)**:

| Input | Type |
| --- | --- |
| `Top` | Float |
| `Bottom` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Ramp Vertical (vector3f)**:

| Input | Type |
| --- | --- |
| `Top` | Vector3f |
| `Bottom` | Vector3f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Ramp Vertical (vector4f)**:

| Input | Type |
| --- | --- |
| `Top` | Vector4f |
| `Bottom` | Vector4f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Ramp Vertical (color4f)**:

| Input | Type |
| --- | --- |
| `Top` | Color4 |
| `Bottom` | Color4 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Ramp Vertical (vector2h)**:

| Input | Type |
| --- | --- |
| `Top` | Vector2h |
| `Bottom` | Vector2h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Ramp Vertical (vector2f)**:

| Input | Type |
| --- | --- |
| `Top` | Vector2f |
| `Bottom` | Vector2f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Ramp Vertical (color3f)**:

| Input | Type |
| --- | --- |
| `Top` | Color3 |
| `Bottom` | Color3 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Ramp Vertical (vector3h)**:

| Input | Type |
| --- | --- |
| `Top` | Vector3h |
| `Bottom` | Vector3h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Ramp Vertical (vector4h)**:

| Input | Type |
| --- | --- |
| `Top` | Vector4h |
| `Bottom` | Vector4h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Ramp Vertical (half)**:

| Input | Type |
| --- | --- |
| `Top` | Half |
| `Bottom` | Half |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Half |

## Parameter Descriptions

- **`Top`**: The top value of the interpolation.
- **`Bottom`**: The bottom value of the interpolation.
- **`Texture coordinates`**: The 2D coordinate at which the data is read for mapping the texture onto a surface. The default is to use the current UV coordinates, in which U is the horizontal axis and V is the vertical axis.

## Discussion

This node uses interpolation to create a vertical ramp or gradient from two values. Any point within the output ramp is a mix of the two values. A given point is more similar to the value that its vertical position is closer to. Below is a an example of a simple node graph that uses `Ramp Vertical` to create a color gradient:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/RampVerticalGraph.png)

The image below shows the resulting texture, along with the color values on either side:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/RampVerticalMaterial.png)

## See Also

### Nodes
- [Ramp Horizontal](./ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp 4 Corners](./ramp-4-corners.md)
  A four-point linear value ramp (gradient) generator.
- [Split Horizontal](./split-horizontal.md)
  A left-to-right split matte, split at a specified U value.
- [Split Vertical](./split-vertical.md)
  A top-to-bottom split matte, split at a specified V value.
- [Noise 2D](./noise-2d.md)
  A 2D Perlin noise generator.
- [Cellular Noise 2D](./cellular-noise-2d.md)
  A 2D cellular noise generator.
- [Worley Noise 2D](./worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/ramp-vertical)*