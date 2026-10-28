# depthwiseConvolutionDescriptorWithKernelSizes:inputFeatureChannelCount:channelMultiplier:strides:paddingPolicy:paddingSizes:

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a depthwise convolution descriptor with the kernel and padding options, number of input feature channels, and channel multiplier you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
+ (instancetype) depthwiseConvolutionDescriptorWithKernelSizes:(NSArray<NSNumber *> *) kernelSizes inputFeatureChannelCount:(NSUInteger) inputFeatureChannelCount channelMultiplier:(NSUInteger) channelMultiplier strides:(NSArray<NSNumber *> *) strides paddingPolicy:(MLCPaddingPolicy) paddingPolicy paddingSizes:(NSArray<NSNumber *> *) paddingSizes;
```

## Return Value

A convolution descriptor.

## Parameters

- `kernelSizes`: An array that contains the kernel sizes for y and x.
- `inputFeatureChannelCount`: The number of feature channels in the input tensor.
- `channelMultiplier`: The channel multiplier.
- `strides`: An array that contains the kernel strides for y and x.
- `paddingPolicy`: The padding policy.
- `paddingSizes`: An array that contains the padding sizes for y and x, if the padding policy is to use padding size.

## See Also

### Creating Convolution Descriptors
- [+ descriptorWithKernelWidth:kernelHeight:inputFeatureChannelCount:outputFeatureChannelCount:](./descriptorwithkernelwidth_kernelheight_inputfeaturechannelcount_outputfeaturechannelcount_.md)
  Creates a convolution descriptor with the kernel sizes and number of feature channels you specify.
- [+ descriptorWithType:kernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:](./descriptorwithtype_kernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_groupcount_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a descriptor with the type, kernel sizes, number of feature channels and groups, strides, dilation rates, and padding policy you specify.
- [+ descriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:strides:paddingPolicy:paddingSizes:](./descriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_strides_paddingpolicy_paddingsizes_.md)
  Creates a convolution descriptor with the kernel sizes, number of feature channels, strides, padding policy, and padding sizes you specify.
- [convenience init(transposeWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int)](./init%28transposewithkernelwidth,kernelheight,inputfeaturechannelcount,outputfeaturechannelcount%29.md)
  Creates a descriptor for convolution transpose with the kernel sizes and number of feature channels you specify.
- [+ convolutionTransposeDescriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:strides:paddingPolicy:paddingSizes:](./convolutiontransposedescriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_strides_paddingpolicy_paddingsizes_.md)
  Creates a convolution transpose descriptor with the kernel sizes, number of feature channels, strides, and padding options you specify.
- [+ convolutionTransposeDescriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:](./convolutiontransposedescriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_groupcount_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a convolution transpose descriptor with the kernel and padding options, number of feature channels and groups, and dilation rates you specify.
- [convenience init(depthwiseWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, channelMultiplier: Int)](./init%28depthwisewithkernelwidth,kernelheight,inputfeaturechannelcount,channelmultiplier%29.md)
  Creates a descriptor for depthwise convolution with the kernel sizes, number of input feature channels, and channel multiplier you specify.
- [+ depthwiseConvolutionDescriptorWithKernelSizes:inputFeatureChannelCount:channelMultiplier:strides:dilationRates:paddingPolicy:paddingSizes:](./depthwiseconvolutiondescriptorwithkernelsizes_inputfeaturechannelcount_channelmultiplier_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a convolution descriptor with the kernel and padding options, number of input channels, channel multiplier, and dilation rates you specify.
- [+ descriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:](./descriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_groupcount_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a convolution descriptor with the kernel and padding options, number of feature channels and groups, and dilation rates you specify.
- [enum MLCConvolutionType](../mlcconvolutiontype.md)
  The convolution type specified for a convolution layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/depthwiseconvolutiondescriptorwithkernelsizes:inputfeaturechannelcount:channelmultiplier:strides:paddingpolicy:paddingsizes:)*