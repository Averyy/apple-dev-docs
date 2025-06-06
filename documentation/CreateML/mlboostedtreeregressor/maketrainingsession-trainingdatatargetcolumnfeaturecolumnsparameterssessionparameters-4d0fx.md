# makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates or restores a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLBoostedTreeRegressor.ModelParameters = ModelParameters(validation: .split(strategy: .automatic)), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>
```

#### Return Value

A `MLTrainingSession` that can be used to start or resume training.

## Parameters

- `trainingData`: A DataTable specifying training data.
- `targetColumn`: A String specifying the target column name in the trainingData
- `featureColumns`: An optional list of Strings specifying feature columns to be   used to predict the target, if not provided, default to use all the   other columns in the trainingData, except the one specified by targetColumn
- `parameters`: Model training parameters. See   for the defaults.
- `sessionParameters`: Training session parameters. See   for the defaults.

## See Also

- [init(checkpoint: MLCheckpoint) throws](mlboostedtreeregressor/init(checkpoint:).md)
  Creates a boosted tree regressor  from a checkpoint.
- [init(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters) throws](mlboostedtreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-6z8wm.md)
  Creates a boosted tree regressor.
- [static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>](mlboostedtreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1x5hc.md)
  Creates or restores a training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLBoostedTreeRegressor>](mlboostedtreeregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.
- [static func resume(MLTrainingSession<MLBoostedTreeRegressor>) throws -> MLJob<MLBoostedTreeRegressor>](mlboostedtreeregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeRegressor>](mlboostedtreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-1razs.md)
  Trains a boosted tree regressor.
- [static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLBoostedTreeRegressor>](mlboostedtreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4okyp.md)
  Trains a boosted tree regressor.
- [init(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]?, parameters: MLBoostedTreeRegressor.ModelParameters) throws](mlboostedtreeregressor/init(trainingdata:targetcolumn:featurecolumns:parameters:)-hfxs.md)
  Creates a Boosted Tree Regressor from the feature columns in the training data to predict the values in the target column.
- [MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.struct.md)
  Parameters that affect the process of training a model.
- [let modelParameters: MLBoostedTreeRegressor.ModelParameters](mlboostedtreeregressor/modelparameters-swift.property.md)
  The underlying parameters used when training the model.
- [var targetColumn: String](mlboostedtreeregressor/targetcolumn.md)
  The name of the column you selected at initialization to define which feature the regressor predicts.
- [var featureColumns: [String]](mlboostedtreeregressor/featurecolumns.md)
  The names of the columns you selected at initialization to train the regressor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlboostedtreeregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-4d0fx)*