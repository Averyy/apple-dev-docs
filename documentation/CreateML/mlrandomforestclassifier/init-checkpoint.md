# init(checkpoint:)

**Framework**: Createml  
**Kind**: init

Creates a random forest classifier classifier  from a checkpoint.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
init(checkpoint: MLCheckpoint) throws
```

#### Discussion

> **Note**: `MLCreateError` if the checkpoint can’t be loaded.

## Parameters

- `checkpoint`: Training checkpoint.

## See Also

- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters) throws](mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-5nojh.md)
  Creates a random forest classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestClassifier.ModelParameters) throws](mlrandomforestclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-4pxej.md)
  Creates a Random Forest Classifier from the feature columns in the training data to predict the categories in the target column.
- [MLRandomForestClassifier.ModelParameters](mlrandomforestclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLRandomForestClassifier.ModelParameters](mlrandomforestclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlrandomforestclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mlrandomforestclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/init(checkpoint:))*