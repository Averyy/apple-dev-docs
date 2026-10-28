# BNNSFilterCreateConvolutionLayer(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a convolution filter, initialized with input, output, layer, and filter parameters.

**Availability**:
- iOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerConvolution(_:_:))
- iPadOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerConvolution(_:_:))
- Mac Catalyst 13.1+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerConvolution(_:_:))
- macOS 10.12+ - Deprecated in 11.0 (renamed: BNNSFilterCreateLayerConvolution(_:_:))
- tvOS 10.0+ - Deprecated in 14.0 (renamed: BNNSFilterCreateLayerConvolution(_:_:))
- visionOS 1.0+ - Deprecated in 1.0 (renamed: BNNSFilterCreateLayerConvolution(_:_:))
- watchOS 3.0+ - Deprecated in 7.0 (renamed: BNNSFilterCreateLayerConvolution(_:_:))

> **Deprecated**: Use [`BNNSFilterCreateLayerConvolution(_:_:)`](./bnnsfiltercreatelayerconvolution%28_,_%29.md) instead.

## Declaration

```swift
func BNNSFilterCreateConvolutionLayer(_ in_desc: UnsafePointer<BNNSImageStackDescriptor>, _ out_desc: UnsafePointer<BNNSImageStackDescriptor>, _ layer_params: UnsafePointer<BNNSConvolutionLayerParameters>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

```c
BNNSFilterBNNSFilterCreateConvolutionLayer(const BNNSImageStackDescriptor *in_desc, const BNNSImageStackDescriptor *out_desc, const BNNSConvolutionLayerParameters *layer_params, const BNNSFilterParameters *filter_params);
```

## Return Value

A BNNSFilter object representing a convolution filter configured with the specified  parameters

## Parameters

- `in_desc`: Pointer to a `BNNSImageStackDescriptor` struct describing the input
- `out_desc`: Pointer to a `BNNSImageStackDescriptor` struct describing the output
- `layer_params`: Pointer to a `BNNSConvolutionLayerParameters` struct describing the layer parameters
- `filter_params`: Pointer to a `BNNSFilterParameters` struct describing the filter parameters

## See Also

### Convolution layers
- [struct BNNSConvolutionLayerParameters](./bnnsconvolutionlayerparameters.md)
  A structure containing convolution parameters.
- [class ConvolutionLayer](./bnns/convolutionlayer.md)
  A layer object that wraps a convolution filter and manages its deinitialization.
- [struct BNNSLayerParametersConvolution](./bnnslayerparametersconvolution.md)
  A structure that contains the parameters of a convolution layer.
- [func BNNSFilterCreateLayerConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayerconvolution%28_,_%29.md)
  Returns a new convolution layer.
- [func BNNSFilterCreateLayerTransposedConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](./bnnsfiltercreatelayertransposedconvolution%28_,_%29.md)
  Returns a new transposed convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreateconvolutionlayer(_:_:_:_:))*