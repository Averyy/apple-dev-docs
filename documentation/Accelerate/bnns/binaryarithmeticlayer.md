# BNNS.BinaryArithmeticLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a binary arithmetic filter and manages its deinitialization.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
class BinaryArithmeticLayer
```

## Topics

### Creating a Binary Arithmetic Layer
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputADescriptorType: BNNS.DescriptorType, inputB: BNNSNDArrayDescriptor, inputBDescriptorType: BNNS.DescriptorType, output: BNNSNDArrayDescriptor, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticBinaryFunction, activation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters?)](bnns/binaryarithmeticlayer/init(inputa:inputadescriptortype:inputb:inputbdescriptortype:output:outputdescriptortype:function:activation:filterparameters:).md)
  Returns a new binary arithmetic layer.
### Specifying a Binary Arithmetic Function
- [BNNS.ArithmeticBinaryFunction](bnns/arithmeticbinaryfunction.md)
  Constants that describe binary arithmetic functions.
### Specifying a Descriptor Type
- [BNNS.DescriptorType](bnns/descriptortype.md)
  Constants that describe the input and output types of an arithmetic operation.
### Applying a Binary Arithmetic Layer
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/binaryarithmeticlayer/apply(batchsize:inputa:inputb:output:).md)
  Applies the layer to a set of input array descriptors, writing the result to a set of output array descriptors.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor) throws](bnns/binaryarithmeticlayer/applybackward(batchsize:inputa:inputb:output:outputgradient:generatinginputagradient:generatinginputbgradient:).md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](bnns/layer.md)

## See Also

- [class UnaryArithmeticLayer](bnns/unaryarithmeticlayer.md)
  A layer object that wraps a unary arithmetic filter and manages its deinitialization.
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
- [func BNNSArithmeticFilterApplyBackwardBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int) -> Int32](bnnsarithmeticfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies an arithmetic filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/binaryarithmeticlayer)*