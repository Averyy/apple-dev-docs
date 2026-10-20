# MPSCNNDilatedPoolingMaxGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A gradient dilated max pooling filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDilatedPoolingMaxGradient
```

```objc
@interface MPSCNNDilatedPoolingMaxGradient : MPSCNNPoolingGradient
```

#### Overview

A gradient max pooling filter but the pixels selected in each “application” of the max pooling operation are exactly the same pixels that would be selected with dilated convolution

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnndilatedpoolingmaxgradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, dilationRateX: Int, dilationRateY: Int, strideInPixelsX: Int, strideInPixelsY: Int)](./mpscnndilatedpoolingmaxgradient/init%28device,kernelwidth,kernelheight,dilationratex,dilationratey,strideinpixelsx,strideinpixelsy%29.md)

## Relationships

### Inherits From
- [MPSCNNPoolingGradient](./mpscnnpoolinggradient.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCoding](../Foundation/nscoding.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)
- [NSSecureCoding](../Foundation/nssecurecoding.md)

## See Also

### Pooling Layers
- [class MPSCNNPoolingAverage](./mpscnnpoolingaverage.md)
  An average pooling filter.
- [class MPSCNNPoolingAverageGradient](./mpscnnpoolingaveragegradient.md)
  A gradient average pooling filter.
- [class MPSCNNPoolingL2Norm](./mpscnnpoolingl2norm.md)
  An L2-norm pooling filter.
- [class MPSCNNPoolingMax](./mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNDilatedPoolingMax](./mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
- [class MPSCNNPooling](./mpscnnpooling.md)
  A pooling kernel.
- [class MPSCNNPoolingGradient](./mpscnnpoolinggradient.md)
  A gradient pooling kernel.
- [class MPSCNNPoolingL2NormGradient](./mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](./mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmaxgradient)*