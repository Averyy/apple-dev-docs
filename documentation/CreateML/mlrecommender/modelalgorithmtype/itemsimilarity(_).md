# MLRecommender.ModelAlgorithmType.itemSimilarity(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

An algorithm that compares the similarity from item to item.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case itemSimilarity(MLRecommender.SimilarityType)
```

#### Discussion

The default value is [`MLRecommender.SimilarityType.jaccard`](../similaritytype/jaccard.md).

## See Also

### Recommender algorithms
- [MLRecommender.SimilarityType](../similaritytype.md)
  The metric by which the recommender computes item similarity.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelalgorithmtype/itemsimilarity(_:))*