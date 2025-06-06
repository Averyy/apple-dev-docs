# MLRecommender.SimilarityType

**Framework**: Create ML  
**Kind**: enum

The metric by which the recommender computes item similarity.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum SimilarityType
```

## Topics

### Similarity types
- [MLRecommender.SimilarityType.jaccard](mlrecommender/similaritytype/jaccard.md)
  The Jaccard similarity measure.
- [MLRecommender.SimilarityType.cosine](mlrecommender/similaritytype/cosine.md)
  The cosine similarity measure.
- [MLRecommender.SimilarityType.pearson](mlrecommender/similaritytype/pearson.md)
  The Pearson correlation similarity measure.
### Comparing similarity types
- [static func == (MLRecommender.SimilarityType, MLRecommender.SimilarityType) -> Bool](mlrecommender/similaritytype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlrecommender/similaritytype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Getting the hash value
- [func hash(into: inout Hasher)](mlrecommender/similaritytype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](mlrecommender/similaritytype/hashvalue.md)
  The hash value.
### Similarity type descriptions
- [var description: String](mlrecommender/similaritytype/description.md)
  A text representation of the similarity type.
- [var debugDescription: String](mlrecommender/similaritytype/debugdescription.md)
  A text representation of the similarity type that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlrecommender/similaritytype/playgrounddescription.md)
  A description of the similarity type shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlrecommender/similaritytype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlrecommender/similaritytype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlrecommender/similaritytype/customstringconvertible-implementations.md)
- [Equatable Implementations](mlrecommender/similaritytype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLRecommender.ModelAlgorithmType.itemSimilarity(_:)](mlrecommender/modelalgorithmtype/itemsimilarity(_:).md)
  An algorithm that compares the similarity from item to item.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/similaritytype)*