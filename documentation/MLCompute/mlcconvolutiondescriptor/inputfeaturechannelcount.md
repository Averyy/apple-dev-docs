# inputFeatureChannelCount

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of feature channels in the input tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var inputFeatureChannelCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger inputFeatureChannelCount;
```

## See Also

### Inspecting Convolution Descriptors
- [var convolutionType: MLCConvolutionType](./convolutiontype.md)
  The type of convolution.
- [var kernelSizes: (height: Int, width: Int)](./kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var outputFeatureChannelCount: Int](./outputfeaturechannelcount.md)
  The number of feature channels in the output tensor.
- [var strides: (y: Int, x: Int)](./strides.md)
  A tuple that contains the kernel strides for y and x.
- [var dilationRates: (y: Int, x: Int)](./dilationrates.md)
  A tuple that contains the dilation rates for y and x.
- [var groupCount: Int](./groupcount.md)
  The number of groups.
- [var paddingPolicy: MLCPaddingPolicy](./paddingpolicy-61tq3.md)
  The padding policy.
- [var isConvolutionTranspose: Bool](./isconvolutiontranspose.md)
  A Boolean that indicates whether this is a convolution transpose.
- [var usesDepthwiseConvolution: Bool](./usesdepthwiseconvolution.md)
  A Boolean that indicates whether you use depthwise convolution.
- [kernelWidth](./kernelwidth.md)
  The kernel size in x.
- [kernelHeight](./kernelheight.md)
  The kernel size in y.
- [strideInX](./strideinx.md)
  The kernel stride in `x`.
- [strideInY](./strideiny.md)
  The kernel stride in `y`.
- [dilationRateInX](./dilationrateinx.md)
  The dilation rate, or stride of elements, in the kernel in x.
- [dilationRateInY](./dilationrateiny.md)
  The dilation rate, or stride of elements, in the kernel in y.
- [paddingPolicy](./paddingpolicy-7drfq.md)
  The padding policy.
- [paddingSizeInX](./paddingsizeinx.md)
  The pooling size in x, left and right, to use if the padding policy is to use padding size.
- [paddingSizeInY](./paddingsizeiny.md)
  The pooling size in y, top and bottom, to use if the padding policy is to use padding size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/inputfeaturechannelcount)*