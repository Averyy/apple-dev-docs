# BNNSFilterType

**Framework**: Accelerate  
**Kind**: struct

Constants that define the component filters of a fused layer.

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
struct BNNSFilterType
```

## Topics

### Layer Constants
- [var BNNSArithmetic: BNNSFilterType](bnnsarithmetic.md)
  An arithmetic filter.
- [var BNNSConvolution: BNNSFilterType](bnnsconvolution.md)
  A convolution filter.
- [var BNNSTransposedConvolution: BNNSFilterType](bnnstransposedconvolution.md)
  A transposed convolution filter.
- [var BNNSFullyConnected: BNNSFilterType](bnnsfullyconnected.md)
  A fully connected filter.
- [var BNNSBatchNorm: BNNSFilterType](bnnsbatchnorm.md)
  A batch normalization filter.
- [var BNNSGroupNorm: BNNSFilterType](bnnsgroupnorm.md)
  A group normalization filter.
- [var BNNSInstanceNorm: BNNSFilterType](bnnsinstancenorm.md)
  An instance normalization filter.
- [var BNNSLayerNorm: BNNSFilterType](bnnslayernorm.md)
  A layer normalization filter.
- [var BNNSQuantization: BNNSFilterType](bnnsquantization.md)
  A quantization filter.
### Raw Values
- [var rawValue: UInt32](bnnsfiltertype/rawvalue.md)
- [init(UInt32)](bnnsfiltertype/init(_:).md)
- [init(rawValue: UInt32)](bnnsfiltertype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [protocol FusableLayerParameters](fusablelayerparameters.md)
- [class FusedParametersLayer](bnns/fusedparameterslayer.md)
  A layer object that wraps a fused layer and manages its deinitialization.
- [class FusedConvolutionNormalizationLayer](bnns/fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [class FusedFullyConnectedNormalizationLayer](bnns/fusedfullyconnectednormalizationlayer.md)
  A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltertype)*