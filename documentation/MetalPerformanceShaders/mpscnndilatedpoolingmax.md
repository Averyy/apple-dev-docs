# MPSCNNDilatedPoolingMax

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A dilated max pooling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDilatedPoolingMax
```

```objc
@interface MPSCNNDilatedPoolingMax : MPSCNNPooling
```

## Overview

For each pixel, returns the maximum value of pixels in the `kernelWidth * kernelHeight` filter region by step size `dilationFactorX` `*` `dilationFactorY`.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnndilatedpoolingmax/init%28coder,device%29.md)
  Initializes a dilated max pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, dilationRateX: Int, dilationRateY: Int, strideInPixelsX: Int, strideInPixelsY: Int)](./mpscnndilatedpoolingmax/init%28device,kernelwidth,kernelheight,dilationratex,dilationratey,strideinpixelsx,strideinpixelsy%29.md)
  Initializes a dilated max pooling filter.
### Instance Properties
- [var dilationRateX: Int](./mpscnndilatedpoolingmax/dilationratex.md)
- [var dilationRateY: Int](./mpscnndilatedpoolingmax/dilationratey.md)

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
- [class MPSCNNPoolingMax](./mpscnnpoolingmax.md)
  A max pooling filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmax)*