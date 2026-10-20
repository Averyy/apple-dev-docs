# MLCConvolutionDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create a convolution or fully connected layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCConvolutionDescriptor
```

```objc
@interface MLCConvolutionDescriptor : NSObject
```

## Topics

### Creating Convolution Descriptors
- [convenience init(type: MLCConvolutionType, kernelSizes: (height: Int, width: Int), inputFeatureChannelCount: Int, outputFeatureChannelCount: Int, groupCount: Int, strides: (y: Int, x: Int), dilationRates: (y: Int, x: Int), paddingPolicy: MLCPaddingPolicy)](./mlcconvolutiondescriptor/init%28type,kernelsizes,inputfeaturechannelcount,outputfeaturechannelcount,groupcount,strides,dilationrates,paddingpolicy%29.md)
  Creates a descriptor for the type, sizes, number of feature channels, group count, strides, dilation rates, and padding policy you specify.
- [convenience init(transposeWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, outputFeatureChannelCount: Int)](./mlcconvolutiondescriptor/init%28transposewithkernelwidth,kernelheight,inputfeaturechannelcount,outputfeaturechannelcount%29.md)
  Creates a descriptor for convolution transpose with the kernel sizes and number of feature channels you specify.
- [convenience init(depthwiseWithKernelWidth: Int, kernelHeight: Int, inputFeatureChannelCount: Int, channelMultiplier: Int)](./mlcconvolutiondescriptor/init%28depthwisewithkernelwidth,kernelheight,inputfeaturechannelcount,channelmultiplier%29.md)
  Creates a descriptor for depthwise convolution with the kernel sizes, number of input feature channels, and channel multiplier you specify.
- [enum MLCConvolutionType](./mlcconvolutiontype.md)
  The convolution type specified for a convolution layer.
### Inspecting Convolution Descriptors
- [var convolutionType: MLCConvolutionType](./mlcconvolutiondescriptor/convolutiontype.md)
  The type of convolution.
- [var kernelSizes: (height: Int, width: Int)](./mlcconvolutiondescriptor/kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var inputFeatureChannelCount: Int](./mlcconvolutiondescriptor/inputfeaturechannelcount.md)
  The number of feature channels in the input tensor.
- [var outputFeatureChannelCount: Int](./mlcconvolutiondescriptor/outputfeaturechannelcount.md)
  The number of feature channels in the output tensor.
- [var strides: (y: Int, x: Int)](./mlcconvolutiondescriptor/strides.md)
  A tuple that contains the kernel strides for y and x.
- [var dilationRates: (y: Int, x: Int)](./mlcconvolutiondescriptor/dilationrates.md)
  A tuple that contains the dilation rates for y and x.
- [var groupCount: Int](./mlcconvolutiondescriptor/groupcount.md)
  The number of groups.
- [var paddingPolicy: MLCPaddingPolicy](./mlcconvolutiondescriptor/paddingpolicy-61tq3.md)
  The padding policy.
- [var isConvolutionTranspose: Bool](./mlcconvolutiondescriptor/isconvolutiontranspose.md)
  A Boolean that indicates whether this is a convolution transpose.
- [var usesDepthwiseConvolution: Bool](./mlcconvolutiondescriptor/usesdepthwiseconvolution.md)
  A Boolean that indicates whether you use depthwise convolution.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Convolution Layers
- [convenience init?(weights: MLCTensor, biases: MLCTensor?, descriptor: MLCConvolutionDescriptor)](./mlcconvolutionlayer/init%28weights,biases,descriptor%29.md)
  Creates a convolution layer with the weights, biases, and descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor)*