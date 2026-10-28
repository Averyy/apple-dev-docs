# MLRegressor.decisionTree(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A regressor that estimates the target by learning rules to split the data.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case decisionTree(MLDecisionTreeRegressor)
```

## Discussion

Don’t create an [`MLRegressor`](../mlregressor.md) using one of its enumeration cases. Use the regressor’s initializer instead.

## See Also

### Regressor cases
- [case linear(MLLinearRegressor)](./linear%28_%29.md)
  A regressor that estimates the target as a linear function of the features.
- [case boostedTree(MLBoostedTreeRegressor)](./boostedtree%28_%29.md)
  A regressor based on a collection of decision trees combined with gradient boosting.
- [case randomForest(MLRandomForestRegressor)](./randomforest%28_%29.md)
  A regressor based on a collection of decision trees trained on subsets of the data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlregressor/decisiontree(_:))*