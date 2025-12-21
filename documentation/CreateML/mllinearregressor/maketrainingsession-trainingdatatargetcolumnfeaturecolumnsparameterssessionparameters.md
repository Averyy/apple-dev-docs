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
static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLLinearRegressor.ModelParameters = .init(validation: .split(strategy: .automatic)), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLLinearRegressor>
```

#### Return Value

A `MLTrainingSession` that can be used to start or resume training.

## Parameters

- `trainingData`: A   specifying training data.
- `targetColumn`: A String specifying the target column name in the trainingData
- `featureColumns`: An optional list of Strings specifying feature columns to be   used to predict the target, if not provided, default to use all the   other columns in the trainingData, except the one specified by targetColumn
- `parameters`: Model training parameters. See   for the defaults.
- `sessionParameters`: Training session parameters. See   for the defaults.

## See Also

- [static train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mllinearregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Trains a linear regressor.
- [static func resume(MLTrainingSession<MLLinearRegressor>) throws -> MLJob<MLLinearRegressor>](mllinearregressor/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLLinearRegressor>](mllinearregressor/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mllinearregressor/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:))*