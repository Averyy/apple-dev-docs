# threshold

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The item confidence value cutoff, below which the recommender omits those items from its recommendations.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var threshold: Double
```

#### Discussion

The default value is `0.001`.

## See Also

### Configuring the parameters
- [var algorithm: MLRecommender.ModelAlgorithmType](./algorithm.md)
  The algorithm the recommender uses to make recommendations.
- [var maxCount: Int](./maxcount.md)
  The largest number of similar items the model stores for each item.
- [var maxSimilarityIterations: Int](./maxsimilarityiterations.md)
  The largest number of iterations the recommender uses to build its lookup table.
- [var nearestItems: MLDataTable?](./nearestitems.md)
  A data table that lists each item’s nearest items.
- [var nearestItemsDataFrame: DataFrame?](./nearestitemsdataframe.md)
  A data frame that lists each item’s nearest items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct/threshold)*