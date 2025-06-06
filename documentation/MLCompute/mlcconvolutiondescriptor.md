# MLCConvolutionDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create a convolution or fully connected layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCConvolutionDescriptor
```

## Topics

### Creating Convolution Descriptors
- [convenience init(type: MLCConvolutionType, kernelSizes: (height: Int, width: Int), inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, groupCount: Int, strides: (y: Int, x: Int), dilationRates: (y: Int, x: Int), paddingPolicy: MLCPaddingPolicy)](mlcconvolutiondescriptor/init(type:kernelsizes:inputfeaturechannelcount:outputfeaturechannelcount:groupcount:strides:dilationrates:paddingpolicy:).md)
  Creates a descriptor for the type, sizes, number of feature channels, group count, strides, dilation rates, and padding policy you specify.
- [convenience init(transposeWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int)](mlcconvolutiondescriptor/init(transposewithkernelwidth:kernelheight:inputfeaturechannelcount:outputfeaturechannelcount:).md)
  Creates a descriptor for convolution transpose with the kernel sizes and number of feature channels you specify.
- [convenience init(depthwiseWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, channelMultiplier: Int)](mlcconvolutiondescriptor/init(depthwisewithkernelwidth:kernelheight:inputfeaturechannelcount:channelmultiplier:).md)
  Creates a descriptor for depthwise convolution with the kernel sizes, number of input feature channels, and channel multiplier you specify.
- [enum MLCConvolutionType](mlcconvolutiontype.md)
  The convolution type specified for a convolution layer.
### Inspecting Convolution Descriptors
- [var convolutionType: MLCConvolutionType](mlcconvolutiondescriptor/convolutiontype.md)
  The type of convolution.
- [var kernelSizes: (height: Int, width: Int)](mlcconvolutiondescriptor/kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var inputFeatureChannelCount: Int](mlcconvolutiondescriptor/inputfeaturechannelcount.md)
  The number of feature channels in the input tensor.
- [var outputFeatureChannelCount: Int](mlcconvolutiondescriptor/outputfeaturechannelcount.md)
  The number of feature channels in the output tensor.
- [var strides: (y: Int, x: Int)](mlcconvolutiondescriptor/strides.md)
  A tuple that contains the kernel strides for y and x.
- [var dilationRates: (y: Int, x: Int)](mlcconvolutiondescriptor/dilationrates.md)
  A tuple that contains the dilation rates for y and x.
- [var groupCount: Int](mlcconvolutiondescriptor/groupcount.md)
  The number of groups.
- [var paddingPolicy: MLCPaddingPolicy](mlcconvolutiondescriptor/paddingpolicy-61tq3.md)
  The padding policy.
- [var isConvolutionTranspose: Bool](mlcconvolutiondescriptor/isconvolutiontranspose.md)
  A Boolean that indicates whether this is a convolution transpose.
- [var usesDepthwiseConvolution: Bool](mlcconvolutiondescriptor/usesdepthwiseconvolution.md)
  A Boolean that indicates whether you use depthwise convolution.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init?(weights: MLCTensor, biases: MLCTensor?, descriptor: MLCConvolutionDescriptor)](mlcconvolutionlayer/init(weights:biases:descriptor:).md)
  Creates a convolution layer with the weights, biases, and descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor)*