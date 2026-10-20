# Normal Map

**Framework**: ShaderGraph  
**Kind**: subscript  
**Role**: ShaderGraph Node

Transforms a normal vector from object or tangent space into world space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

**Normal Map**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Space` | String |
| `Scale` | Float |
| `Normal` | Vector3f |
| `Tangent` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

**Normal Map (vector2f Scale)**:

| Input | Type |
| --- | --- |
| `In` | Vector3f |
| `Space` | String |
| `Scale` | Vector2f |
| `Normal` | Vector3f |
| `Tangent` | Vector3f |

| Output | Type |
| --- | --- |
| `Out` | Vector3f |

#### Parameter descriptions

- **`In`**: The input vector to be transformed; the default is `(0.5, 0.5, 1.0)`.
- **`Space`**: The space from which the node transforms the normal vector. The value can either be `object` or `tangent`. The default value is `tangent`.
- **`Scale`**: A scalar multiplier for the input vector before the node transforms it. The default value is `1.0`.
- **`Normal`**: The surface normal vector. The default value is the current surface normal of world space.
- **`Tangent`**: The surface tangent vector. The default value is the current tangent vector of world space.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/normal-map)*