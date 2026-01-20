# MPSCNNPoolingMax

**Framework**: Metal Performance Shaders  
**Kind**: class

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

#### Overview

For each pixel in an image, the filter returns the maximum value of the pixels in the filter region defined by `kernelWidth` x `kernelHeight`.

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnpoolingmax/init(coder:device:).md)
  Initializes a max pooling filter.
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpoolingmax/init(device:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:).md)
  Initializes a max pooling filter.

## Relationships

### Inherits From
- [MPSCNNPooling](mpscnnpooling.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCoding](../Foundation/NSCoding.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)
- [NSSecureCoding](../Foundation/NSSecureCoding.md)

## See Also

- [class MPSCNNPoolingAverage](mpscnnpoolingaverage.md)
  An average pooling filter.
- [class MPSCNNPoolingAverageGradient](mpscnnpoolingaveragegradient.md)
  A gradient average pooling filter.
- [class MPSCNNPoolingL2Norm](mpscnnpoolingl2norm.md)
  An L2-norm pooling filter.
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

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolingmax)*