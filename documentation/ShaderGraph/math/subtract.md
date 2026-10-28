# Subtract

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Subtracts two values.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Subtract (float)**:

| Input | Type |
| --- | --- |
| `In 1` | Float |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Subtract (color4f)**:

| Input | Type |
| --- | --- |
| `In 1` | Color4 |
| `In 2` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Subtract (vector3f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector3f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Subtract (matrix2x2f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Matrix2x2f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Matrix2x2f |

**Subtract (vector2f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector2f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Subtract (vector3f)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector3f |
| `In 2` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Subtract (matrix3x3f)**:

| Input | Type |
| --- | --- |
| `In 1` | Matrix3x3f |
| `In 2` | Matrix3x3f |

| Output | Type |
| --- | --- |
| `Out` | Matrix3x3f |

**Subtract (vector4f)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector4f |
| `In 2` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Subtract (matrix4x4f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Matrix4x4f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Matrix4x4f |

**Subtract (matrix2x2f)**:

| Input | Type |
| --- | --- |
| `In 1` | Matrix2x2f |
| `In 2` | Matrix2x2f |

| Output | Type |
| --- | --- |
| `Out` | Matrix2x2f |

**Subtract (vector3h)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector3h |
| `In 2` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Subtract (color3f)**:

| Input | Type |
| --- | --- |
| `In 1` | Color3 |
| `In 2` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Subtract (color3f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Color3 |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Subtract (vector2h)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector2h |
| `In 2` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Subtract (vector2f)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector2f |
| `In 2` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Subtract (vector2h - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector2h |
| `In 2` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Subtract (vector3h - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector3h |
| `In 2` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Subtract (vector4h)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector4h |
| `In 2` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Subtract (matrix4x4f)**:

| Input | Type |
| --- | --- |
| `In 1` | Matrix4x4f |
| `In 2` | Matrix4x4f |

| Output | Type |
| --- | --- |
| `Out` | Matrix4x4f |

**Subtract (matrix3x3f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Matrix3x3f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Matrix3x3f |

**Subtract (half)**:

| Input | Type |
| --- | --- |
| `In 1` | Half |
| `In 2` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Subtract (vector4h - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector4h |
| `In 2` | Half |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Subtract (color4f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Color4 |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Subtract (vector4f - float)**:

| Input | Type |
| --- | --- |
| `In 1` | Vector4f |
| `In 2` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

## See Also

### Nodes
- [Add](./add.md)
  Adds two values.
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
- [Square Root](./square-root.md)
  The square root of the incoming value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/subtract)*