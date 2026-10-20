# maxSimilarityIterations

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The largest number of iterations the recommender uses to build its lookup table.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var maxSimilarityIterations: Int
```

#### Discussion

This value limits the number of iterations the recommender can use to construct a lookup table. The default value is `1024`.

## See Also

### Configuring the parameters
- [var algorithm: MLRecommender.ModelAlgorithmType](./algorithm.md)
  The algorithm the recommender uses to make recommendations.
- [var maxCount: Int](./maxcount.md)
  The largest number of similar items the model stores for each item.
- [var threshold: Double](./threshold.md)
  The item confidence value cutoff, below which the recommender omits those items from its recommendations.
- [var nearestItems: MLDataTable?](./nearestitems.md)
  A data table that lists each item’s nearest items.
- [var nearestItemsDataFrame: DataFrame?](./nearestitemsdataframe.md)
  A data frame that lists each item’s nearest items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct/maxsimilarityiterations)*