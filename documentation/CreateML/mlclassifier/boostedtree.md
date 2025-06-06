# MLClassifier.boostedTree(_:)

**Framework**: Create ML  
**Kind**: case

A classifier based on a collection of decision trees combined with gradient boosting.

**Availability**:
- macOS 10.14+

## Declaration

```swift
case boostedTree(MLBoostedTreeClassifier)
```

#### Discussion

Don’t create an [`MLClassifier`](mlclassifier.md) using one of its enumeration cases. Use the classifier’s initializer instead.

## See Also

- [case decisionTree(MLDecisionTreeClassifier)](mlclassifier/decisiontree(_:).md)
  A classifier that predicts the target by creating rules to split the data.
- [case randomForest(MLRandomForestClassifier)](mlclassifier/randomforest(_:).md)
  A classifier based on a collection of decision trees trained on subsets of the data.
- [case logisticRegression(MLLogisticRegressionClassifier)](mlclassifier/logisticregression(_:).md)
  A classifier that predicts a discrete target value as a function of data features.
- [case supportVector(MLSupportVectorClassifier)](mlclassifier/supportvector(_:).md)
  A classifier that predicts a binary target value by maximizing the separation between categories.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlclassifier/boostedtree(_:))*