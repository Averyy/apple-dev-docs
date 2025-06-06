# BlendShapeWeightsData

**Framework**: RealityKit  
**Kind**: struct

A structure that encapsulates the blend shape name, blend shape weights and the names of those weights to be stored by the blend shape weights set.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct BlendShapeWeightsData
```

## Topics

### Initializers
- [init(id: BlendShapeWeightsData.ID, weights: [(String, BlendShapeWeights.Element)])](blendshapeweightsdata/init(id:weights:).md)
  Creates an instance of the named weights for a single blend shape.
### Instance Properties
- [var id: BlendShapeWeightsData.ID](blendshapeweightsdata/id-swift.property.md)
  The unique id of the blend shape. This value is used when binding to the structure using an animation bind target.
- [var weightNames: [String]](blendshapeweightsdata/weightnames.md)
  The name of each weight value defined in the [`weights`](blendshapeweightsdata/weights.md) variable.
- [var weights: BlendShapeWeights](blendshapeweightsdata/weights.md)
  The blend shape’s weight values.
### Type Aliases
- [BlendShapeWeightsData.ID](blendshapeweightsdata/id-swift.typealias.md)
  A type representing the stable identity of the entity associated with an instance.

## Relationships

### Conforms To
- [Identifiable](../Swift/Identifiable.md)

## See Also

- [struct BlendShapeWeightsComponent](blendshapeweightscomponent.md)
  A component that provides access to the current weights associated with all blend shape meshes on an entity.
- [class BlendShapeWeightsMapping](blendshapeweightsmapping.md)
  A mapping of blend weights to the target meshes that those weights affect.
- [struct BlendShapeWeights](blendshapeweights.md)
  A set of animatable weight values that collectively represent the blending amounts for all the blend shapes’ blend targets.
- [struct BlendShapeWeightsSet](blendshapeweightsset.md)
  A custom collection of named blend shape weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweightsdata)*