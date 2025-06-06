# modelParameters

**Framework**: Create ML  
**Kind**: property

The underlying parameters used when training the model.

**Availability**:
- macOS 10.14+

## Declaration

```swift
let modelParameters: MLSupportVectorClassifier.ModelParameters
```

## See Also

- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLSupportVectorClassifier.ModelParameters) throws](mlsupportvectorclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7t1yb.md)
  Creates a support vector classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLSupportVectorClassifier.ModelParameters) throws](mlsupportvectorclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-9ob53.md)
  Creates a Support Vector Classifier from the feature columns in the training data to predict the categories in the target column.
- [MLSupportVectorClassifier.ModelParameters](mlsupportvectorclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [var targetColumn: String](mlsupportvectorclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlsupportvectorclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/modelparameters-swift.property)*