# Clamp

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Clamps the input per-channel to a specified range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Clamp (float)**:

| Input | Type |
| --- | --- |
| `In` | Float |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Float |

**Clamp (vector3f)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Low` | Vector3f |
| `High` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Clamp (vector2f)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Low` | Vector2f |
| `High` | Vector2f |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Clamp (vector4f)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Low` | Vector4f |
| `High` | Vector4f |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

**Clamp (color4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Clamp (vector3h)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Low` | Vector3h |
| `High` | Vector3h |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Clamp (half)**:

| Input | Type |
| --- | --- |
| `In` | Half |
| `Low` | Half |
| `High` | Half |

| Output | Type |
| --- | --- |
| `Out` | Half |

**Clamp (vector2h)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Low` | Vector2h |
| `High` | Vector2h |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Clamp (color3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Clamp (vector3f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Clamp (vector2h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector2h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2h |

**Clamp (vector4h)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Low` | Vector4h |
| `High` | Vector4h |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Clamp (vector3h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector3h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector3h |

**Clamp (vector4h FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector4h |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4h |

**Clamp (color3f)**:

| Input | Type |
| --- | --- |
| `In` | Color3 |
| `Low` | Color3 |
| `High` | Color3 |

| Output | Type |
| --- | --- |
| `Out` | Color3 |

**Clamp (vector2f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector2f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector2f |

**Clamp (color4f)**:

| Input | Type |
| --- | --- |
| `In` | Color4 |
| `Low` | Color4 |
| `High` | Color4 |

| Output | Type |
| --- | --- |
| `Out` | Color4 |

**Clamp (vector4f FA)**:

| Input | Type |
| --- | --- |
| `In` | Vector4f |
| `Low` | Float |
| `High` | Float |

| Output | Type |
| --- | --- |
| `Out` | Vector4f |

#### Parameter descriptions

- **`In`**: The input to clamp.
- **`Low`**: The low end of the clamp range.
- **`High`**: The high end of the clamp range.

#### Discussion

The `Clamp` node restricts the range of values of an input as defined by the `Low` and `High` parameters passed into the node. The output of the `Clamp` node is the same as the `In` value if it falls within the defined range. Otherwise, the output clamps to the nearest limit, which is either the `Low` or `High` value. Use the `Clamp` node to create more predictable and controlled shader behavior for materials.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/clamp)*