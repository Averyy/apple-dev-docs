# init(type:input:output:bias:activation:kernelSize:stride:padding:filterParameters:)

**Framework**: Accelerate  
**Kind**: init

Returns a new pooling layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
convenience init?(type poolingType: BNNS.PoolingType, input: BNNSNDArrayDescriptor, output: BNNSNDArrayDescriptor, bias: BNNSNDArrayDescriptor?, activation: BNNS.ActivationFunction, kernelSize: (width: Int, height: Int), stride: (x: Int, y: Int), padding: BNNS.ConvolutionPadding, filterParameters: BNNSFilterParameters? = nil)
```

#### Discussion

> ❗ **Important**:  The number of input channels must be equal to number of output channels. The pooling layer supports `float16` and `float`, and the input data type must be equal to the output data type. The pooling layer only supports dilation stride for max and unmax pooling functions and in that case, data type must be `float`.

## Parameters

- `poolingType`: An enumeration that specifies the pooling type.
- `input`: The descriptor of the input.
- `output`: The descriptor of the output.
- `bias`: The descriptor of the bias.
- `activation`: The activation function that the layer applies to the output.
- `kernelSize`: The size of the kernel.
- `stride`: The width and height increments of the input image.
- `padding`: The padding, which is the number of virtual zeros added to the sides of each channel.
- `filterParameters`: The filter runtime parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/poolinglayer/init(type:input:output:bias:activation:kernelsize:stride:padding:filterparameters:))*