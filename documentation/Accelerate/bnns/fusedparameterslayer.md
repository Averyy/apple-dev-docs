# BNNS.FusedParametersLayer

**Framework**: Accelerate  
**Kind**: class

A layer object that wraps a fused layer and manages its deinitialization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
class FusedParametersLayer
```

#### Overview

Use a [`BNNS.FusedParametersLayer`](bnns/fusedparameterslayer.md) instance to fuse component layers with the following configurations:

- Convolution → Normalization
- Fully Connected → Normalization
- Transposed Convolution → Normalization
- Convolution → Quantization
- Fully Connected → Quantization
- Transposed Convolution → Quantization
- Arithmetic → Normalization

## Topics

### Creating a Fused Parameters Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](bnns/fusedparameterslayer/init(input:output:fusedlayerparameters:filterparameters:).md)
  Creates a new fused layer from an array of layer parameters.
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](bnns/fusedparameterslayer/init(inputa:inputb:output:fusedlayerparameters:filterparameters:).md)
  Creates a new fused layer from an array of layer parameters, where the first layer accepts two inputs.
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](bnns/fusedparameterslayer/init(inputa:inputb:inputc:output:fusedlayerparameters:filterparameters:).md)
  Creates a new fused layer from an array of layer parameters, where the first layer accepts three inputs.
### Specifying a Layer Parameter
- [struct FusedUnaryArithmeticParameters](bnns/fusedunaryarithmeticparameters.md)
  A structure that contains the parameters for a fused unary arithmetic layer.
- [struct FusedBinaryArithmeticParameters](bnns/fusedbinaryarithmeticparameters.md)
  A structure that contains the parameters for a fused binary arithmetic layer.
- [struct FusedTernaryArithmeticParameters](bnns/fusedternaryarithmeticparameters.md)
  A structure that contains the parameters for a fused ternary arithmetic layer.
- [struct FusedConvolutionParameters](bnns/fusedconvolutionparameters.md)
  A structure that contains the parameters for a fused convolution layer.
- [struct FusedQuantizationParameters](bnns/fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedDequantizationParameters](bnns/fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](bnns/fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.
### Applying a Fused Parameters Layer
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/fusedparameterslayer/apply(batchsize:inputa:inputb:output:for:).md)
  Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](bnns/fusedparameterslayer/apply(batchsize:inputa:inputb:inputc:output:for:).md)
  Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](bnns/fusedparameterslayer/applybackward(batchsize:inputa:inputb:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatingparametergradients:).md)
  Applies the layer backward to generate input gradients, where the first layer accepts two inputs.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingInputCGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](bnns/fusedparameterslayer/applybackward(batchsize:inputa:inputb:inputc:output:outputgradient:generatinginputagradient:generatinginputbgradient:generatinginputcgradient:generatingparametergradients:).md)
  Applies the layer backward to generate input gradients, where the first layer accepts three inputs.

## Relationships

### Inherits From
- [BNNS.FusedLayer](bnns/fusedlayer.md)

## See Also

- [protocol FusableLayerParameters](fusablelayerparameters.md)
- [class FusedConvolutionNormalizationLayer](bnns/fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [class FusedFullyConnectedNormalizationLayer](bnns/fusedfullyconnectednormalizationlayer.md)
  A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.
- [struct BNNSFilterType](bnnsfiltertype.md)
  Constants that define the component filters of a fused layer.
- [func BNNSFilterCreateFusedLayer(Int, UnsafePointer<BNNSFilterType>, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatefusedlayer(_:_:_:_:).md)
  Returns a new fused layer.
- [func BNNSFusedFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies a fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplymultiinputbatch(_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](bnnsfusedfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a fused filter backward to generate input gradients.
- [func BNNSFusedFilterApplyBackwardMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](bnnsfusedfilterapplybackwardmultiinputbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedparameterslayer)*