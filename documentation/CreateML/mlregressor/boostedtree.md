# MLRegressor.boostedTree(_:)

**Framework**: Create ML  
**Kind**: case

A regressor based on a collection of decision trees combined with gradient boosting.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case boostedTree(MLBoostedTreeRegressor)
```

#### Discussion

Don’t create an [`MLRegressor`](mlregressor.md) using one of its enumeration cases. Use the regressor’s initializer instead.

## See Also

- [case linear(MLLinearRegressor)](mlregressor/linear(_:).md)
  A regressor that estimates the target as a linear function of the features.
- [case decisionTree(MLDecisionTreeRegressor)](mlregressor/decisiontree(_:).md)
  A regressor that estimates the target by learning rules to split the data.
- [case randomForest(MLRandomForestRegressor)](mlregressor/randomforest(_:).md)
  A regressor based on a collection of decision trees trained on subsets of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/boostedtree(_:))*