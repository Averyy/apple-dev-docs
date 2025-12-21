# MLRecommender.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

The algorithms a recommender can use to make recommendations.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Recommender algorithms
- [MLRecommender.ModelAlgorithmType.itemSimilarity(_:)](mlrecommender/modelalgorithmtype/itemsimilarity(_:).md)
  An algorithm that compares the similarity from item to item.
- [MLRecommender.SimilarityType](mlrecommender/similaritytype.md)
  The metric by which the recommender computes item similarity.
### Algorithm descriptions
- [var description: String](mlrecommender/modelalgorithmtype/description.md)
  A text representation of the recommender algorithm.
- [var debugDescription: String](mlrecommender/modelalgorithmtype/debugdescription.md)
  A text representation of the recommender algorithm that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlrecommender/modelalgorithmtype/playgrounddescription.md)
  A description of the recommender algorithm shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlrecommender/modelalgorithmtype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlrecommender/modelalgorithmtype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlrecommender/modelalgorithmtype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLRecommender.SimilarityType](mlrecommender/similaritytype.md)
  The metric by which the recommender computes item similarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelalgorithmtype)*