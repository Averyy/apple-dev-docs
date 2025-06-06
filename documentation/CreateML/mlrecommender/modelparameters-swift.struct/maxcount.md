# maxCount

**Framework**: Create ML  
**Kind**: property

The largest number of similar items the model stores for each item.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var maxCount: Int
```

#### Discussion

The memory Create ML requires to train this model is proportional to this number. A lower value reduces its demand for memory but decreases the recommender’s accuracy. The default value is `64`.

## See Also

- [var algorithm: MLRecommender.ModelAlgorithmType](mlrecommender/modelparameters-swift.struct/algorithm.md)
  The algorithm the recommender uses to make recommendations.
- [var maxSimilarityIterations: Int](mlrecommender/modelparameters-swift.struct/maxsimilarityiterations.md)
  The largest number of iterations the recommender uses to build its lookup table.
- [var threshold: Double](mlrecommender/modelparameters-swift.struct/threshold.md)
  The item confidence value cutoff, below which the recommender omits those items from its recommendations.
- [var nearestItems: MLDataTable?](mlrecommender/modelparameters-swift.struct/nearestitems.md)
  A data table that lists each item’s nearest items.
- [var nearestItemsDataFrame: DataFrame?](mlrecommender/modelparameters-swift.struct/nearestitemsdataframe.md)
  A data frame that lists each item’s nearest items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct/maxcount)*