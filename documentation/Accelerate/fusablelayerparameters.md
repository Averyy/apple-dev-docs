# FusableLayerParameters

**Framework**: Accelerate  
**Kind**: protocol

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
protocol FusableLayerParameters
```

## Relationships

### Conforming Types
- [BNNS.FusedBinaryArithmeticParameters](bnns/fusedbinaryarithmeticparameters.md)
- [BNNS.FusedConvolutionParameters](bnns/fusedconvolutionparameters.md)
- [BNNS.FusedDequantizationParameters](bnns/fuseddequantizationparameters.md)
- [BNNS.FusedFullyConnectedParameters](bnns/fusedfullyconnectedparameters.md)
- [BNNS.FusedNormalizationParameters](bnns/fusednormalizationparameters.md)
- [BNNS.FusedQuantizationParameters](bnns/fusedquantizationparameters.md)
- [BNNS.FusedTernaryArithmeticParameters](bnns/fusedternaryarithmeticparameters.md)
- [BNNS.FusedUnaryArithmeticParameters](bnns/fusedunaryarithmeticparameters.md)

## See Also

- [class FusedParametersLayer](bnns/fusedparameterslayer.md)
  A layer object that wraps a fused layer and manages its deinitialization.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/fusablelayerparameters)*