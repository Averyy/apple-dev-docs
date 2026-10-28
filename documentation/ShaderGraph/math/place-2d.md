# Place 2D

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Transforms UV texture coordinates for 2D texture placement.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

| Input | Type |
| --- | --- |
| `Texture Coordinates` | Vector2f |
| `Pivot` | Vector2f |
| `Scale` | Vector2f |
| `Rotate` | Float |
| `Offset` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

## Parameter descriptions

- **`Texture Coordinates`**: The input texture coordinates to transform. The default value is the current surface texture coordinates with an index of `0`.
- **`Pivot`**: The pivot point for scaling and rotating the texture coordinates. The node subtracts this value from U and V before it applies the scale or rotation. The node then adds this value back later.
- **`Scale`**: The value by which to scale the texture coordinates. The node divides the U and V coordinates by this value. The default is `(1,1)`.
- **`Rotate`**: The number of degrees to rotate the texture coordinates. A postive value rotates the texture coordinates by that many degrees counterclockwise and the resulting image clockwise. A negative value rotates the texture coordinates by that many degrees clockwise and the resulting image counterclockwise. The default value is `0`.
- **`Offset`**: The value to offset the position of the texture coordinates. The node subtracts this value from the texture coordinates after scaling and rotating it, and adding back the pivot. The default is `(0,0)`.

## Discussion

Use the `Place 2D` node to transform texture coordinates and apply these basic transformations to textures. Below is an example of a simple node graph that uses the `Place 2D` node to transform texture coordinates before passing them to an image node:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Place2dGraph.png)

The incoming texture coordinates transform in three ways; they are:

- scaled down to half the size
- rotated 180 degrees
- offset by `0.5` in both the U and V directions. For the scale and rotation, the pivot point is set to `(0.5, 0.5)`. Because texture coordinates generally range from `(0-1)`, this means the scale and rotation are done from the center point of the image.

Below is the original image and the texture with the transformation applied:

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Place2dMaterial1.png)

![](https://developer.apple.com/tutorials/images/ShaderGraph-Docs/Place2dMaterial2.png)

## See Also

### Nodes
- [Add](./add.md)
  Adds two values.
- [Subtract](./subtract.md)
  Subtracts two values.
- [Multiply](./multiply.md)
  Multiplies two values.
- [Divide](./divide.md)
  Divides two values.
- [Modulo](./modulo.md)
  Outputs the remaining fraction after dividing the input by a value and subtracting the integer portion.
- [Abs](./abs.md)
  Outputs the per-channel absolute value of the input.
- [Floor](./floor.md)
  Outputs the nearest integer value, per-channel, less than or equal to the incoming values.
- [Ceiling](./ceiling.md)
  Outputs the nearest integer value, per-channel, greater than or equal to the incoming values.
- [Power](./power.md)
  Raises the incoming value to an exponent.
- [Sin](./sin.md)
  The sine of the incoming value in radians.
- [Cos](./cos.md)
  The cosine of the incoming value in radians.
- [Tan](./tan.md)
  The tangent of the incoming value in radians.
- [Asin](./asin.md)
  The arcsine of the incoming value in radians.
- [Acos](./acos.md)
  The arccosine of the incoming value in radians.
- [Atan2](./atan2.md)
  The arctangent of the expression (iny/inx) in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/place-2d)*