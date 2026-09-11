# MeshDeformerOptions.Cadence

**Framework**: RealityKit  
**Kind**: enum

Specifies when RealityKit applies the custom deformer functions.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
enum Cadence
```

## Topics

### Choosing an update cadence
- [MeshDeformerOptions.Cadence.everyFrame](meshdeformeroptions/cadence-swift.enum/everyframe.md)
  Applies the custom deformer function automatically, every frame.
- [MeshDeformerOptions.Cadence.onDemand](meshdeformeroptions/cadence-swift.enum/ondemand.md)
  Applies the custom deformer function only when you request it. You can explicitly request the deformer function to be called by setting new input. Like all other deformers, the deformer updates again if a previous deformer in the `MeshDeformationStack` updates.

## Relationships

### Conforms To
- [Decodable](../swift/decodable.md)
- [Encodable](../swift/encodable.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [let cadence: MeshDeformerOptions.Cadence](meshdeformeroptions/cadence-swift.property.md)
  Determines the update frequence for the defomer type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformeroptions/cadence-swift.enum)*