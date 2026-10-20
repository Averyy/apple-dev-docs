# Rotate 3D

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Rotates a Vector3 (Float) about a specified unit axis vector.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Amount` | Float |
| `Axis` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

#### Parameter descriptions

- **`In`**: The vector to rotate.
- **`Amount`**: The amount of degrees to rotate the `In` vector; the default is `0`.
- **`Axis`**: The unit axis vector that the node rotates the `In` vector around; the default `(0, 1, 0)`.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/rotate-3d)*