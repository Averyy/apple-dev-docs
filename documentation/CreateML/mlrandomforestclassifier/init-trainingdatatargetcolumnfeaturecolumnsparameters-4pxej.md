# init(trainingData:targetColumn:featureColumns:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a Random Forest Classifier from the feature columns in the training data to predict the categories in the target column.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLRandomForestClassifier.ModelParameters = ModelParameters(validationData: nil)) throws
```

## Parameters

- `trainingData`: A data table of training examples.
- `targetColumn`: The column name for the values in the training data that the classifier should predict.
- `featureColumns`: The column names for the values in the training data that the classifier uses to predict   the target value.
- `parameters`: The model parameters.

## See Also

- [init(checkpoint: MLCheckpoint) throws](mlrandomforestclassifier/init(checkpoint:).md)
  Creates a random forest classifier classifier  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters) throws](mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-5nojh.md)
  Creates a random forest classifier.
- [MLRandomForestClassifier.ModelParameters](mlrandomforestclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLRandomForestClassifier.ModelParameters](mlrandomforestclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlrandomforestclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlrandomforestclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-4pxej)*