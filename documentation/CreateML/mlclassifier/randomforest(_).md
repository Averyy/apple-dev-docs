# MLClassifier.randomForest(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A classifier based on a collection of decision trees trained on subsets of the data.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case randomForest(MLRandomForestClassifier)
```

## Discussion

Don’t create an [`MLClassifier`](../mlclassifier.md) using one of its enumeration cases. Use the classifier’s initializer instead.

## See Also

### Classifier cases
- [case decisionTree(MLDecisionTreeClassifier)](./decisiontree%28_%29.md)
  A classifier that predicts the target by creating rules to split the data.
- [case boostedTree(MLBoostedTreeClassifier)](./boostedtree%28_%29.md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [case logisticRegression(MLLogisticRegressionClassifier)](./logisticregression%28_%29.md)
  A classifier that predicts a discrete target value as a function of data features.
- [case supportVector(MLSupportVectorClassifier)](./supportvector%28_%29.md)
  A classifier that predicts a binary target value by maximizing the separation between categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/randomforest(_:))*