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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/init(transposewithkernelwidth:kernelheight:inputfeaturechannelcount:outputfeaturechannelcount:))*