# MLCConvolutionType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

The convolution type specified for a convolution layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCConvolutionType
```

```c
enum MLCConvolutionType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCConvolutionType.standard](./mlcconvolutiontype/standard.md)
- [MLCConvolutionType.depthwise](./mlcconvolutiontype/depthwise.md)
- [MLCConvolutionType.transposed](./mlcconvolutiontype/transposed.md)
- [var debugDescription: String](./mlcconvolutiontype/debugdescription.md)
  A textual description of the convolution type, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlcconvolutiontype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Convolution Descriptors
- [convenience init(type: MLCConvolutionType, kernelSizes: (height: Int, width: Int), inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, groupCount: Int, strides: (y: Int, x: Int), dilationRates: (y: Int, x: Int), paddingPolicy: MLCPaddingPolicy)](./mlcconvolutiondescriptor/init%28type,kernelsizes,inputfeaturechannelcount,outputfeaturechannelcount,groupcount,strides,dilationrates,paddingpolicy%29.md)
  Creates a descriptor for the type, sizes, number of feature channels, group count, strides, dilation rates, and padding policy you specify.
- [convenience init(transposeWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int)](./mlcconvolutiondescriptor/init%28transposewithkernelwidth,kernelheight,inputfeaturechannelcount,outputfeaturechannelcount%29.md)
  Creates a descriptor for convolution transpose with the kernel sizes and number of feature channels you specify.
- [convenience init(depthwiseWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, channelMultiplier: Int)](./mlcconvolutiondescriptor/init%28depthwisewithkernelwidth,kernelheight,inputfeaturechannelcount,channelmultiplier%29.md)
  Creates a descriptor for depthwise convolution with the kernel sizes, number of input feature channels, and channel multiplier you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiontype)*