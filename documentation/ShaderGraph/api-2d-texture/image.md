# Image

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

A texture referencing a 2D image file.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Image (float)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Float |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Image (vector3f)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Vector3f |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Image (color3f)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Color3 |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Image (half)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Half |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Image (color4f)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Color4 |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Image (vector2f)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Vector2f |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Image (vector4f)**:

| Input | Type |
| --- | --- |
| `File` | AssetPath |
| `Default` | Vector4f |
| `Texture Coordinates` | Vector2f |
| `Uaddressmode` | String |
| `Vaddressmode` | String |
| `Filter Type` | String |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

## Parameter descriptions

- **`File`**: The image file to use for the texture.
- **`Default`**: The default value to use if the ​file​ reference fails to resolve.
- **`Texture Coordinates`**: The 2D coordinate at which the data is read in order to map the texture onto a surface. The default is to use the current *UV* coordinates, in which *U* is the horizontal axis and *V* is the vertical axis.
- **`Uaddressmode`**: The way that the node will handle *U* values outside of the range of `0-1`.
- **`Vaddressmode`**: The way that the node will handle *V* values outside of the range of `0-1`.
- **`Filter Type`**: The type of texture filtering the node will use.

## Discussion

The Image node creates a material from an image file. This node samples data from a single image, and maps it onto an object. The address modes for the Image node tell it how to handle *U* and *V* values outside of the normal range of `0-1`. `Uaddressmode` and `Vaddressmode`  take one of four values to determine their behavior.

- constant: Texture coordinates outside the normal range return the `Default` input.
- clamp: Texture coordinates outside the normal range are clamped to the normal range. Any values greater than `1` will be set to `1`, and any values less than `0` will be set to `0`
- periodic: Texture coordinates outside the normal range will “wrap around.” This behavior is effectively equivalent to applying modulo 1 to the coordinates.
- mirror: Texture coordinates outside the normal range will be mirrored.

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ImageAddressMode1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ImageAddressMode2.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ImageAddressMode3.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ImageAddressMode4.png)

Below is an example of a simple node graph that uses the Image node to create a material from an image:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ImageGraph.png)

Below, the resulting texture applies to a cube:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/ImageMaterial.png)

## See Also

### Nodes
- [Tiled Image](./tiled-image.md)
  Samples data from an image with provisions for offsetting and tiling in UV space.
- [UV Texture](./uv-texture.md)
  A MaterialX version of USD UV Texture reader.
- [Transform 2D](./transform-2d.md)
  A node that applies an affine transformation to a 2d input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/2d-texture/image)*