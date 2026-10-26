# init(transposeWithKernelWidth:kernelHeight:inputFeatureChannelCount:outputFeatureChannelCount:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a descriptor for convolution transpose with the kernel sizes and number of feature channels you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(transposeWithKernelWidth kernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int)
```

```objc
+ (instancetype) convolutionTransposeDescriptorWithKernelWidth:(NSUInteger) kernelWidth kernelHeight:(NSUInteger) kernelHeight inputFeatureChannelCount:(NSUInteger) inputFeatureChannelCount outputFeatureChannelCount:(NSUInteger) outputFeatureChannelCount;
```

## Parameters

- `kernelWidth`: The kernel size in x.
- `kernelHeight`: The kernel size in y.
- `inputFeatureChannelCount`: The number of feature channels in the input tensor.
- `outputFeatureChannelCount`: The number of feature channels in the output tensor.

## See Also

### Creating Convolution Descriptors
- [convenience init(type: MLCConvolutionType, kernelSizes: (height: Int, width: Int), inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, groupCount: Int, strides: (y: Int, x: Int), dilationRates: (y: Int, x: Int), paddingPolicy: MLCPaddingPolicy)](./init%28type,kernelsizes,inputfeaturechannelcount,outputfeaturechannelcount,groupcount,strides,dilationrates,paddingpolicy%29.md)
  Creates a descriptor for the type, sizes, number of feature channels, group count, strides, dilation rates, and padding policy you specify.
- [convenience init(depthwiseWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, channelMultiplier: Int)](./init%28depthwisewithkernelwidth,kernelheight,inputfeaturechannelcount,channelmultiplier%29.md)
  Creates a descriptor for depthwise convolution with the kernel sizes, number of input feature channels, and channel multiplier you specify.
- [enum MLCConvolutionType](../mlcconvolutiontype.md)
  The convolution type specified for a convolution layer.
- [+ descriptorWithKernelWidth:kernelHeight:inputFeatureChannelCount:outputFeatureChannelCount:](./descriptorwithkernelwidth_kernelheight_inputfeaturechannelcount_outputfeaturechannelcount_.md)
  Creates a convolution descriptor with the kernel sizes and number of feature channels you specify.
- [+ descriptorWithType:kernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:](./descriptorwithtype_kernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_groupcount_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a descriptor with the type, kernel sizes, number of feature channels and groups, strides, dilation rates, and padding policy you specify.
- [+ descriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:strides:paddingPolicy:paddingSizes:](./descriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_strides_paddingpolicy_paddingsizes_.md)
  Creates a convolution descriptor with the kernel sizes, number of feature channels, strides, padding policy, and padding sizes you specify.
- [+ convolutionTransposeDescriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:strides:paddingPolicy:paddingSizes:](./convolutiontransposedescriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_strides_paddingpolicy_paddingsizes_.md)
  Creates a convolution transpose descriptor with the kernel sizes, number of feature channels, strides, and padding options you specify.
- [+ convolutionTransposeDescriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:](./convolutiontransposedescriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_groupcount_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a convolution transpose descriptor with the kernel and padding options, number of feature channels and groups, and dilation rates you specify.
- [+ depthwiseConvolutionDescriptorWithKernelSizes:inputFeatureChannelCount:channelMultiplier:strides:paddingPolicy:paddingSizes:](./depthwiseconvolutiondescriptorwithkernelsizes_inputfeaturechannelcount_channelmultiplier_strides_paddingpolicy_paddingsizes_.md)
  Creates a depthwise convolution descriptor with the kernel and padding options, number of input feature channels, and channel multiplier you specify.
- [+ depthwiseConvolutionDescriptorWithKernelSizes:inputFeatureChannelCount:channelMultiplier:strides:dilationRates:paddingPolicy:paddingSizes:](./depthwiseconvolutiondescriptorwithkernelsizes_inputfeaturechannelcount_channelmultiplier_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a convolution descriptor with the kernel and padding options, number of input channels, channel multiplier, and dilation rates you specify.
- [+ descriptorWithKernelSizes:inputFeatureChannelCount:outputFeatureChannelCount:groupCount:strides:dilationRates:paddingPolicy:paddingSizes:](./descriptorwithkernelsizes_inputfeaturechannelcount_outputfeaturechannelcount_groupcount_strides_dilationrates_paddingpolicy_paddingsizes_.md)
  Creates a convolution descriptor with the kernel and padding options, number of feature channels and groups, and dilation rates you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/init(transposewithkernelwidth:kernelheight:inputfeaturechannelcount:outputfeaturechannelcount:))*