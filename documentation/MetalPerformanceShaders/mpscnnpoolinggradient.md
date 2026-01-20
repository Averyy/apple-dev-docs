# MPSCNNPoolingGradient

**Framework**: Metal Performance Shaders  
**Kind**: class

A gradient pooling kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNPoolingGradient
```

## Topics

### Initializers
- [init?(coder: NSCoder, device: any MTLDevice)](mpscnnpoolinggradient/init(coder:device:).md)
- [convenience init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int)](mpscnnpoolinggradient/init(device:kernelwidth:kernelheight:).md)
- [init(device: any MTLDevice, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int)](mpscnnpoolinggradient/init(device:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:).md)
### Instance Properties
- [var sourceSize: MTLSize](mpscnnpoolinggradient/sourcesize.md)

## Relationships

### Inherits From
- [MPSCNNGradientKernel](mpscnngradientkernel.md)
### Inherited By
- [MPSCNNDilatedPoolingMaxGradient](mpscnndilatedpoolingmaxgradient.md)
- [MPSCNNPoolingAverageGradient](mpscnnpoolingaveragegradient.md)
- [MPSCNNPoolingL2NormGradient](mpscnnpoolingl2normgradient.md)
- [MPSCNNPoolingMaxGradient](mpscnnpoolingmaxgradient.md)
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
- [class MPSCNNPoolingMax](mpscnnpoolingmax.md)
  A max pooling filter.
- [class MPSCNNDilatedPoolingMax](mpscnndilatedpoolingmax.md)
  A dilated max pooling filter.
- [class MPSCNNPooling](mpscnnpooling.md)
  A pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradient](mpscnndilatedpoolingmaxgradient.md)
  A gradient dilated max pooling filter.
- [class MPSCNNPoolingL2NormGradient](mpscnnpoolingl2normgradient.md)
  A gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradient](mpscnnpoolingmaxgradient.md)
  A gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnpoolinggradient)*