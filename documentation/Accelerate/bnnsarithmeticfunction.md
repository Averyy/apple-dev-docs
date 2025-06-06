# BNNSArithmeticFunction

**Framework**: Accelerate  
**Kind**: struct

Constants that define arithmetic operations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSArithmeticFunction
```

## Topics

### Unary Arithmetic Functions
- [var BNNSArithmeticCeil: BNNSArithmeticFunction](bnnsarithmeticceil.md)
  An operation that calculates the element-wise ceiling of its input.
- [var BNNSArithmeticFloor: BNNSArithmeticFunction](bnnsarithmeticfloor.md)
  An operation that calculates the element-wise floor of its input.
- [var BNNSArithmeticSquareRoot: BNNSArithmeticFunction](bnnsarithmeticsquareroot.md)
  An operation that calculates the element-wise square root of its input.
- [var BNNSArithmeticReciprocalSquareRoot: BNNSArithmeticFunction](bnnsarithmeticreciprocalsquareroot.md)
  An operation that calculates the element-wise reciprocal square root of its input.
- [var BNNSArithmeticRound: BNNSArithmeticFunction](bnnsarithmeticround.md)
  An operation that calculates the element-wise rounding of its input.
- [var BNNSArithmeticAbs: BNNSArithmeticFunction](bnnsarithmeticabs.md)
  An operation that calculates the element-wise absolute of its input.
- [var BNNSArithmeticErf: BNNSArithmeticFunction](bnnsarithmeticerf.md)
  An operation that calculates the element-wise error function of its input.
- [var BNNSArithmeticNegate: BNNSArithmeticFunction](bnnsarithmeticnegate.md)
  An operation that calculates the element-wise negation of its input.
- [var BNNSArithmeticReciprocal: BNNSArithmeticFunction](bnnsarithmeticreciprocal.md)
  An operation that calculates the element-wise reciprocal of its input.
- [var BNNSArithmeticSign: BNNSArithmeticFunction](bnnsarithmeticsign.md)
  An operation that calculates the element-wise sign of its input.
- [var BNNSArithmeticSquare: BNNSArithmeticFunction](bnnsarithmeticsquare.md)
  An operation that calculates the element-wise square of its input.
### Binary Arithmetic Functions
- [var BNNSArithmeticAdd: BNNSArithmeticFunction](bnnsarithmeticadd.md)
  An operation that calculates the element-wise sum of its two inputs.
- [var BNNSArithmeticSubtract: BNNSArithmeticFunction](bnnsarithmeticsubtract.md)
  An operation that calculates the element-wise difference of its two inputs.
- [var BNNSArithmeticDivide: BNNSArithmeticFunction](bnnsarithmeticdivide.md)
  An operation that calculates the element-wise division of its two inputs.
- [var BNNSArithmeticDivideNoNaN: BNNSArithmeticFunction](bnnsarithmeticdividenonan.md)
  An operation that calculates the element-wise division of its two inputs and returns zero if the divisor is zero, even if the first input is NaN or infinity.
- [var BNNSArithmeticMultiply: BNNSArithmeticFunction](bnnsarithmeticmultiply.md)
  An operation that calculates the element-wise product of its two inputs.
- [var BNNSArithmeticMultiplyNoNaN: BNNSArithmeticFunction](bnnsarithmeticmultiplynonan.md)
  An operation that calculates the element-wise product of its two inputs and returns zero, even if the first input is NaN or infinity.
- [var BNNSArithmeticPow: BNNSArithmeticFunction](bnnsarithmeticpow.md)
  An operation that calculates the element-wise first input raised to the power of its second input.
- [var BNNSArithmeticMaximum: BNNSArithmeticFunction](bnnsarithmeticmaximum.md)
  An operation that calculates the element-wise maximum of its two inputs.
- [var BNNSArithmeticMinimum: BNNSArithmeticFunction](bnnsarithmeticminimum.md)
  An operation that calculates the element-wise minimum of its two inputs.
- [var BNNSArithmeticFloorDivide: BNNSArithmeticFunction](bnnsarithmeticfloordivide.md)
  An operation that calculates the element-wise floor division of its inputs.
- [var BNNSArithmeticTruncDivide: BNNSArithmeticFunction](bnnsarithmetictruncdivide.md)
  An operation that calculates the element-wise truncated division of its inputs.
- [var BNNSArithmeticTruncRemainder: BNNSArithmeticFunction](bnnsarithmetictruncremainder.md)
  An operation that calculates the element-wise remainder of truncated division of its inputs.
### Ternary Arithmetic Functions
- [var BNNSArithmeticMultiplyAdd: BNNSArithmeticFunction](bnnsarithmeticmultiplyadd.md)
  An operation that calculates the element-wise fused multiply-add of its three inputs.
- [var BNNSArithmeticSelect: BNNSArithmeticFunction](bnnsarithmeticselect.md)
  An operation that selects elements from either its second or third input based on the corresponding value of its first input.
### Exponential and Logarithmic Functions
- [var BNNSArithmeticExp: BNNSArithmeticFunction](bnnsarithmeticexp.md)
  An operation that calculates the element-wise result of  raised to the power of its input.
- [var BNNSArithmeticExp2: BNNSArithmeticFunction](bnnsarithmeticexp2.md)
  An operation that calculates the element-wise result of 2 raised to the power of its input.
- [var BNNSArithmeticLog: BNNSArithmeticFunction](bnnsarithmeticlog.md)
  An operation that calculates the element-wise natural logarithm of its input.
- [var BNNSArithmeticLog2: BNNSArithmeticFunction](bnnsarithmeticlog2.md)
  An operation that calculates the element-wise base 2 logarithm of its input.
### Trigonometric Functions
- [var BNNSArithmeticAcos: BNNSArithmeticFunction](bnnsarithmeticacos.md)
  An operation that calculates the element-wise inverse cosine of its input.
- [var BNNSArithmeticAcosh: BNNSArithmeticFunction](bnnsarithmeticacosh.md)
  An operation that calculates the element-wise inverse hyperbolic cosine of its input.
- [var BNNSArithmeticAsin: BNNSArithmeticFunction](bnnsarithmeticasin.md)
  An operation that calculates the element-wise inverse sine of its input.
- [var BNNSArithmeticAsinh: BNNSArithmeticFunction](bnnsarithmeticasinh.md)
  An operation that calculates the element-wise inverse hyperbolic sine of its input.
- [var BNNSArithmeticAtan: BNNSArithmeticFunction](bnnsarithmeticatan.md)
  An operation that calculates the element-wise inverse tangent of its input.
- [var BNNSArithmeticAtanh: BNNSArithmeticFunction](bnnsarithmeticatanh.md)
  An operation that calculates the element-wise inverse hyperbolic tangent of its input.
- [var BNNSArithmeticCos: BNNSArithmeticFunction](bnnsarithmeticcos.md)
  An operation that calculates the element-wise cosine of its input.
- [var BNNSArithmeticCosh: BNNSArithmeticFunction](bnnsarithmeticcosh.md)
  An operation that calculates the element-wise hyperbolic cosine of its input.
- [var BNNSArithmeticSin: BNNSArithmeticFunction](bnnsarithmeticsin.md)
  An operation that calculates the element-wise sine of its input.
- [var BNNSArithmeticSinh: BNNSArithmeticFunction](bnnsarithmeticsinh.md)
  An operation that calculates the element-wise hyperbolic sine of its input.
- [var BNNSArithmeticTan: BNNSArithmeticFunction](bnnsarithmetictan.md)
  An operation that calculates the element-wise tangent of its input.
- [var BNNSArithmeticTanh: BNNSArithmeticFunction](bnnsarithmetictanh.md)
  An operation that calculates the element-wise hyperbolic tangent of its input.
### Raw Values
- [var rawValue: UInt32](bnnsarithmeticfunction/rawvalue.md)
- [init(UInt32)](bnnsarithmeticfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnsarithmeticfunction/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [class UnaryArithmeticLayer](bnns/unaryarithmeticlayer.md)
  A layer object that wraps a unary arithmetic filter and manages its deinitialization.
- [class BinaryArithmeticLayer](bnns/binaryarithmeticlayer.md)
  A layer object that wraps a binary arithmetic filter and manages its deinitialization.
- [class TernaryArithmeticLayer](bnns/ternaryarithmeticlayer.md)
  A layer object that wraps a ternary arithmetic filter and manages its deinitialization.
- [struct BNNSDescriptorType](bnnsdescriptortype.md)
  Constants that describe the input and output types of an arithmetic operation.
- [struct BNNSArithmeticUnary](bnnsarithmeticunary.md)
  A structure that contains the input and output of an arithmetic operation with a single input.
- [struct BNNSArithmeticBinary](bnnsarithmeticbinary.md)
  A structure that contains the inputs and output of an arithmetic operation with two inputs.
- [struct BNNSArithmeticTernary](bnnsarithmeticternary.md)
  A structure that contains the inputs and output of an arithmetic operation with three inputs.
- [struct BNNSLayerParametersArithmetic](bnnslayerparametersarithmetic.md)
  A structure that contains the parameters of an arithmetic layer.
- [func BNNSFilterCreateLayerArithmetic(UnsafePointer<BNNSLayerParametersArithmetic>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerarithmetic(_:_:).md)
  Returns a new arithmetic layer.
- [func BNNSArithmeticFilterApplyBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int) -> Int32](bnnsarithmeticfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies an arithmetic filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSArithmeticFilterApplyBackwardBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnsarithmeticfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies an arithmetic filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsarithmeticfunction)*