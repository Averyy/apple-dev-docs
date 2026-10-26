# MPSCNNDropoutGradientNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a gradient dropout filter.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNDropoutGradientNode
```

```objc
@interface MPSCNNDropoutGradientNode : MPSNNGradientFilterNode
```

## Topics

### Initializers
- [init(sourceGradient: MPSNNImageNode, sourceImage: MPSNNImageNode, gradientState: MPSNNGradientStateNode, keepProbability: Float, seed: Int, maskStrideInPixels: MTLSize)](./mpscnndropoutgradientnode/init%28sourcegradient,sourceimage,gradientstate,keepprobability,seed,maskstrideinpixels%29.md)
### Instance Properties
- [var keepProbability: Float](./mpscnndropoutgradientnode/keepprobability.md)
- [var maskStrideInPixels: MTLSize](./mpscnndropoutgradientnode/maskstrideinpixels.md)
- [var seed: Int](./mpscnndropoutgradientnode/seed.md)
### Type Methods
- [+ nodeWithSourceGradient:sourceImage:gradientState:keepProbability:seed:maskStrideInPixels:](./mpscnndropoutgradientnode/nodewithsourcegradient_sourceimage_gradientstate_keepprobability_seed_maskstrideinpixels_.md)

## Relationships

### Inherits From
- [MPSNNGradientFilterNode](./mpsnngradientfilternode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Dropout Layer Nodes
- [class MPSCNNDropoutNode](./mpscnndropoutnode.md)
  A representation of a dropout filter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnndropoutgradientnode)*