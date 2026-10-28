# MLClassifier.supportVector(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A classifier that predicts a binary target value by maximizing the separation between categories.

**Availability**:
- macOS 10.14+ - Deprecated in 14.0

## Declaration

```swift
case supportVector(MLSupportVectorClassifier)
```

## Discussion

Don’t create an [`MLClassifier`](../mlclassifier.md) using one of its enumeration cases. Use the classifier’s initializer instead.

## See Also

### Classifier cases
- [case decisionTree(MLDecisionTreeClassifier)](./decisiontree%28_%29.md)
  A classifier that predicts the target by creating rules to split the data.
- [case randomForest(MLRandomForestClassifier)](./randomforest%28_%29.md)
  A classifier based on a collection of decision trees trained on subsets of the data.
- [case boostedTree(MLBoostedTreeClassifier)](./boostedtree%28_%29.md)
  A classifier based on a collection of decision trees combined with gradient boosting.
- [case logisticRegression(MLLogisticRegressionClassifier)](./logisticregression%28_%29.md)
  A classifier that predicts a discrete target value as a function of data features.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/supportvector(_:))*