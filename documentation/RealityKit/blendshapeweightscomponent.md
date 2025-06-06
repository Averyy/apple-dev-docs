# BlendShapeWeightsComponent

**Framework**: RealityKit  
**Kind**: struct

A component that provides access to the current weights associated with all blend shape meshes on an entity.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct BlendShapeWeightsComponent
```

#### Overview

You can access the weights associated with an entity’s blend shapes by using the [`weightSet`](blendshapeweightscomponent/weightset.md) variable after an initialized `BlendShapeWeightsComponent` is added to an entity.

```swift
let blendShapeWeightsComponent = BlendShapeWeightsComponent(
    weightsMapping: weightsMapping)
entity.components.set(blendShapeWeightsComponent)
let weightValues: [Float] = [0.3, 0.8]
entity.components[BlendShapeWeightsComponent.self]!.weightSets[0].weights
    = weightValues
```

## Topics

### Initializers
- [init(weightsMapping: BlendShapeWeightsMapping)](blendshapeweightscomponent/init(weightsmapping:).md)
  Create a BlendShapeWeightsComponent from a BlendShapeWeightsMapping.
### Instance Properties
- [var weightSet: BlendShapeWeightsSet](blendshapeweightscomponent/weightset.md)
  The runtime named blend shapes weights.
### Default Implementations
- [Component Implementations](blendshapeweightscomponent/component-implementations.md)

## Relationships

### Conforms To
- [Component](component.md)

## See Also

- [class BlendShapeWeightsMapping](blendshapeweightsmapping.md)
  A mapping of blend weights to the target meshes that those weights affect.
- [struct BlendShapeWeights](blendshapeweights.md)
  A set of animatable weight values that collectively represent the blending amounts for all the blend shapes’ blend targets.
- [struct BlendShapeWeightsData](blendshapeweightsdata.md)
  A structure that encapsulates the blend shape name, blend shape weights and the names of those weights to be stored by the blend shape weights set.
- [struct BlendShapeWeightsSet](blendshapeweightsset.md)
  A custom collection of named blend shape weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweightscomponent)*