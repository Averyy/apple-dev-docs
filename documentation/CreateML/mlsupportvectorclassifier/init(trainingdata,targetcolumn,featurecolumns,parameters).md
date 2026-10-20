# init(trainingData:targetColumn:featureColumns:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a support vector classifier.

**Availability**:
- macOS 12.0+ - Deprecated in 14.0

## Declaration

```swift
init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLSupportVectorClassifier.ModelParameters = ModelParameters(validation: .split(strategy: .automatic))) throws
```

**Other overloads**:

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLSupportVectorClassifier.ModelParameters = ModelParameters(validationData: nil)) throws
```

## Parameters

- `trainingData`: The training data
- `targetColumn`: Name of the column containing the class labels
- `featureColumns`: Names of the columns containing feature values. If `nil` all columns, other than the target column, will be used as feature values.
- `parameters`: Model training parameters

## See Also

### Creating and training a support vector classifier
- [MLSupportVectorClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLSupportVectorClassifier.ModelParameters](./modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](./targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](./featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsupportvectorclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:))*