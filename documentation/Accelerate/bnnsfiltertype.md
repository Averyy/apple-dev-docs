# BNNSFilterType

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Constants that define the component filters of a fused layer.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct BNNSFilterType
```

```c
typedef enum { ... } BNNSFilterType;
```

## Topics

### Layer Constants
- [var BNNSArithmetic: BNNSFilterType](./bnnsarithmetic.md)
  An arithmetic filter.
- [var BNNSConvolution: BNNSFilterType](./bnnsconvolution.md)
  A convolution filter.
- [var BNNSTransposedConvolution: BNNSFilterType](./bnnstransposedconvolution.md)
  A transposed convolution filter.
- [var BNNSFullyConnected: BNNSFilterType](./bnnsfullyconnected.md)
  A fully connected filter.
- [var BNNSBatchNorm: BNNSFilterType](./bnnsbatchnorm.md)
  A batch normalization filter.
- [var BNNSGroupNorm: BNNSFilterType](./bnnsgroupnorm.md)
  A group normalization filter.
- [var BNNSInstanceNorm: BNNSFilterType](./bnnsinstancenorm.md)
  An instance normalization filter.
- [var BNNSLayerNorm: BNNSFilterType](./bnnslayernorm.md)
  A layer normalization filter.
- [var BNNSQuantization: BNNSFilterType](./bnnsquantization.md)
  A quantization filter.
### Raw Values
- [var rawValue: UInt32](./bnnsfiltertype/rawvalue.md)
- [init(UInt32)](./bnnsfiltertype/init%28_%29.md)
- [init(rawValue: UInt32)](./bnnsfiltertype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Fused layers
- [protocol FusableLayerParameters](./fusablelayerparameters.md)
- [class FusedParametersLayer](./bnns/fusedparameterslayer.md)
  A layer object that wraps a fused layer and manages its deinitialization.
- [class FusedConvolutionNormalizationLayer](./bnns/fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [class FusedFullyConnectedNormalizationLayer](./bnns/fusedfullyconnectednormalizationlayer.md)
  A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.
- [func BNNSFilterCreateFusedLayer(Int, UnsafePointer<BNNSFilterType>, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatefusedlayer%28_,_,_,_%29.md)
  Returns a new fused layer.
- [func BNNSFusedFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](./bnnsfusedfilterapplybatch%28_,_,_,_,_,_,_%29.md)
  Applies a fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int, Bool) -> Int32](./bnnsfusedfilterapplymultiinputbatch%28_,_,_,_,_,_,_,_%29.md)
  Applies a multiple-input fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](./bnnsfusedfilterapplybackwardbatch%28_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a fused filter backward to generate input gradients.
- [func BNNSFusedFilterApplyBackwardMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](./bnnsfusedfilterapplybackwardmultiinputbatch%28_,_,_,_,_,_,_,_,_,_,_,_%29.md)
  Applies a multiple-input fused filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltertype)*