# init(checkpoint:)

**Framework**: Create ML  
**Kind**: init

Creates a random forest regressor  from a checkpoint.

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

- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters) throws](mlrandomforestregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-7ep5e.md)
  Creates a random tree regressor.
- [static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](mlrandomforestregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-3e9dp.md)
  Creates or restores a training session.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](mlrandomforestregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-8ds4f.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](mlrandomforestregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLRandomForestRegressor>) throws -> MLJob<MLRandomForestRegressor>](mlrandomforestregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLRandomForestRegressor>](mlrandomforestregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4mev0.md)
  Trains a random forest regressor.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLRandomForestRegressor>](mlrandomforestregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7axdk.md)
  Trains a random forest regressor.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLRandomForestRegressor.ModelParameters) throws](mlrandomforestregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-9p7os.md)
  Creates a Random Forest Regressor from the feature columns in the training data to predict the values in the target column.
- [MLRandomForestRegressor.ModelParameters](mlrandomforestregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLRandomForestRegressor.ModelParameters](mlrandomforestregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlrandomforestregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlrandomforestregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/init(checkpoint:))*