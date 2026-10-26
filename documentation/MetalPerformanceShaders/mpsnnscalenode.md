# MPSNNScaleNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

Abstract node representing an image resampling filter.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSNNScaleNode
```

```objc
@interface MPSNNScaleNode : MPSNNFilterNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, outputSize: MTLSize)](./mpsnnscalenode/init%28source,outputsize%29.md)
- [init(source: MPSNNImageNode, transformProvider: (any MPSImageTransformProvider)?, outputSize: MTLSize)](./mpsnnscalenode/init%28source,transformprovider,outputsize%29.md)
### Type Methods
- [+ nodeWithSource:outputSize:](./mpsnnscalenode/nodewithsource_outputsize_.md)
- [+ nodeWithSource:transformProvider:outputSize:](./mpsnnscalenode/nodewithsource_transformprovider_outputsize_.md)

## Relationships

### Inherits From
- [MPSNNFilterNode](./mpsnnfilternode.md)
### Inherited By
- [MPSNNBilinearScaleNode](./mpsnnbilinearscalenode.md)
- [MPSNNLanczosScaleNode](./mpsnnlanczosscalenode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Resampling Nodes
- [class MPSNNBilinearScaleNode](./mpsnnbilinearscalenode.md)
  A representation of a bilinear resampling filter.
- [class MPSNNLanczosScaleNode](./mpsnnlanczosscalenode.md)
  A representation of a Lanczos resampling filter.
- [protocol MPSImageTransformProvider](./mpsimagetransformprovider.md)
  A general interface for objects that provide image resampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnscalenode)*