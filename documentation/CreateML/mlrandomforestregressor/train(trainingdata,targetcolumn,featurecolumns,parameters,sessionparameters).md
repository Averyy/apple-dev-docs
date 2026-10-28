# train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Trains a random forest regressor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLRandomForestRegressor.ModelParameters = .init(validation: .split(strategy: .automatic)), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLRandomForestRegressor>
```

**Other overloads**:

```swift
static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLRandomForestRegressor.ModelParameters = ModelParameters(validation: .split(strategy: .automatic)), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLRandomForestRegressor>
```

## Return Value

A `MLJob` that can be used to observe training progress.

## Discussion

If `sessionDirectory` is provided it will save training progress. If there is progress already saved training will resume from the last checkpoint.

## Parameters

- `trainingData`: A `DataFrame` specifying training data.
- `targetColumn`: A String specifying the target column name in the trainingData
- `featureColumns`: An optional list of Strings specifying feature columns to be used to predict the target, if not provided, default to use all the other columns in the trainingData, except the one specified by targetColumn
- `parameters`: Model training parameters. See [`MLRandomForestRegressor.ModelParameters`](./modelparameters-swift.struct.md) for the defaults.
- `sessionParameters`: Training session parameters. See [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) for the defaults.

## See Also

### Training a random forest regressor
- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](./maketrainingsession%28trainingdata,targetcolumn,featurecolumns,parameters,sessionparameters%29.md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLRandomForestRegressor>) throws -> MLJob<MLRandomForestRegressor>](./resume%28_%29.md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestRegressor>](./restoretrainingsession%28sessionparameters%29.md)
  Restores an existing training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:))*