# BNNSFilterCreateConvolutionLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a convolution filter, initialized with input, output, layer, and filter parameters.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
func BNNSFilterCreateConvolutionLayer(_ in_desc: UnsafePointer<BNNSImageStackDescriptor>, _ out_desc: UnsafePointer<BNNSImageStackDescriptor>, _ layer_params: UnsafePointer<BNNSConvolutionLayerParameters>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Return Value

A BNNSFilter object representing a convolution filter configured with the specified  parameters

## Parameters

- `in_desc`: Pointer to a   struct describing the input
- `out_desc`: Pointer to a   struct describing the output
- `layer_params`: Pointer to a   struct describing the layer parameters
- `filter_params`: Pointer to a   struct describing the filter parameters

## See Also

- [struct BNNSConvolutionLayerParameters](bnnsconvolutionlayerparameters.md)
  A structure containing convolution parameters.
- [class ConvolutionLayer](bnns/convolutionlayer.md)
  A layer object that wraps a convolution filter and manages its deinitialization.
- [struct BNNSLayerParametersConvolution](bnnslayerparametersconvolution.md)
  A structure that contains the parameters of a convolution layer.
- [func BNNSFilterCreateLayerConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerconvolution(_:_:).md)
  Returns a new convolution layer.
- [func BNNSFilterCreateLayerTransposedConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayertransposedconvolution(_:_:).md)
  Returns a new transposed convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreateconvolutionlayer(_:_:_:_:))*