# MPSCNNDilatedPoolingMax

**Framework**: Metal Performance Shaders  
**Kind**: class

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

#### Overview

For each pixel, returns the maximum value of pixels in the `kernelWidth * kernelHeight` filter region by step size `dilationFactorX` `*` `dilationFactorY`.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnndilatedpoolingmax/init(coder:device:).md)
  Initializes a dilated max pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, dilationRateX: Int, dilationRateY: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnndilatedpoolingmax/init(device:kernelwidth:kernelheight:dilationratex:dilationratey:strideinpixelsx:strideinpixelsy:).md)
  Initializes a dilated max pooling filter.
### Instance Properties
- [var dilationRateX: Int](mpscnndilatedpoolingmax/dilationratex.md)
- [var dilationRateY: Int](mpscnndilatedpoolingmax/dilationratey.md)

## Relationships

### Inherits From
- [MPSCNNPooling](mpscnnpooling.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCoding](../foundation/nscoding.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)
- [NSSecureCoding](../foundation/nssecurecoding.md)

## See Also

- [class MPSCNNPoolingAverage](mpscnnpoolingaverage.md)
  An average pooling filter.
- [class MPSCNNPoolingAverageGradient](mpscnnpoolingaveragegradient.md)
  A gradient average pooling filter.
- [class MPSCNNPoolingL2Norm](mpscnnpoolingl2norm.md)
  An L2-norm pooling filter.
- [class MPSCNNPoolingMax](mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNPooling](mpscnnpooling.md)
  A pooling kernel.
- [class MPSCNNPoolingGradient](mpscnnpoolinggradient.md)
  A gradient pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradient](mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmax)*