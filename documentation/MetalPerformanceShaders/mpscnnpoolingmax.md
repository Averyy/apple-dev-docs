# MPSCNNPoolingMax

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A max pooling filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingMax
```

```objc
@interface MPSCNNPoolingMax : MPSCNNPooling
```

## Overview

For each pixel in an image, the filter returns the maximum value of the pixels in the filter region defined by `kernelWidth` x `kernelHeight`.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnpoolingmax/init%28coder,device%29.md)
  Initializes a max pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](./mpscnnpoolingmax/init%28device,kernelwidth,kernelheight,strideinpixelsx,strideinpixelsy%29.md)
  Initializes a max pooling filter.

## Relationships

### Inherits From
- [MPSCNNPooling](./mpscnnpooling.md)
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
- [class MPSCNNDilatedPoolingMax](./mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
- [class MPSCNNPooling](./mpscnnpooling.md)
  A pooling kernel.
- [class MPSCNNPoolingGradient](./mpscnnpoolinggradient.md)
  A gradient pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradient](./mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](./mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](./mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingmax)*