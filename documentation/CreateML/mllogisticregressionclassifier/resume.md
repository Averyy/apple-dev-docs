# resume(_:)

**Framework**: Create ML  
**Kind**: method

Resumes a training session from the last checkpoint if available.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func resume(_ session: MLTrainingSession<MLLogisticRegressionClassifier>) throws -> MLJob<MLLogisticRegressionClassifier>
```

#### Return Value

A `MLJob` that can be used to observe training progress.

#### Discussion

If there are no resumable checkpoints training starts over from the beginning.

## Parameters

- `session`: Loaded or new training session.

## See Also

- [init(checkpoint: MLCheckpoint) throws](mllogisticregressionclassifier/init(checkpoint:).md)
  Creates a logistic regression classifier from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters) throws](mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-3ilkk.md)
  Creates a logistic regression classifier.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters) throws](mllogisticregressionclassifier/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7xy2g.md)
  Creates a Logistic Regression Classifier from the feature columns in the training data to predict the categories in the target column.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1jn01.md)
  Trains a logistic regression classifier.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-8vpa1.md)
  Trains a logistic regression classifier.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4anyg.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLLogisticRegressionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7l7f0.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLogisticRegressionClassifier>](mllogisticregressionclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [MLLogisticRegressionClassifier.ModelParameters](mllogisticregressionclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLLogisticRegressionClassifier.ModelParameters](mllogisticregressionclassifier/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mllogisticregressionclassifier/targetcolumn.md)
  The name of the column you selected at initialization to define which categories the classifier predicts.
- [var featureColumns: [String]](mllogisticregressionclassifier/featurecolumns.md)
  The names of the columns you selected at initialization to train the classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllogisticregressionclassifier/resume(_:))*