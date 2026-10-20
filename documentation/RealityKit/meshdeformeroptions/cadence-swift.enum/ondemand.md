# MeshDeformerOptions.Cadence.onDemand

**Framework**: RealityKit  
**Kind**: case  
**Role**: Case

Applies the custom deformer function only when you request it. You can explicitly request the deformer function to be called by setting new input. Like all other deformers, the deformer updates again if a previous deformer in the `MeshDeformationStack` updates.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+

## Declaration

```swift
case onDemand
```

## See Also

### Choosing an update cadence
- [MeshDeformerOptions.Cadence.everyFrame](./everyframe.md)
  Applies the custom deformer function automatically, every frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/meshdeformeroptions/cadence-swift.enum/ondemand)*