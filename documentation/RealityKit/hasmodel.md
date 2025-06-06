# HasModel

**Framework**: RealityKit  
**Kind**: protocol

An interface that provides meshes and materials to define the visual appearance of an entity.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasModel : HasTransform
```

## Topics

### Retrieving a model
- [var model: ModelComponent?](hasmodel/model.md)
  The model component for the entity.
### Managing joints
- [var jointNames: [String]](hasmodel/jointnames.md)
  The names of all the joints in the model entity.
- [var jointTransforms: [Transform]](hasmodel/jointtransforms.md)
  The relative joint transforms of the model entity.
### Instance Properties
- [var blendWeightNames: [[String]]](hasmodel/blendweightnames.md)
  The names of the weights on each blend shape in the model entity.
- [var blendWeights: [[Float]]](hasmodel/blendweights.md)
  The blend shape weights in the model entity.
- [var modelDebugOptions: ModelDebugOptionsComponent?](hasmodel/modeldebugoptions.md)
  Configures the debug visualization of this model.

## Relationships

### Inherits From
- [HasTransform](hastransform.md)
### Conforming Types
- [BodyTrackedEntity](bodytrackedentity.md)
- [ModelEntity](modelentity.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasmodel)*