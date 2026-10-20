# Split Horizontal

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A left-to-right split matte, split at a specified U value.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Split Horizontal (float)**:

| Input | Type |
| --- | --- |
| `Left` | Float |
| `Right` | Float |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Split Horizontal (color3f)**:

| Input | Type |
| --- | --- |
| `Left` | Color3 |
| `Right` | Color3 |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Split Horizontal (vector3f)**:

| Input | Type |
| --- | --- |
| `Left` | Vector3f |
| `Right` | Vector3f |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Split Horizontal (vector2f)**:

| Input | Type |
| --- | --- |
| `Left` | Vector2f |
| `Right` | Vector2f |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Split Horizontal (color4f)**:

| Input | Type |
| --- | --- |
| `Left` | Color4 |
| `Right` | Color4 |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Split Horizontal (half)**:

| Input | Type |
| --- | --- |
| `Left` | Half |
| `Right` | Half |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Split Horizontal (vector3h)**:

| Input | Type |
| --- | --- |
| `Left` | Vector3h |
| `Right` | Vector3h |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Split Horizontal (vector2h)**:

| Input | Type |
| --- | --- |
| `Left` | Vector2h |
| `Right` | Vector2h |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Split Horizontal (vector4f)**:

| Input | Type |
| --- | --- |
| `Left` | Vector4f |
| `Right` | Vector4f |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Split Horizontal (vector4h)**:

| Input | Type |
| --- | --- |
| `Left` | Vector4h |
| `Right` | Vector4h |
| `Center` | Float |
| `Texture Coordinates` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

#### Parameter descriptions

- **`Left`**: The value of the left side of the split.
- **`Right`**: The value of the right side of the split.
- **`Center`**: The V value at which the output is split. Everything above this value is equal to the `Top` input; everything below this value is equal to the `Bottom` input. This parameter ranges between `0` and `1`.
- **`Texture Coordinates`**: The 2D coordinate at which the data is read for mapping the texture onto a surface. The default uses the current UV coordinates, in which U is the horizontal axis, and V is the vertical axis.

#### Discussion

This node creates two distinct regions along the horizontal axis. The value of the `Center` input determines these regions. A value of `0` establishes the center at the left-most position, causing the output to always be equal to the `Right` input. A value of `1` establishes the center at the right-most position. Below is a an example of a simple node graph that uses `Split Horizontal` to create a split color:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SplitHorizontalGraph.png)

By editing the center value, you change the texture to show a larger left or right region. The image below shows the resulting textures:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SplitHorizontalMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SplitHorizontalMaterial2.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/SplitHorizontalMaterial3.png)

## See Also

### Nodes
- [Ramp Horizontal](./ramp-horizontal.md)
  A left-to-right linear value ramp (gradient) generator.
- [Ramp Vertical](./ramp-vertical.md)
  A top-to-bottom linear value ramp (gradient) generator.
- [Ramp 4 Corners](./ramp-4-corners.md)
  A four-point linear value ramp (gradient) generator.
- [Split Vertical](./split-vertical.md)
  A top-to-bottom split matte, split at a specified V value.
- [Noise 2D](./noise-2d.md)
  A 2D Perlin noise generator.
- [Cellular Noise 2D](./cellular-noise-2d.md)
  A 2D cellular noise generator.
- [Worley Noise 2D](./worley-noise-2d.md)
  A 2D Worley noise generator.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-procedural/split-horizontal)*