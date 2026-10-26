# strideInY

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The kernel stride in `y`.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, readonly) NSUInteger strideInY;
```

## See Also

### Inspecting Convolution Descriptors
- [var convolutionType: MLCConvolutionType](./convolutiontype.md)
  The type of convolution.
- [kernelWidth](./kernelwidth.md)
  The kernel size in x.
- [kernelHeight](./kernelheight.md)
  The kernel size in y.
- [var inputFeatureChannelCount: Int](./inputfeaturechannelcount.md)
  The number of feature channels in the input tensor.
- [var outputFeatureChannelCount: Int](./outputfeaturechannelcount.md)
  The number of feature channels in the output tensor.
- [strideInX](./strideinx.md)
  The kernel stride in `x`.
- [dilationRateInX](./dilationrateinx.md)
  The dilation rate, or stride of elements, in the kernel in x.
- [dilationRateInY](./dilationrateiny.md)
  The dilation rate, or stride of elements, in the kernel in y.
- [var groupCount: Int](./groupcount.md)
  The number of groups.
- [paddingPolicy](./paddingpolicy-7drfq.md)
  The padding policy.
- [paddingSizeInX](./paddingsizeinx.md)
  The pooling size in x, left and right, to use if the padding policy is to use padding size.
- [paddingSizeInY](./paddingsizeiny.md)
  The pooling size in y, top and bottom, to use if the padding policy is to use padding size.
- [var isConvolutionTranspose: Bool](./isconvolutiontranspose.md)
  A Boolean that indicates whether this is a convolution transpose.
- [var usesDepthwiseConvolution: Bool](./usesdepthwiseconvolution.md)
  A Boolean that indicates whether you use depthwise convolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/strideiny)*