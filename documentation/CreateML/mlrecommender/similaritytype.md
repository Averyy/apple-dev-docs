# MLRecommender.SimilarityType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The metric by which the recommender computes item similarity.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum SimilarityType
```

## Topics

### Similarity types
- [MLRecommender.SimilarityType.jaccard](./similaritytype/jaccard.md)
  The Jaccard similarity measure.
- [MLRecommender.SimilarityType.cosine](./similaritytype/cosine.md)
  The cosine similarity measure.
- [MLRecommender.SimilarityType.pearson](./similaritytype/pearson.md)
  The Pearson correlation similarity measure.
### Similarity type descriptions
- [var description: String](./similaritytype/description.md)
  A text representation of the similarity type.
- [var debugDescription: String](./similaritytype/debugdescription.md)
  A text representation of the similarity type that’s suitable for output during debugging.
- [var playgroundDescription: Any](./similaritytype/playgrounddescription.md)
  A description of the similarity type shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./similaritytype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./similaritytype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./similaritytype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Equatable](../../Swift/equatable.md)
- [Escapable](../../Swift/escapable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLRecommender.ModelAlgorithmType](./modelalgorithmtype.md)
  The algorithms a recommender can use to make recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/similaritytype)*