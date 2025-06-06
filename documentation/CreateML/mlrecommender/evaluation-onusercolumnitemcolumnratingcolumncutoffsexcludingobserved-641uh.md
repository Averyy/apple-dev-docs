# evaluation(on:userColumn:itemColumn:ratingColumn:cutoffs:excludingObserved:)

**Framework**: Create ML  
**Kind**: method

Computes the metrics for the given testing data.

**Availability**:
- macOS 13.0+

## Declaration

```swift
func evaluation(on testingData: DataFrame, userColumn: String, itemColumn: String, ratingColumn: String? = nil, cutoffs: [Int] = [1, 2, 3, 4, 5], excludingObserved: Bool = true) -> MLRecommenderMetrics
```

#### Discussion

Let P𝑘 be a vector of the first k items recommended by the model for a particular user and let A be the set of items in the provided testingData for the same user.

The “precision at cutoff k” for this user is: precision(k) = |A ∩ P𝑘| / k

while “recall at cutoff k” for this user is: recall(k) = |A ∩ P𝑘| / |A|

where |A ∩ P𝑘| is the number of elements in the intersection of A and P𝑘 and |A| is the number of elements in A.

## Parameters

- `testingData`: A MLDataTable containing testing data.
- `userColumn`: Name of the Int or String typed column in the testing data containing user identifiers.
- `itemColumn`: Name of the Int or String typed column in the testing data containing item identifiers.
- `ratingColumn`: Name of an Int or Double typed column optionally in the testing data containing   scores or ratings. The default is nil, which corresponds to no rating column.
- `cutoffs`: A list of Ints corresponding to each value at which the precision and recall will be evaluated.   The default is [1,2,3,4,5].
- `excludingObserved`: Specifies whether user-item interactions observed in the training data are excluded when   generating evaluation result. The default is true.

## See Also

- [func evaluation(on: MLDataTable, userColumn: String, itemColumn: String, ratingColumn: String?, cutoffs: [Int], excludingObserved: Bool) -> MLRecommenderMetrics](mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:)-50o7t.md)
  Computes the metrics for the given testing data.
- [struct MLRecommenderMetrics](mlrecommendermetrics.md)
  Metrics you use to evaluate a recommender’s performance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrecommender/evaluation(on:usercolumn:itemcolumn:ratingcolumn:cutoffs:excludingobserved:)-641uh)*