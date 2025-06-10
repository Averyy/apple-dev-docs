# Clamp

**Framework**: ShaderGraph  
**Kind**: subscript

Clamps the input per-channel to a specified range.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 26.0+ (Beta)
- visionOS 1.0+

#### Parameter Types

#### Parameter Descriptions

#### Discussion

The `Clamp` node restricts the range of values of an input as defined by the `Low` and `High` parameters passed into the node. The output of the `Clamp` node is the same as the `In` value if it falls within the defined range. Otherwise, the output clamps to the nearest limit, which is either the `Low` or `High` value. Use the `Clamp` node to create more predictable and controlled shader behavior for materials.

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

*[View on Apple Developer](https://developer.apple.com/documentation/shadergraph/math/clamp)*