# MLRecommender.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The algorithms a recommender can use to make recommendations.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Recommender algorithms
- [MLRecommender.ModelAlgorithmType.itemSimilarity(_:)](./modelalgorithmtype/itemsimilarity%28_%29.md)
  An algorithm that compares the similarity from item to item.
- [MLRecommender.SimilarityType](./similaritytype.md)
  The metric by which the recommender computes item similarity.
### Algorithm descriptions
- [var description: String](./modelalgorithmtype/description.md)
  A text representation of the recommender algorithm.
- [var debugDescription: String](./modelalgorithmtype/debugdescription.md)
  A text representation of the recommender algorithm that’s suitable for output during debugging.
- [var playgroundDescription: Any](./modelalgorithmtype/playgrounddescription.md)
  A description of the recommender algorithm shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLRecommender.SimilarityType](./similaritytype.md)
  The metric by which the recommender computes item similarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelalgorithmtype)*