# BNNSFilterCreateFusedLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new fused layer.

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
func BNNSFilterCreateFusedLayer(_ number_of_fused_filters: Int, _ filter_type: UnsafePointer<BNNSFilterType>, _ layer_params: UnsafeMutablePointer<UnsafeRawPointer>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use this function to create an `N` layer fused filter that processes input as: `input → filter0 → filter1 →` … `→ filter N-1 → output`. The first `N - 1` filters must have [`BNNSActivationFunctionIdentity`](bnnsactivationfunctionidentity.md) activation function. For the first `N - 2` filters, each filter’s output descriptor and its subsequent filter’s input descriptor must have the same size, stride, and data type.

[`BNNSFilterCreateFusedLayer(_:_:_:_:)`](bnnsfiltercreatefusedlayer(_:_:_:_:).md) supports two filters. The first filter must be either [`BNNSConvolution`](bnnsconvolution.md) or [`BNNSFullyConnected`](bnnsfullyconnected.md). The second filter must be one of [`BNNSBatchNorm`](bnnsbatchnorm.md), [`BNNSInstanceNorm`](bnnsinstancenorm.md), [`BNNSLayerNorm`](bnnslayernorm.md), or [`BNNSGroupNorm`](bnnsgroupnorm.md).

The following code shows how you pass [`BNNSLayerParametersConvolution`](bnnslayerparametersconvolution.md) and [`BNNSLayerParametersNormalization`](bnnslayerparametersnormalization.md) structures to [`BNNSFilterCreateFusedLayer(_:_:_:_:)`](bnnsfiltercreatefusedlayer(_:_:_:_:).md) to create a fused convolution-layer normalization filter:

```swift
// `input`, `output`, and `weights` are single-precision arrays.
// `inDescriptor` and `outDescriptor` are the `BNNSNDArrayDescriptor` structures
// for the fused layer's input and output.

weights.withUnsafeMutableBytes { weightsPtr in
    let weightsDescriptor = BNNSNDArrayDescriptor(flags: flags,
                                                  layout: BNNSDataLayoutConvolutionWeightsOIHW,
                                                  size: (3, 3, 1, 1, 0, 0, 0, 0),
                                                  stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                  data: weightsPtr.baseAddress,
                                                  data_type: .float,
                                                  table_data: nil,
                                                  table_data_type: .float,
                                                  data_scale: 0,
                                                  data_bias: 0)
    
    let convolutionParameters = BNNSLayerParametersConvolution(i_desc: inDescriptor,
                                                               w_desc: weightsDescriptor,
                                                               o_desc: outDescriptor,
                                                               bias: BNNSNDArrayDescriptor(),
                                                               activation: .identity,
                                                               x_stride: 1, y_stride: 1,
                                                               x_dilation_stride: 0, y_dilation_stride: 0,
                                                               x_padding: 0, y_padding: 0,
                                                               groups: 1,
                                                               pad: (0, 0, 0, 0))
    
    let normalizationParameters = BNNSLayerParametersNormalization(i_desc: outDescriptor,
                                                                   o_desc: outDescriptor,
                                                                   beta_desc: inDescriptor,
                                                                   gamma_desc: inDescriptor,
                                                                   moving_mean_desc: BNNSNDArrayDescriptor(),
                                                                   moving_variance_desc: BNNSNDArrayDescriptor(),
                                                                   momentum: 0,
                                                                   epsilon: 1,
                                                                   activation: .identity,
                                                                   num_groups: 1,
                                                                   normalization_axis: 0)
    withUnsafeBytes(of: convolutionParameters) { convolutionPtr in
        withUnsafeBytes(of: normalizationParameters) { normalizationPtr in
            
            var parameters = [convolutionPtr.baseAddress!, normalizationPtr.baseAddress!]
            let filter = BNNSFilterCreateFusedLayer(2,
                                                    [BNNSConvolution, BNNSLayerNorm],
                                                    &parameters,
                                                    nil)
            defer {
                BNNSFilterDestroy(filter)
            }
            
            BNNSFusedFilterApplyBatch(filter, 1,
                                      input, input.count,
                                      &output, output.count,
                                      false)
        }
    }
}
```

## Parameters

- `number_of_fused_filters`: The number of fused filters.
- `filter_type`: Array of fused filter types.
- `layer_params`: Array of fused layer parameter pointers.
- `filter_params`: The filter runtime parameters.

## See Also

- [protocol FusableLayerParameters](fusablelayerparameters.md)
- [class FusedParametersLayer](bnns/fusedparameterslayer.md)
  A layer object that wraps a fused layer and manages its deinitialization.
- [class FusedConvolutionNormalizationLayer](bnns/fusedconvolutionnormalizationlayer.md)
  A layer object that wraps a fused, convolution normalization layer and manages its deinitialization.
- [class FusedFullyConnectedNormalizationLayer](bnns/fusedfullyconnectednormalizationlayer.md)
  A layer object that wraps a fused, fully connected normalization layer and manages its deinitialization.
- [struct BNNSFilterType](bnnsfiltertype.md)
  Constants that define the component filters of a fused layer.
- [func BNNSFusedFilterApplyBatch(BNNSFilter?, Int, UnsafeRawPointer, Int, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplybatch(_:_:_:_:_:_:_:).md)
  Applies a fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer>, UnsafePointer<Int>, UnsafeMutableRawPointer, Int, Bool) -> Int32](bnnsfusedfilterapplymultiinputbatch(_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter to a set of input objects, writing the result to a set of output objects.
- [func BNNSFusedFilterApplyBackwardBatch(BNNSFilter?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>?, Int, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](bnnsfusedfilterapplybackwardbatch(_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a fused filter backward to generate input gradients.
- [func BNNSFusedFilterApplyBackwardMultiInputBatch(BNNSFilter?, Int, Int, UnsafeMutablePointer<UnsafeRawPointer?>?, UnsafePointer<Int>?, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>>, UnsafePointer<Int>, UnsafeRawPointer?, Int, UnsafeMutablePointer<BNNSNDArrayDescriptor>, Int, UnsafeMutablePointer<UnsafeMutablePointer<BNNSNDArrayDescriptor>?>?) -> Int32](bnnsfusedfilterapplybackwardmultiinputbatch(_:_:_:_:_:_:_:_:_:_:_:_:).md)
  Applies a multiple-input fused filter backward to generate input gradients.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatefusedlayer(_:_:_:_:))*