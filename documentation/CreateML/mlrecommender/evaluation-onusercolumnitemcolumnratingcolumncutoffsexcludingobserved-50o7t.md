# evaluation(on:userColumn:itemColumn:ratingColumn:cutoffs:excludingObserved:)

**Framework**: Create ML  
**Kind**: method

Computes the metrics for the given testing data.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func evaluation(on testingData: MLDataTable, userColumn: String, itemColumn: String, ratingColumn: String? = nil, cutoffs: [Int] = [1, 2, 3, 4, 5], excludingObserved: Bool = true) -> MLRecommenderMetrics
```

## Parameters

- `testingData`: A MLDataTable containing testing data.
- `userColumn`: Name of the Int or String typed column in the testing data containing user identifiers.
- `itemColumn`: Name of the Int or String typed column in the testing data containing item identifiers.
- `ratingColumn`: Name of an Int or Double typed column optionally in the testing data containing scores or   ratings. The default is nil, which corresponds to no rating column.
- `cutoffs`: The “precision at cutoff k” for this user is:   while “recall at cutoff k” for   this user is:   where   is the number of elements in the intersection   of A and P𝑘 and |A| is the number of elements in A.
- `excludingObserved`: Specifies whether user-item interactions observed in the training data are excluded when   generating evaluation result. The default is true.

## See Also

- [func evaluation(on: DataFrame, userColumn: String, itemColumn: String, ratingColumn: String?, cutoffs: [Int], excludingObserved: Bool) -> MLRecommenderMetrics](mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:)-641uh.md)
  Computes the metrics for the given testing data.
- [struct MLRecommenderMetrics](mlrecommendermetrics.md)
  Metrics you use to evaluate a recommender’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:)-50o7t)*