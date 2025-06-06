# outputFeatureChannelCount

**Framework**: ML Compute  
**Kind**: property

The number of feature channels in the output tensor.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var outputFeatureChannelCount: Int { get }
```

## See Also

- [var convolutionType: MLCConvolutionType](mlcconvolutiondescriptor/convolutiontype.md)
  The type of convolution.
- [var kernelSizes: (height: Int, width: Int)](mlcconvolutiondescriptor/kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var inputFeatureChannelCount: Int](mlcconvolutiondescriptor/inputfeaturechannelcount.md)
  The number of feature channels in the input tensor.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/outputfeaturechannelcount)*