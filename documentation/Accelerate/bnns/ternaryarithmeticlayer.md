# BNNS.TernaryArithmeticLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a ternary arithmetic filter and manages its deinitialization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- watchOS 8.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
class TernaryArithmeticLayer
```

## Topics

### Creating a Ternary Arithmetic Layer
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputADescriptorType: BNNS.DescriptorType, inputB: BNNSNDArrayDescriptor, inputBDescriptorType: BNNS.DescriptorType, inputC: BNNSNDArrayDescriptor, inputCDescriptorType: BNNS.DescriptorType, output: BNNSNDArrayDescriptor, outputDescriptorType: BNNS.DescriptorType, function: BNNS.ArithmeticTernaryFunction, activation: BNNS.ActivationFunction, filterParameters: BNNSFilterParameters?)](bnns/ternaryarithmeticlayer/init(inputa:inputadescriptortype:inputb:inputbdescriptortype:inputc:inputcdescriptortype:output:outputdescriptortype:function:activation:filterparameters:).md)
  Returns a new ternary arithmetic layer.
### Specifying a Ternary Arithmetic Function
- [BNNS.ArithmeticTernaryFunction](bnns/arithmeticternaryfunction.md)
  Constants that describe ternary arithmetic functions.
### Specifying a Descriptor Type
- [BNNS.DescriptorType](bnns/descriptortype.md)
  Constants that describe the input and output types of an arithmetic operation.
### Applying a Ternary Arithmetic Layer
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor) throws](bnns/ternaryarithmeticlayer/apply(batchsize:inputa:inputb:inputc:output:).md)
  Applies the layer to a set of input array descriptors, writing the result to a set of output array descriptors.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingInputCGradient: BNNSNDArrayDescriptor) throws](bnns/ternaryarithmeticlayer/applybackward(batchsize:inputa:inputb:inputc:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatinginputcgradient:).md)
  Applies the layer backward to generate input gradients.

## Relationships

### Inherits From
- [BNNS.Layer](bnns/layer.md)

## See Also

- [class UnaryArithmeticLayer](bnns/unaryarithmeticlayer.md)
  A layer object that wraps a unary arithmetic filter and manages its deinitialization.
- [class BinaryArithmeticLayer](bnns/binaryarithmeticlayer.md)
  A layer object that wraps a binary arithmetic filter and manages its deinitialization.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/ternaryarithmeticlayer)*