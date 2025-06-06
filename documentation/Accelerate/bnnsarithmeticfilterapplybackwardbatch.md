# BNNSArithmeticFilterApplyBackwardBatch(_:_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Applies an arithmetic filter backward to generate input gradients.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
func BNNSArithmeticFilterApplyBackwardBatch(_ filter: BNNSFilter?, _ batch_size: Int, _ number_of_inputs: Int, _ in: UnsafeMutablePointer<UnsafeRawPointer?>?, _ in_stride: UnsafePointer<Int>?, _ in_delta: UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, _ in_delta_stride: UnsafePointer<Int>, _ out: UnsafeRawPointer?, _ out_stride: Int, _ out_delta: UnsafeMutablePointer<BNNSNDArrayDescriptor>, _ out_delta_stride: Int) -> Int32
```

## Parameters

- `filter`: The filter to apply.
- `batch_size`: The number of input-output pairs.
- `number_of_inputs`: The number of inputs to the arithmetic operation.
- `in`: Pointer to the input data.
- `in_stride`: Increment, in values, between inputs.
- `in_delta`: The descriptor of the input delta.
- `in_delta_stride`: Increment, in values, between input delta objects.
- `out`: Pointer to output object.
- `out_stride`: Increment, in values, between output objects.
- `out_delta`: The descriptor of the output delta.
- `out_delta_stride`: Increment, in values, between output delta objects.

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
- [struct BNNSArithmeticFunction](bnnsarithmeticfunction.md)
  Constants that define arithmetic operations.
- [struct BNNSLayerParametersArithmetic](bnnslayerparametersarithmetic.md)
  A structure that contains the parameters of an arithmetic layer.
- [func BNNSFilterCreateLayerArithmetic(UnsafePointer<BNNSLayerParametersArithmetic>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerarithmetic(_:_:).md)
  Returns a new arithmetic layer.
- [func BNNSArithmeticFilterApplyBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int) -> Int32](bnnsarithmeticfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies an arithmetic filter to a set of input objects, writing the result to a set of output objects.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsarithmeticfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:))*