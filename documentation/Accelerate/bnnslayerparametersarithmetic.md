# BNNSLayerParametersArithmetic

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that contains the parameters of an arithmetic layer.

**Availability**:
- iOS 14.0+ - Deprecated in 18.0
- iPadOS 14.0+ - Deprecated in 18.0
- Mac Catalyst 14.0+ - Deprecated in 18.0
- macOS 11.0+ - Deprecated in 15.0
- tvOS 14.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 7.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
struct BNNSLayerParametersArithmetic
```

```c
typedef struct { ... } BNNSLayerParametersArithmetic;
```

## Topics

### Initializers
- [init(arithmetic_function: BNNSArithmeticFunction, arithmetic_function_fields: UnsafeMutableRawPointer, activation: BNNSActivation)](./bnnslayerparametersarithmetic/init%28arithmetic_function,arithmetic_function_fields,activation%29.md)
  Returns a new arithmetic layer parameters structure.
### Instance Properties
- [var arithmetic_function: BNNSArithmeticFunction](./bnnslayerparametersarithmetic/arithmetic_function.md)
  The arithmetic operation of the layer.
- [var arithmetic_function_fields: UnsafeMutableRawPointer](./bnnslayerparametersarithmetic/arithmetic_function_fields.md)
  A pointer to an arithmetic function field structure.
- [var activation: BNNSActivation](./bnnslayerparametersarithmetic/activation.md)
  The activation function that the layer applies to the output.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)

## See Also

### Arithmetic layers
- [class UnaryArithmeticLayer](./bnns/unaryarithmeticlayer.md)
  A layer object that wraps a unary arithmetic filter and manages its deinitialization.
- [class BinaryArithmeticLayer](./bnns/binaryarithmeticlayer.md)
  A layer object that wraps a binary arithmetic filter and manages its deinitialization.
- [class TernaryArithmeticLayer](./bnns/ternaryarithmeticlayer.md)
  A layer object that wraps a ternary arithmetic filter and manages its deinitialization.
- [struct BNNSDescriptorType](./bnnsdescriptortype.md)
  Constants that describe the input and output types of an arithmetic operation.
- [struct BNNSArithmeticUnary](./bnnsarithmeticunary.md)
  A structure that contains the input and output of an arithmetic operation with a single input.
- [struct BNNSArithmeticBinary](./bnnsarithmeticbinary.md)
  A structure that contains the inputs and output of an arithmetic operation with two inputs.
- [struct BNNSArithmeticTernary](./bnnsarithmeticternary.md)
  A structure that contains the inputs and output of an arithmetic operation with three inputs.
- [struct BNNSArithmeticFunction](./bnnsarithmeticfunction.md)
  Constants that define arithmetic operations.
- [func BNNSFilterCreateLayerArithmetic(UnsafePointer<BNNSLayerParametersArithmetic>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerarithmetic%28_,_%29.md)
  Returns a new arithmetic layer.
- [func BNNSArithmeticFilterApplyBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int) -> Int32](./bnnsarithmeticfilterapplybatch%28_,_,_,_,_,_,_%29.md)
  Applies an arithmetic filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSArithmeticFilterApplyBackwardBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int) -> Int32](./bnnsarithmeticfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies an arithmetic filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersarithmetic)*