# MPSNNScaleNode

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init(source: MPSNNImageNode, outputSize: MTLSize)](mpsnnscalenode/init(source:outputsize:).md)
- [init(source: MPSNNImageNode, transformProvider: (any MPSImageTransformProvider)?, outputSize: MTLSize)](mpsnnscalenode/init(source:transformprovider:outputsize:).md)

## Relationships

### Inherits From
- [MPSNNFilterNode](mpsnnfilternode.md)
### Inherited By
- [MPSNNBilinearScaleNode](mpsnnbilinearscalenode.md)
- [MPSNNLanczosScaleNode](mpsnnlanczosscalenode.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## See Also

- [class MPSNNBilinearScaleNode](mpsnnbilinearscalenode.md)
  A representation of a bilinear resampling filter.
- [class MPSNNLanczosScaleNode](mpsnnlanczosscalenode.md)
  A representation of a Lanczos resampling filter.
- [protocol MPSImageTransformProvider](mpsimagetransformprovider.md)
  A general interface for objects that provide image resampling.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpsnnscalenode)*