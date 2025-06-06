# BNNSFilterCreateLayerConvolution(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a new convolution layer.

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
func BNNSFilterCreateLayerConvolution(_ layer_params: UnsafePointer<BNNSLayerParametersConvolution>, _ filter_params: UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?
```

#### Discussion

Use convolution to convolve an input image over all dimensions. For example, given the following inputs and weights:

```swift
let channelZero: [Float] = [10, 11,
                            12, 13]
let channelOne: [Float] = [20, 21,
                           22, 23]
let channelTwo: [Float] = [30, 31,
                           32, 33]

let input = channelZero + channelOne + channelTwo

var weights = [Float](repeating: 1 / Float(input.count),
                      count: input.count)
```

The following code creates and applies convolution:

```swift
var bias = [Float(0)]

var output = [Float](repeating: 0, count: 1)

weights.withUnsafeMutableBufferPointer { weightsPtr in
    bias.withUnsafeMutableBufferPointer { biasPtr in
        
        let inDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                 layout: BNNSDataLayoutImageCHW,
                                                 size: (2, 2, 3, 0, 0, 0, 0, 0),
                                                 stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                 data: nil,
                                                 data_type: .float,
                                                 table_data: nil,
                                                 table_data_type: .float,
                                                 data_scale: 1,
                                                 data_bias: 0)
        
        let outDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                  layout: BNNSDataLayoutImageCHW,
                                                  size: (1, 1, 1, 0, 0, 0, 0, 0),
                                                  stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                  data: nil,
                                                  data_type: .float,
                                                  table_data: nil,
                                                  table_data_type: .float,
                                                  data_scale: 1,
                                                  data_bias: 0)
        
        let weightsDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                      layout: BNNSDataLayoutConvolutionWeightsOIHW,
                                                      size: (2, 2, 3, 1, 0, 0, 0, 0),
                                                      stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                      data: weightsPtr.baseAddress,
                                                      data_type: .float,
                                                      table_data: nil,
                                                      table_data_type: .float,
                                                      data_scale: 1,
                                                      data_bias: 0)
        
        let biasDescriptor = BNNSNDArrayDescriptor(flags: BNNSNDArrayFlags(0),
                                                   layout: BNNSDataLayoutVector,
                                                   size: (1, 0, 0, 1, 0, 0, 0, 0),
                                                   stride: (0, 0, 0, 0, 0, 0, 0, 0),
                                                   data: biasPtr.baseAddress,
                                                   data_type: .float,
                                                   table_data: nil,
                                                   table_data_type: .float,
                                                   data_scale: 1,
                                                   data_bias: 0)
        
        var parameters = BNNSLayerParametersConvolution(i_desc: inDescriptor,
                                                        w_desc: weightsDescriptor,
                                                        o_desc: outDescriptor,
                                                        bias: biasDescriptor,
                                                        activation: .identity,
                                                        x_stride: 1, y_stride: 1,
                                                        x_dilation_stride: 0, y_dilation_stride: 0,
                                                        x_padding: 0, y_padding: 0,
                                                        groups: 1,
                                                        pad: (0, 0, 0, 0))
        
        guard let filter = BNNSFilterCreateLayerConvolution(&parameters, nil) else {
            fatalError("`BNNSFilterCreateLayerConvolution` returns `nil`.")
        }
        defer {
            BNNSFilterDestroy(filter)
        }
        
        BNNSFilterApply(filter,
                        input,
                        &output)
    }
}
```

On return, the output contains `[21.5]`, calculated using the following arithmetic:

```c
// 1.0 / 12.0 ≅ 0.0833

( (10.0 * 0.0833) + (11.0 * 0.0833) + 
  (12.0 * 0.0833) + (13.0 * 0.0833) ) +

( (20.0 * 0.0833) + (21.0 * 0.0833) + 
  (22.0 * 0.0833) + (23.0 * 0.0833) ) +

( (30.0 * 0.0833) + (31.0 * 0.0833) + 
  (32.0 * 0.0833) + (33.0 * 0.0833) ) = 21.5

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
- [func BNNSFilterCreateLayerTransposedConvolution(UnsafePointer<BNNSLayerParametersConvolution>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayertransposedconvolution(_:_:).md)
  Returns a new transposed convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsfiltercreatelayerconvolution(_:_:))*