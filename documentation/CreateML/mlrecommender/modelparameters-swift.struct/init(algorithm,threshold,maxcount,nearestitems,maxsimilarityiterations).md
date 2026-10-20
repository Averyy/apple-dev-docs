# init(algorithm:threshold:maxCount:nearestItems:maxSimilarityIterations:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new set of recommender configuration parameters.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
init(algorithm: MLRecommender.ModelAlgorithmType = .itemSimilarity(.cosine), threshold: Double = 0.001, maxCount: Int = 64, nearestItems: MLDataTable?, maxSimilarityIterations: Int = 1024)
```

## See Also

### Creating parameters
- [init(algorithm: MLRecommender.ModelAlgorithmType, threshold: Double, maxCount: Int, nearestItemsDataFrame: DataFrame?, maxSimilarityIterations: Int)](./init%28algorithm,threshold,maxcount,nearestitemsdataframe,maxsimilarityiterations%29.md)
  Creates a new set of recommender configuration parameters.
- [MLRecommender.ModelAlgorithmType](../modelalgorithmtype.md)
  The algorithms a recommender can use to make recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct/init(algorithm:threshold:maxcount:nearestitems:maxsimilarityiterations:))*