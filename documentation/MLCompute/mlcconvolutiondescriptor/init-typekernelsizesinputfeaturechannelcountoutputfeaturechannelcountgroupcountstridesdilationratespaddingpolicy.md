# init(type:kernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:)

**Framework**: ML Compute  
**Kind**: init

Creates a descriptor for the type, sizes, number of feature channels, group count, strides, dilation rates, and padding policy you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(type: MLCConvolutionType = .standard, kernelSizes: (height: Int, width: Int), inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, groupCount: Int = 1, strides: (y: Int, x: Int) = (1, 1), dilationRates: (y: Int, x: Int) = (1, 1), paddingPolicy: MLCPaddingPolicy = .same)
```

## Parameters

- `type`: The convolution type.
- `kernelSizes`: A tuple that contains the kernel sizes for y and x.
- `inputFeatureChannelCount`: The number of feature channels in the input tensor.
- `outputFeatureChannelCount`: The number of feature channels in the output tensor.
- `groupCount`: The number of groups.
- `strides`: A tuple that contains the kernel strides for y and x.
- `dilationRates`: A tuple that contains the dilation rates for y and x.
- `paddingPolicy`: The padding policy.

## See Also

- [convenience init(transposeWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int)](mlcconvolutiondescriptor/init(transposewithkernelwidth:kernelheight:inputfeaturechannelcount:outputfeaturechannelcount:).md)
  Creates a descriptor for convolution transpose with the kernel sizes and number of feature channels you specify.
- [convenience init(depthwiseWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, channelMultiplier: Int)](mlcconvolutiondescriptor/init(depthwisewithkernelwidth:kernelheight:inputfeaturechannelcount:channelmultiplier:).md)
  Creates a descriptor for depthwise convolution with the kernel sizes, number of input feature channels, and channel multiplier you specify.
- [enum MLCConvolutionType](mlcconvolutiontype.md)
  The convolution type specified for a convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/init(type:kernelsizes:inputfeaturechannelcount:outputfeaturechannelcount:groupcount:strides:dilationrates:paddingpolicy:))*