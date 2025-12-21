# init(trainingData:targetColumn:featureColumns:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a support vector classifier.

**Availability**:
- macOS 12.0+

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLSupportVectorClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the class labels
- `featureColumns`: Names of the columns containing feature values. If   all columns, other than the target   column, will be used as feature values.
- `parameters`: Model training parameters

## See Also

- [MLSupportVectorClassifier.ModelParameters](mlsupportvectorclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLSupportVectorClassifier.ModelParameters](mlsupportvectorclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlsupportvectorclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlsupportvectorclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:))*