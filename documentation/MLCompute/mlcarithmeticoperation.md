# MLCArithmeticOperation

**Framework**: ML Compute  
**Kind**: enum

Constants that describe an arithmetic operation.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCArithmeticOperation
```

## Topics

### Basic Operations
- [MLCArithmeticOperation.add](mlcarithmeticoperation/add.md)
  Calculates the element-wise sum of the inputs.
- [MLCArithmeticOperation.subtract](mlcarithmeticoperation/subtract.md)
  Calculates the element-wise difference between the inputs.
- [MLCArithmeticOperation.multiply](mlcarithmeticoperation/multiply.md)
  Calculates the element-wise product of the inputs.
- [MLCArithmeticOperation.multiplyNoNaN](mlcarithmeticoperation/multiplynonan.md)
  Calculates the element-wise product of the inputs, and returns `0` when the result isn’t a number or infinity.
- [MLCArithmeticOperation.divide](mlcarithmeticoperation/divide.md)
  Calculates the element-wise division of the inputs.
- [MLCArithmeticOperation.divideNoNaN](mlcarithmeticoperation/dividenonan.md)
  Calculates the element-wise division of the inputs, and returns `0` if the denominator is `0`.
- [MLCArithmeticOperation.min](mlcarithmeticoperation/min.md)
  Calculates the element-wise minimum of the inputs.
- [MLCArithmeticOperation.max](mlcarithmeticoperation/max.md)
  Calculates the element-wise maximum the inputs.
### Rounding Operations
- [MLCArithmeticOperation.floor](mlcarithmeticoperation/floor.md)
  Calculates the element-wise floor of the inputs.
- [MLCArithmeticOperation.round](mlcarithmeticoperation/round.md)
  Calculates the element-wise rounding of the inputs.
- [MLCArithmeticOperation.ceil](mlcarithmeticoperation/ceil.md)
  Calculates the element-wise ceiling of the inputs.
### Trigonometric Operations
- [MLCArithmeticOperation.sin](mlcarithmeticoperation/sin.md)
  Calculates the element-wise sine of the input.
- [MLCArithmeticOperation.cos](mlcarithmeticoperation/cos.md)
  Calculates the element-wise cosine of the input.
- [MLCArithmeticOperation.tan](mlcarithmeticoperation/tan.md)
  Calculates the element-wise tangent of the input.
- [MLCArithmeticOperation.asin](mlcarithmeticoperation/asin.md)
  Calculates the element-wise inverse sine of the input.
- [MLCArithmeticOperation.acos](mlcarithmeticoperation/acos.md)
  Calculates the element-wise inverse cosine of the input.
- [MLCArithmeticOperation.atan](mlcarithmeticoperation/atan.md)
  Calculates the element-wise inverse tangent of the input.
- [MLCArithmeticOperation.sinh](mlcarithmeticoperation/sinh.md)
  Calculates the element-wise hyperbolic sine of the input.
- [MLCArithmeticOperation.cosh](mlcarithmeticoperation/cosh.md)
  Calculates the element-wise hyperbolic cosine of the input.
- [MLCArithmeticOperation.tanh](mlcarithmeticoperation/tanh.md)
  Calculates the element-wise hyperbolic tangent of the input.
- [MLCArithmeticOperation.asinh](mlcarithmeticoperation/asinh.md)
  Calculates the element-wise inverse hyperbolic sine of the input.
- [MLCArithmeticOperation.acosh](mlcarithmeticoperation/acosh.md)
  Calculates the element-wise inverse hyperbolic cosine of the input.
- [MLCArithmeticOperation.atanh](mlcarithmeticoperation/atanh.md)
  Calculates the element-wise inverse hyperbolic tangent of the input.
### Advanced Operations
- [MLCArithmeticOperation.sqrt](mlcarithmeticoperation/sqrt.md)
  Calculates the element-wise square root of the input.
- [MLCArithmeticOperation.rsqrt](mlcarithmeticoperation/rsqrt.md)
  Calculates the element-wise reciprocal of the square root of the input.
- [MLCArithmeticOperation.pow](mlcarithmeticoperation/pow.md)
  Calculates the element-wise first input raised to the power of the second input.
- [MLCArithmeticOperation.exp](mlcarithmeticoperation/exp.md)
  Calculates the element-wise result of the exponent raised to the power of the input.
- [MLCArithmeticOperation.exp2](mlcarithmeticoperation/exp2.md)
  Calculates the element-wise result of the number 2 raised to the power of the input.
- [MLCArithmeticOperation.log](mlcarithmeticoperation/log.md)
  Calculates the element-wise natural logarithm of the input.
- [MLCArithmeticOperation.log2](mlcarithmeticoperation/log2.md)
  Calculates the element-wise base 2 logarithm of the input.
### Debugging
- [var debugDescription: String](mlcarithmeticoperation/debugdescription.md)
  A textual description of the arithmetic operation you use for debugging.
### Initializers
- [init?(rawValue: Int32)](mlcarithmeticoperation/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [convenience init(operation: MLCArithmeticOperation)](mlcarithmeticlayer/init(operation:).md)
  Creates an arithmetic layer with the operation you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcarithmeticoperation)*