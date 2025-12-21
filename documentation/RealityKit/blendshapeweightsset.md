# BlendShapeWeightsSet

**Framework**: RealityKit  
**Kind**: struct

A custom collection of named blend shape weights.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+
- visionOS 2.0+

## Declaration

```swift
struct BlendShapeWeightsSet
```

#### Overview

Retrieve a `BlendShapeWeightsSet` from a [`BlendShapeWeightsComponent`](blendshapeweightscomponent.md) to access the current weights and weight names for each blend shape managed by the component.

Set the current weights for a blend shape by assigning a `BlendShapeWeightsSet` to a [`BlendShapeWeightsComponent`](blendshapeweightscomponent.md) for a specific blend shape.

The collection allows:

- Access to elements by name.
- Protection that prohibits updating an element, where such an update would try to rename the stored element.

[`BlendShapeWeightsSet`](blendshapeweightsset.md) does not support addition/removal of elements, as the blend shape weights are defined in the asset and the number and names of the weights are immutable.

## Topics

### Initializers
- [init()](blendshapeweightsset/init.md)
  Creates an empty set.
### Instance Properties
- [var count: Int](blendshapeweightsset/count.md)
  Number of blend shape weight data in the set.
- [var `default`: BlendShapeWeightsSet.Element?](blendshapeweightsset/default.md)
  The blend shape weights data set that drives the model.
- [var isEmpty: Bool](blendshapeweightsset/isempty.md)
  Checks if the set contains any blend shape weights data.
### Instance Methods
- [func contains(String) -> Bool](blendshapeweightsset/contains(_:).md)
  Checks if the set contains a blend shape weights data instance with the given name.
- [func index(of: String) -> BlendShapeWeightsSet.Index?](blendshapeweightsset/index(of:).md)
  Returns the index where the specified blend shape weights data appears in the collection.
- [func set(BlendShapeWeightsSet.Element) -> BlendShapeWeightsSet.Element?](blendshapeweightsset/set(_:).md)
  Updates a blend shape weights data instance in the set based on its name. If blend shape weights data with this ID does not exist, does nothing.
### Subscripts
- [subscript(_:)](blendshapeweightsset/subscript(_:).md)
  Accessor for reading a blend shape weights data in the set.
### Default Implementations
- [Collection Implementations](blendshapeweightsset/collection-implementations.md)

## Relationships

### Conforms To
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct BlendShapeWeightsComponent](blendshapeweightscomponent.md)
  A component that provides access to the current weights associated with all blend shape meshes on an entity.
- [class BlendShapeWeightsMapping](blendshapeweightsmapping.md)
  A mapping of blend weights to the target meshes that those weights affect.
- [struct BlendShapeWeights](blendshapeweights.md)
  A set of animatable weight values that collectively represent the blending amounts for all the blend shapes’ blend targets.
- [struct BlendShapeWeightsData](blendshapeweightsdata.md)
  A structure that encapsulates the blend shape name, blend shape weights and the names of those weights to be stored by the blend shape weights set.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweightsset)*