# Normal Map

**Framework**: ShaderGraph  
**Kind**: subscript

Transforms a normal vector from object or tangent space into world space.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

- **`In`**: The input vector to be transformed; the default is `(0.5, 0.5, 1.0)`.
- **`Space`**: The space from which the node transforms the normal vector. The value can either be `object` or `tangent`. The default value is `tangent`.
- **`Scale`**: A scalar multiplier for the input vector before the node transforms it. The default value is `1.0`.
- **`Normal`**: The surface normal vector. The default value is the current surface normal of world space.
- **`Tangent`**: The surface tangent vector. The default value is the current tangent vector of world space.

## See Also

- [Add](math/add.md)
  Adds two values.
- [Subtract](math/subtract.md)
  Subtracts two values.
- [Multiply](math/multiply.md)
  Multiplies two values.
- [Divide](math/divide.md)
  Divides two values.
- [Modulo](math/modulo.md)
  Outputs the remaining fraction after dividing the input by a value and subtracting the integer portion.
- [Abs](math/abs.md)
  Outputs the per-channel absolute value of the input.
- [Floor](math/floor.md)
  Outputs the nearest integer value, per-channel, less than or equal to the incoming values.
- [Ceiling](math/ceiling.md)
  Outputs the nearest integer value, per-channel, greater than or equal to the incoming values.
- [Power](math/power.md)
  Raises the incoming value to an exponent.
- [Sin](math/sin.md)
  The sine of the incoming value in radians.
- [Cos](math/cos.md)
  The cosine of the incoming value in radians.
- [Tan](math/tan.md)
  The tangent of the incoming value in radians.
- [Asin](math/asin.md)
  The arcsine of the incoming value in radians.
- [Acos](math/acos.md)
  The arccosine of the incoming value in radians.
- [Atan2](math/atan2.md)
  The arctangent of the expression (iny/inx) in radians.


---

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/normal-map)*