# BlendShapeWeights

**Framework**: RealityKit  
**Kind**: struct

A set of animatable weight values that collectively represent the blending amounts for all the blend shapes’ blend targets.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- visionOS 2.0+

## Declaration

```swift
struct BlendShapeWeights
```

## Topics

### Operators
- [static func == (BlendShapeWeights, BlendShapeWeights) -> Bool](blendshapeweights/==(_:_:).md)
  Returns a Boolean value that indicates whether two collections of weights are equal.
### Initializers
- [init()](blendshapeweights/init.md)
  Initializes a collection of animatable weights for a blend shape.
- [init<S>(S)](blendshapeweights/init(_:).md)
  Initializes a collection of weights for a single blend shape.
- [init(arrayLiteral: Float...)](blendshapeweights/init(arrayliteral:).md)
  Creates a collection of animatable weights using the argument elements for a blend shape.
### Instance Properties
- [var endIndex: BlendShapeWeights.Index](blendshapeweights/endindex.md)
  An index to the last weight in the collection.
- [var startIndex: BlendShapeWeights.Index](blendshapeweights/startindex.md)
  An index to the first weight in the collection.
### Instance Methods
- [func index(after: BlendShapeWeights.Index) -> BlendShapeWeights.Index](blendshapeweights/index(after:).md)
  Returns the position in the sequence of the weight that follows the given position.
- [func index(before: BlendShapeWeights.Index) -> BlendShapeWeights.Index](blendshapeweights/index(before:).md)
  Returns the position in the sequence of the weight that preceeds the given position.
### Subscripts
- [subscript(BlendShapeWeights.Index) -> Float](blendshapeweights/subscript(_:).md)
  Accesses a single weight in the collection at the given index.
### Type Aliases
- [BlendShapeWeights.ArrayLiteralElement](blendshapeweights/arrayliteralelement.md)
  The type of the elements of an array literal.
- [BlendShapeWeights.Element](blendshapeweights/element.md)
  An individual weight in the collection.
- [BlendShapeWeights.Index](blendshapeweights/index.md)
  A position of an individual weight in the collection.
- [BlendShapeWeights.Indices](blendshapeweights/indices.md)
  A type that represents the indices that are valid for subscripting the collection, in ascending order.
- [BlendShapeWeights.Iterator](blendshapeweights/iterator.md)
  A type that provides the collection’s iteration interface and encapsulates its iteration state.
- [BlendShapeWeights.SubSequence](blendshapeweights/subsequence.md)
  A collection representing a contiguous subrange of this collection’s elements. The subsequence shares indices with the original collection.
### Default Implementations
- [BidirectionalCollection Implementations](blendshapeweights/bidirectionalcollection-implementations.md)
- [Collection Implementations](blendshapeweights/collection-implementations.md)
- [Decodable Implementations](blendshapeweights/decodable-implementations.md)
- [Encodable Implementations](blendshapeweights/encodable-implementations.md)
- [Equatable Implementations](blendshapeweights/equatable-implementations.md)
- [MutableCollection Implementations](blendshapeweights/mutablecollection-implementations.md)
- [Sequence Implementations](blendshapeweights/sequence-implementations.md)

## Relationships

### Conforms To
- [AnimatableData](animatabledata.md)
- [BidirectionalCollection](../Swift/BidirectionalCollection.md)
- [Collection](../Swift/Collection.md)
- [Copyable](../Swift/Copyable.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [MutableCollection](../Swift/MutableCollection.md)
- [Sequence](../Swift/Sequence.md)

## See Also

- [struct BlendShapeWeightsComponent](blendshapeweightscomponent.md)
  A component that provides access to the current weights associated with all blend shape meshes on an entity.
- [class BlendShapeWeightsMapping](blendshapeweightsmapping.md)
  A mapping of blend weights to the target meshes that those weights affect.
- [struct BlendShapeWeightsData](blendshapeweightsdata.md)
  A structure that encapsulates the blend shape name, blend shape weights and the names of those weights to be stored by the blend shape weights set.
- [struct BlendShapeWeightsSet](blendshapeweightsset.md)
  A custom collection of named blend shape weights.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/blendshapeweights)*