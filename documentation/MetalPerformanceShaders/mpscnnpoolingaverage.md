# MPSCNNPoolingAverage

**Framework**: Metal Performance Shaders  
**Kind**: class

An average pooling filter.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 10.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingAverage
```

#### Overview

For each pixel in an image, the filter returns the average value of the pixels in the filter region defined by `kernelWidth` `x` `kernelHeight`.

When the value of the [`edgeMode`](mpscnnkernel/edgemode.md) property is set to [`MPSImageEdgeMode.clamp`](mpsimageedgemode/clamp.md), the filtering window is shrunk to remain within the source image borders. For pixels close to the image borders, the filtering window will be smaller in order to fit inside the source image and less values will be used to compute the average value. In case the filtering window is entirely outside the source image border, the output value will be `0`.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnpoolingaverage/init(coder:device:).md)
  Initializes an average pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpoolingaverage/init(device:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:).md)
  Initializes an average pooling filter.
### Instance Properties
- [var zeroPadSizeX: Int](mpscnnpoolingaverage/zeropadsizex.md)
- [var zeroPadSizeY: Int](mpscnnpoolingaverage/zeropadsizey.md)

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

- [class MPSCNNPoolingAverageGradient](mpscnnpoolingaveragegradient.md)
  A gradient average pooling filter.
- [class MPSCNNPoolingL2Norm](mpscnnpoolingl2norm.md)
  An L2-norm pooling filter.
- [class MPSCNNPoolingMax](mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNDilatedPoolingMax](mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingaverage)*