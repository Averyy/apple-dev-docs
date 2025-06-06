# MLRegressor.linear(_:)

**Framework**: Create ML  
**Kind**: case

A regressor that estimates the target as a linear function of the features.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case linear(MLLinearRegressor)
```

#### Discussion

Don’t create an [`MLRegressor`](mlregressor.md) using one of its enumeration cases. Use the regressor’s initializer instead.

## See Also

- [case decisionTree(MLDecisionTreeRegressor)](mlregressor/decisiontree(_:).md)
  A regressor that estimates the target by learning rules to split the data.
- [case boostedTree(MLBoostedTreeRegressor)](mlregressor/boostedtree(_:).md)
  A regressor based on a collection of decision trees combined with gradient boosting.
- [case randomForest(MLRandomForestRegressor)](mlregressor/randomforest(_:).md)
  A regressor based on a collection of decision trees trained on subsets of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/linear(_:))*