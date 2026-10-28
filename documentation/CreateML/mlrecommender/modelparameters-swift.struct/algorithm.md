# algorithm

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The algorithm the recommender uses to make recommendations.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var algorithm: MLRecommender.ModelAlgorithmType
```

## Discussion

The default is [`MLRecommender.ModelAlgorithmType.itemSimilarity(_:)`](../modelalgorithmtype/itemsimilarity%28_%29.md).

## See Also

### Configuring the parameters
- [var maxCount: Int](./maxcount.md)
  The largest number of similar items the model stores for each item.
- [var maxSimilarityIterations: Int](./maxsimilarityiterations.md)
  The largest number of iterations the recommender uses to build its lookup table.
- [var threshold: Double](./threshold.md)
  The item confidence value cutoff, below which the recommender omits those items from its recommendations.
- [var nearestItems: MLDataTable?](./nearestitems.md)
  A data table that lists each item’s nearest items.
- [var nearestItemsDataFrame: DataFrame?](./nearestitemsdataframe.md)
  A data frame that lists each item’s nearest items.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/modelparameters-swift.struct/algorithm)*