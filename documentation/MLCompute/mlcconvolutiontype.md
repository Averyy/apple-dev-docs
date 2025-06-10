# MLCConvolutionType

**Framework**: ML Compute  
**Kind**: enum

The convolution type specified for a convolution layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCConvolutionType
```

## Topics

### Enumeration Cases
- [MLCConvolutionType.standard](mlcconvolutiontype/standard.md)
- [MLCConvolutionType.depthwise](mlcconvolutiontype/depthwise.md)
- [MLCConvolutionType.transposed](mlcconvolutiontype/transposed.md)
- [var debugDescription: String](mlcconvolutiontype/debugdescription.md)
  A textual description of the convolution type, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](mlcconvolutiontype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init(type: MLCConvolutionType, kernelSizes: (height: Int, width: Int), inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, groupCount: Int, strides: (y: Int, x: Int), dilationRates: (y: Int, x: Int), paddingPolicy: MLCPaddingPolicy)](mlcconvolutiondescriptor/init(type:kernelsizes:inputfeaturechannelcount:outputfeaturechannelcount:groupcount:strides:dilationrates:paddingpolicy:).md)
  Creates a descriptor for the type, sizes, number of feature channels, group count, strides, dilation rates, and padding policy you specify.
- [convenience init(transposeWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int)](mlcconvolutiondescriptor/init(transposewithkernelwidth:kernelheight:inputfeaturechannelcount:outputfeaturechannelcount:).md)
  Creates a descriptor for convolution transpose with the kernel sizes and number of feature channels you specify.
- [convenience init(depthwiseWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, channelMultiplier: Int)](mlcconvolutiondescriptor/init(depthwisewithkernelwidth:kernelheight:inputfeaturechannelcount:channelmultiplier:).md)
  Creates a descriptor for depthwise convolution with the kernel sizes, number of input feature channels, and channel multiplier you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiontype)*