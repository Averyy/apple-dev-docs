# Transform Matrix

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Transforms a vector by a matrix.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Transform Matrix (vector2f matrix3x3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Mat` | Matrix3x3f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Transform Matrix (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Mat` | Matrix4x4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Transform Matrix (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Mat` | Matrix2x2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Transform Matrix (vector3f matrix4x4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Mat` | Matrix4x4f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Transform Matrix (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Mat` | Matrix3x3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

## Parameter descriptions

- **`In`**: The vector to transform. This node appends an addtional component onto the `In` vector with a value of `1.0` to make the vector match the dimensions of the `Mat` matrix. This additional compenent is removed after the transformation completes.
- **`Mat`**: The matrix by which to transform the `In` vector; the default is the identity matrix.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/transform-matrix)*