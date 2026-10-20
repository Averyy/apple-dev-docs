# groupCount

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The number of groups.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var groupCount: Int { get }
```

```objc
@property (nonatomic, readonly) NSUInteger groupCount;
```

## See Also

### Inspecting Convolution Descriptors
- [var convolutionType: MLCConvolutionType](./convolutiontype.md)
  The type of convolution.
- [var kernelSizes: (height: Int, width: Int)](./kernelsizes.md)
  A tuple that contains the kernel sizes for height and width.
- [var inputFeatureChannelCount: Int](./inputfeaturechannelcount.md)
  The number of feature channels in the input tensor.
- [var outputFeatureChannelCount: Int](./outputfeaturechannelcount.md)
  The number of feature channels in the output tensor.
- [var strides: (y: Int, x: Int)](./strides.md)
  A tuple that contains the kernel strides for y and x.
- [var dilationRates: (y: Int, x: Int)](./dilationrates.md)
  A tuple that contains the dilation rates for y and x.
- [var paddingPolicy: MLCPaddingPolicy](./paddingpolicy-61tq3.md)
  The padding policy.
- [var isConvolutionTranspose: Bool](./isconvolutiontranspose.md)
  A Boolean that indicates whether this is a convolution transpose.
- [var usesDepthwiseConvolution: Bool](./usesdepthwiseconvolution.md)
  A Boolean that indicates whether you use depthwise convolution.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutiondescriptor/groupcount)*