# BNNSFilterCreateLayerTransposedConvolution(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new transposed convolution layer.

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
func BNNSFilterCreateLayerTransposedConvolution(_ layer_params: UnsafePointer<BNNSLayerParametersConvolution>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use transposed convolution to upsample a tensor by performing an operation that’s effectively the inverse of a convolution.

The following figure illustrates the process of transposed convolution. The operation multiplies each element in the input by the kernel to produce the corresponding values in the output. The final output, pictured at the bottom of the figure, is the sum of the products:

![Figure that describes a transposed convolution operation over a two times two source matrix using a three times three kernel. Each step is illustrated as a row, showing scalar multiplication of the source element multiplied by the kernel, and the transposed convolution result is the sum of each scalar multiplication.](https://docs-assets.developer.apple.com/published/f459e35c9259780d5d26b6db74ac9c0b/media-3633105%402x.png)

Use the following code to perform the illustrated transposed convolution:

```swift
let input = [Float](repeating: 1, count: 2 * 2)

var kernel = [Float](repeating: 1, count: 3 * 3)

var output = [Float](repeating: 0, count: 4 * 4)

kernel.withUnsafeMutableBufferPointer { kernelPtr in
    
    let inDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                             layout: BNNSDataLayoutImageCHW,
                                             size: (2, 2, 1, 0, 0, 0, 0, 0),
                                             stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                             data: nil,
                                             data_type: .float,
                                             table_data: nil,
                                             table_data_type: .float,
                                             data_scale: 1,
                                             data_bias: 0)
    
    let weightsDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                  layout: BNNSDataLayoutConvolutionWeightsOIHW,
                                                  size: (3, 3, 1, 1, 0, 0, 0, 0),
                                                  stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                  data: kernelPtr.baseAddress,
                                                  data_type: .float,
                                                  table_data: nil,
                                                  table_data_type: .float,
                                                  data_scale: 1,
                                                  data_bias: 0)
    
    let outDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                              layout: BNNSDataLayoutImageCHW,
                                              size: (4, 4, 1, 0, 0, 0, 0, 0),
                                              stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                              data: nil,
                                              data_type: .float,
                                              table_data: nil,
                                              table_data_type: .float,
                                              data_scale: 1,
                                              data_bias: 0)
    
    var parameters = BNNSLayerParametersConvolution(i_desc: inDescriptor,
                                                    w_desc: weightsDescriptor,
                                                    o_desc: outDescriptor,
                                                    bias: BNNSNDArrayDescriptor(),
                                                    activation: .identity,
                                                    x_stride: 1, y_stride: 1,
                                                    x_dilation_stride: 0, y_dilation_stride: 0,
                                                    x_padding: 0, y_padding: 0,
                                                    groups: 1,
                                                    pad: (0, 0, 0, 0))

    let filter = BNNSFilterCreateLayerTransposedConvolution(&parameters,
                                                            nil)
    defer {
        BNNSFilterDestroy(filter)
    }
    
    BNNSFilterApply(filter,
                    input,
                    &output)
}
```

On return, `output` contains the following values:

```swift
[ 1.0, 2.0, 2.0, 1.0, 
  2.0, 4.0, 4.0, 2.0, 
  2.0, 4.0, 4.0, 2.0, 
  1.0, 2.0, 2.0, 1.0 ]
```

## Parameters

- `layer_params`: Layer parameters.
- `filter_params`: The filter runtime parameters.

## See Also

- [struct BNNSConvolutionLayerParameters](bnnsconvolutionlayerparameters.md)
  A structure containing convolution parameters.
- [func BNNSFilterCreateConvolutionLayer(UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSImageStackDescriptor>, UnsafePointer<BNNSConvolutionLayerParameters>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreateconvolutionlayer(_:_:_:_:).md)
  Returns a convolution filter, initialized with input, output, layer, and filter parameters.
- [class ConvolutionLayer](bnns/convolutionlayer.md)
  A layer object that wraps a convolution filter and manages its deinitialization.
- [struct BNNSLayerParametersConvolution](bnnslayerparametersconvolution.md)
  A structure that contains the parameters of a convolution layer.
- [func BNNSFilterCreateLayerConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerconvolution(_:_:).md)
  Returns a new convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayertransposedconvolution(_:_:))*