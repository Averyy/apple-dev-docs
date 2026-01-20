# MPSCNNDilatedPoolingMaxNode

**Framework**: Metal Performance Shaders  
**Kind**: class

A representation of a dilated max pooling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDilatedPoolingMaxNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, filterSize: Int)](mpscnndilatedpoolingmaxnode/init(source:filtersize:).md)
- [init(source: MPSNNImageNode, filterSize: Int, stride: Int, dilationRate: Int)](mpscnndilatedpoolingmaxnode/init(source:filtersize:stride:dilationrate:).md)
- [init(source: MPSNNImageNode, kernelWidth: Int, kernelHeight: Int, strideInPixelsX: Int, strideInPixelsY: Int, dilationRateX: Int, dilationRateY: Int)](mpscnndilatedpoolingmaxnode/init(source:kernelwidth:kernelheight:strideinpixelsx:strideinpixelsy:dilationratex:dilationratey:).md)
### Instance Properties
- [var dilationRateX: Int](mpscnndilatedpoolingmaxnode/dilationratex.md)
- [var dilationRateY: Int](mpscnndilatedpoolingmaxnode/dilationratey.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNPoolingAverageNode](mpscnnpoolingaveragenode.md)
  A representation of an average pooling filter.
- [class MPSCNNPoolingL2NormNode](mpscnnpoolingl2normnode.md)
  A representation of a L2-norm pooling filter.
- [class MPSCNNPoolingMaxNode](mpscnnpoolingmaxnode.md)
  A representation of a max pooling filter.
- [class MPSCNNPoolingNode](mpscnnpoolingnode.md)
  A representation of a MPS CNN pooling kernel.
- [class MPSCNNDilatedPoolingMaxGradientNode](mpscnndilatedpoolingmaxgradientnode.md)
  A representation of a gradient dilated max pooling filter.
- [class MPSCNNPoolingAverageGradientNode](mpscnnpoolingaveragegradientnode.md)
  A representation of a gradient average pooling filter.
- [class MPSCNNPoolingGradientNode](mpscnnpoolinggradientnode.md)
  A representation of a gradient pooling kernel.
- [class MPSCNNPoolingL2NormGradientNode](mpscnnpoolingl2normgradientnode.md)
  A representation of a gradient L2-norm pooling filter.
- [class MPSCNNPoolingMaxGradientNode](mpscnnpoolingmaxgradientnode.md)
  A representation of a gradient max pooling filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndilatedpoolingmaxnode)*