# Sign

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

The per-channel sign of the input value: -1 for negative, +1 for positive, 0 for zero.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

## Parameter Types

**Sign (float)**:

| Input | Type |
| --- | --- |
| `In` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Sign (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Sign (vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Sign (half)**:

| Input | Type |
| --- | --- |
| `In` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Sign (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Sign (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Sign (vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Sign (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Sign (vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Sign (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/sign)*