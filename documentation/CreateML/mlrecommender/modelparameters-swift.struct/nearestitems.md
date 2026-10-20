# nearestItems

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A data table that lists each item’s nearest items.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

> **Deprecated**: Use nearestItemsDataFrame.

## Declaration

```swift
var nearestItems: MLDataTable?
```

## See Also

### Configuring the parameters
- [var algorithm: MLRecommender.ModelAlgorithmType](./algorithm.md)
  The algorithm the recommender uses to make recommendations.
- [var maxCount: Int](./maxcount.md)
  The largest number of similar items the model stores for each item.
- [var maxSimilarityIterations: Int](./maxsimilarityiterations.md)
  The largest number of iterations the recommender uses to build its lookup table.
- [var threshold: Double](./threshold.md)
  The item confidence value cutoff, below which the recommender omits those items from its recommendations.
- [var nearestItemsDataFrame: DataFrame?](./nearestitemsdataframe.md)
  A data frame that lists each item’s nearest items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct/nearestitems)*