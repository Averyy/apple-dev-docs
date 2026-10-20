# init(algorithm:threshold:maxCount:nearestItemsDataFrame:maxSimilarityIterations:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new set of recommender configuration parameters.

**Availability**:
- macOS 14.0+

## Declaration

```swift
init(algorithm: MLRecommender.ModelAlgorithmType = .itemSimilarity(.cosine), threshold: Double = 0.001, maxCount: Int = 64, nearestItemsDataFrame: DataFrame?, maxSimilarityIterations: Int = 1024)
```

## See Also

### Creating parameters
- [init(algorithm: MLRecommender.ModelAlgorithmType, threshold: Double, maxCount: Int, nearestItems: MLDataTable?, maxSimilarityIterations: Int)](./init%28algorithm,threshold,maxcount,nearestitems,maxsimilarityiterations%29.md)
  Creates a new set of recommender configuration parameters.
- [MLRecommender.ModelAlgorithmType](../modelalgorithmtype.md)
  The algorithms a recommender can use to make recommendations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct/init(algorithm:threshold:maxcount:nearestitemsdataframe:maxsimilarityiterations:))*