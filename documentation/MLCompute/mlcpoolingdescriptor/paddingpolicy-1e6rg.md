# paddingPolicy

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The padding policy.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, readonly) MLCPaddingPolicy paddingPolicy;
```

## See Also

### Inspecting Pooling Descriptors
- [poolingType](./poolingtype-9daku.md)
  The pooling operation type.
- [kernelWidth](./kernelwidth.md)
  The pooling kernel size in x.
- [kernelHeight](./kernelheight.md)
  The pooling kernel size in y.
- [strideInX](./strideinx.md)
  The stride of the kernel in x.
- [strideInY](./strideiny.md)
  The stride of the kernel in y.
- [dilationRateInX](./dilationrateinx.md)
  The kernel dilation rate, or stride of elements, in x.
- [dilationRateInY](./dilationrateiny.md)
  The kernel dilation rate, or stride of elements, in y.
- [paddingSizeInX](./paddingsizeinx.md)
  The padding size in x, left and right, to use if the padding policy is to use padding size.
- [paddingSizeInY](./paddingsizeiny.md)
  The padding size in y, top and bottom, to use if the padding policy is to use padding size.
- [countIncludesPadding](./countincludespadding.md)
  A Boolean that indicates whether you include zero padding in the averaging calculation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolingdescriptor/paddingpolicy-1e6rg)*