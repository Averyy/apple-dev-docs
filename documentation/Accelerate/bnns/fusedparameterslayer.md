# BNNS.FusedParametersLayer

**Framework**: Accelerate  
**Kind**: class  
**Role**: Class

A layer object that wraps a fused layer and manages its deinitialization.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
class FusedParametersLayer
```

#### Overview

Use a [`BNNS.FusedParametersLayer`](./fusedparameterslayer.md) instance to fuse component layers with the following configurations:

- Convolution → Normalization
- Fully Connected → Normalization
- Transposed Convolution → Normalization
- Convolution → Quantization
- Fully Connected → Quantization
- Transposed Convolution → Quantization
- Arithmetic → Normalization

## Topics

### Creating a Fused Parameters Layer
- [convenience init?(input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](./fusedparameterslayer/init%28input,output,fusedlayerparameters,filterparameters%29.md)
  Creates a new fused layer from an array of layer parameters.
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](./fusedparameterslayer/init%28inputa,inputb,output,fusedlayerparameters,filterparameters%29.md)
  Creates a new fused layer from an array of layer parameters, where the first layer accepts two inputs.
- [convenience init?(inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, fusedLayerParameters: [any FusableLayerParameters], filterParameters: BNNSFilterParameters?)](./fusedparameterslayer/init%28inputa,inputb,inputc,output,fusedlayerparameters,filterparameters%29.md)
  Creates a new fused layer from an array of layer parameters, where the first layer accepts three inputs.
### Specifying a Layer Parameter
- [struct FusedUnaryArithmeticParameters](./fusedunaryarithmeticparameters.md)
  A structure that contains the parameters for a fused unary arithmetic layer.
- [struct FusedBinaryArithmeticParameters](./fusedbinaryarithmeticparameters.md)
  A structure that contains the parameters for a fused binary arithmetic layer.
- [struct FusedTernaryArithmeticParameters](./fusedternaryarithmeticparameters.md)
  A structure that contains the parameters for a fused ternary arithmetic layer.
- [struct FusedConvolutionParameters](./fusedconvolutionparameters.md)
  A structure that contains the parameters for a fused convolution layer.
- [struct FusedQuantizationParameters](./fusedquantizationparameters.md)
  A structure that contains the parameters for a fused quantization layer.
- [struct FusedDequantizationParameters](./fuseddequantizationparameters.md)
  A structure that contains the parameters for a fused dequantization layer.
- [struct FusedFullyConnectedParameters](./fusedfullyconnectedparameters.md)
  A structure that contains the parameters for a fused fully connected layer.
- [struct FusedNormalizationParameters](./fusednormalizationparameters.md)
  A structure that contains the parameters for a fused normalization layer.
### Applying a Fused Parameters Layer
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](./fusedparameterslayer/apply%28batchsize,inputa,inputb,output,for%29.md)
  Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.
- [func apply(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, for: BNNS.LearningPhase) throws](./fusedparameterslayer/apply%28batchsize,inputa,inputb,inputc,output,for%29.md)
  Applies the layer to a set of input objects and writes the result to a set of output objects, where the first layer accepts two inputs.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](./fusedparameterslayer/applybackward%28batchsize,inputa,inputb,output,outputgradient,generatinginputagradient,generatinginputbgradient,generatingparametergradients%29.md)
  Applies the layer backward to generate input gradients, where the first layer accepts two inputs.
- [func applyBackward(batchSize: Int, inputA: BNNSNDArrayDescriptor, inputB: BNNSNDArrayDescriptor, inputC: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, outputGradient: BNNSNDArrayDescriptor, generatingInputAGradient: BNNSNDArrayDescriptor, generatingInputBGradient: BNNSNDArrayDescriptor, generatingInputCGradient: BNNSNDArrayDescriptor, generatingParameterGradients: [BNNSNDArrayDescriptor]) throws](./fusedparameterslayer/applybackward%28batchsize,inputa,inputb,inputc,output,outputgradient,generatinginputagradient,generatinginputbgradient,generatinginputcgradient,generatingparametergradients%29.md)
  Applies the layer backward to generate input gradients, where the first layer accepts three inputs.

## Relationships

### Inherits From
- [BNNS.FusedLayer](./fusedlayer.md)

## See Also

### Fused layers
- [protocol FusableLayerParameters](../fusablelayerparameters.md)
- [class FusedConvolutionNormalizationLayer](./fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [class FusedFullyConnectedNormalizationLayer](./fusedfullyconnectednormalizationlayer.md)
  A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.
- [struct BNNSFilterType](../bnnsfiltertype.md)
  Constants that define the component filters of a fused layer.
- [func BNNSFilterCreateFusedLayer(Int, UnsafePointer<BNNSFilterType>, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](../bnnsfiltercreatefusedlayer%28_,_,_,_%29.md)
  Returns a new fused layer.
- [func BNNSFusedFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](../bnnsfusedfilterapplybatch%28_,_,_,_,_,_,_%29.md)
  Applies a fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int, Bool) -> Int32](../bnnsfusedfilterapplymultiinputbatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a multiple-input fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](../bnnsfusedfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a fused filter backward to generate input gradients.
- [func BNNSFusedFilterApplyBackwardMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](../bnnsfusedfilterapplybackwardmultiinputbatch%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a multiple-input fused filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/fusedparameterslayer)*