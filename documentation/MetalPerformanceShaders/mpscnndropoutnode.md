# MPSCNNDropoutNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropoutNode
```

```objc
@interface MPSCNNDropoutNode : MPSNNFilterNode
```

## Topics

### Initializers
- [convenience init(source: MPSNNImageNode)](./mpscnndropoutnode/init%28source%29.md)
- [convenience init(source: MPSNNImageNode, keepProbability: Float)](./mpscnndropoutnode/init%28source,keepprobability%29.md)
- [init(source: MPSNNImageNode, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](./mpscnndropoutnode/init%28source,keepprobability,seed,maskstrideinpixels%29.md)
### Instance Properties
- [var keepProbability: Float](./mpscnndropoutnode/keepprobability.md)
- [var maskStrideInPixels: MTLSize](./mpscnndropoutnode/maskstrideinpixels.md)
- [var seed: Int](./mpscnndropoutnode/seed.md)
### Type Methods
- [+ nodeWithSource:](./mpscnndropoutnode/nodewithsource_.md)
- [+ nodeWithSource:keepProbability:](./mpscnndropoutnode/nodewithsource_keepprobability_.md)
- [+ nodeWithSource:keepProbability:seed:maskStrideInPixels:](./mpscnndropoutnode/nodewithsource_keepprobability_seed_maskstrideinpixels_.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](./mpsnnfilternode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Dropout Layer Nodes
- [class MPSCNNDropoutGradientNode](./mpscnndropoutgradientnode.md)
  A representation of a gradient dropout filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutnode)*