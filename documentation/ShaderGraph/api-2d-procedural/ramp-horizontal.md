# Ramp Horizontal

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A left-to-right linear value ramp (gradient) generator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Ramp Horizontal (float)**:

| Input | Type |
| --- | --- |
| `Left` | Float |
| `Right` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Ramp Horizontal (vector4f)**:

| Input | Type |
| --- | --- |
| `Left` | Vector4f |
| `Right` | Vector4f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Ramp Horizontal (vector2h)**:

| Input | Type |
| --- | --- |
| `Left` | Vector2h |
| `Right` | Vector2h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Ramp Horizontal (vector4h)**:

| Input | Type |
| --- | --- |
| `Left` | Vector4h |
| `Right` | Vector4h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Ramp Horizontal (vector3f)**:

| Input | Type |
| --- | --- |
| `Left` | Vector3f |
| `Right` | Vector3f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Ramp Horizontal (vector2f)**:

| Input | Type |
| --- | --- |
| `Left` | Vector2f |
| `Right` | Vector2f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Ramp Horizontal (color4f)**:

| Input | Type |
| --- | --- |
| `Left` | Color4 |
| `Right` | Color4 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Ramp Horizontal (color3f)**:

| Input | Type |
| --- | --- |
| `Left` | Color3 |
| `Right` | Color3 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Ramp Horizontal (half)**:

| Input | Type |
| --- | --- |
| `Left` | Half |
| `Right` | Half |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Ramp Horizontal (vector3h)**:

| Input | Type |
| --- | --- |
| `Left` | Vector3h |
| `Right` | Vector3h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

## Parameter descriptions

- **`Left`**: The left value of the interpolation.
- **`Right`**: The right value of the interpolation.
- **`Texture Coordinates`**: The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is to use the current UV coordinates, in which U is the horizontal axis and V is the vertical axis.

## Discussion

This node uses interpolation to create a horizontal ramp or gradient from two values. Any point within the output ramp is a mix of the two values. A given point is more similar to the value that its horizontal position is closer to. Below is a an example of a simple node graph that uses `Ramp Horizontal` to create a color gradient:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/RampHorizontalGraph.png)

The image below shows the resulting texture, along with the color values on either side:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/RampHorizontalMaterial.png)

## See Also

### Nodes
- [Ramp Vertical](./ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/ramp-horizontal)*