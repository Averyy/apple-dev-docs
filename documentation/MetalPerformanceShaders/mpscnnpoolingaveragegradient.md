# MPSCNNPoolingAverageGradient

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A gradient average pooling filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingAverageGradient
```

```objc
@interface MPSCNNPoolingAverageGradient : MPSCNNPoolingGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](./mpscnnpoolingaveragegradient/init%28coder,device%29.md)
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](./mpscnnpoolingaveragegradient/init%28device,kernelwidth,kernelheight,strideinpixelsx,strideinpixelsy%29.md)
### Instance Properties
- [var zeroPadSizeX: Int](./mpscnnpoolingaveragegradient/zeropadsizex.md)
- [var zeroPadSizeY: Int](./mpscnnpoolingaveragegradient/zeropadsizey.md)

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
- [class MPSCNNDilatedPoolingMaxGradient](./mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](./mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](./mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingaveragegradient)*