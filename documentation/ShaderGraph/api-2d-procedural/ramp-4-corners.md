# Ramp 4 Corners

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A four-point linear value ramp (gradient) generator.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Ramp 4 Corners (float)**:

| Input | Type |
| --- | --- |
| `Top Left` | Float |
| `Top Right` | Float |
| `Bottom Left` | Float |
| `Bottom Right` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Ramp 4 Corners (color3f)**:

| Input | Type |
| --- | --- |
| `Top Left` | Color3 |
| `Top Right` | Color3 |
| `Bottom Left` | Color3 |
| `Bottom Right` | Color3 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Ramp 4 Corners (vector3f)**:

| Input | Type |
| --- | --- |
| `Top Left` | Vector3f |
| `Top Right` | Vector3f |
| `Bottom Left` | Vector3f |
| `Bottom Right` | Vector3f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Ramp 4 Corners (half)**:

| Input | Type |
| --- | --- |
| `Top Left` | Half |
| `Top Right` | Half |
| `Bottom Left` | Half |
| `Bottom Right` | Half |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Ramp 4 Corners (vector4h)**:

| Input | Type |
| --- | --- |
| `Top Left` | Vector4h |
| `Top Right` | Vector4h |
| `Bottom Left` | Vector4h |
| `Bottom Right` | Vector4h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Ramp 4 Corners (vector3h)**:

| Input | Type |
| --- | --- |
| `Top Left` | Vector3h |
| `Top Right` | Vector3h |
| `Bottom Left` | Vector3h |
| `Bottom Right` | Vector3h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Ramp 4 Corners (color4f)**:

| Input | Type |
| --- | --- |
| `Top Left` | Color4 |
| `Top Right` | Color4 |
| `Bottom Left` | Color4 |
| `Bottom Right` | Color4 |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Ramp 4 Corners (vector4f)**:

| Input | Type |
| --- | --- |
| `Top Left` | Vector4f |
| `Top Right` | Vector4f |
| `Bottom Left` | Vector4f |
| `Bottom Right` | Vector4f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Ramp 4 Corners (vector2f)**:

| Input | Type |
| --- | --- |
| `Top Left` | Vector2f |
| `Top Right` | Vector2f |
| `Bottom Left` | Vector2f |
| `Bottom Right` | Vector2f |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Ramp 4 Corners (vector2h)**:

| Input | Type |
| --- | --- |
| `Top Left` | Vector2h |
| `Top Right` | Vector2h |
| `Bottom Left` | Vector2h |
| `Bottom Right` | Vector2h |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

## Parameter descriptions

- **`Top left`**: The top-left value of the four-point interpolation.
- **`Top right`**: The top-right value of the four-point interpolation.
- **`Bottom left`**: The bottom-left value of the four-point interpolation.
- **`Bottom right`**: The bottom-right value of the four-point interpolation.
- **`Texture Coordinates`**: The 2D coordinate at which the data is read for mapping the texture onto a surface. The default is to use the current UV coordinates, in which U is the horizontal axis and V is the vertical axis.

## Discussion

This node uses bilinear interpolation to create a ramp from four corner values. Any point within the output ramp is a mix of one of the four corner values. A given point is more similar to a corner value the closer its position is to that corner. Below is a an example of a simple node graph that uses `Ramp 4 Corners` to create a gradient with four different colors:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Ramp4Graph.png)

The image below shows the resulting texture along with the color values on each corner:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Ramp4Material.png)

## See Also

### Nodes
- [Ramp Horizontal](./ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](./ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/ramp-4-corners)*