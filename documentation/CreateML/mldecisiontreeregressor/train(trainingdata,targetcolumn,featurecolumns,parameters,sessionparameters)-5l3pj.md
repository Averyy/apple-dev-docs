# train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Trains a decision tree regressor.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 16.0+ - Deprecated in 17.0
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLDecisionTreeRegressor.ModelParameters = ModelParameters(validation: .split(strategy: .automatic)), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLDecisionTreeRegressor>
```

**Other overloads**:

```swift
static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLDecisionTreeRegressor.ModelParameters = .init(validation: .split(strategy: .automatic)), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLDecisionTreeRegressor>
```

## Return Value

A `MLJob` that can be used to observe training progress.

## Discussion

If `sessionDirectory` is provided it will save training progress. If there is progress already saved training will resume from the last checkpoint.

## Parameters

- `trainingData`: A DataTable specifying training data.
- `targetColumn`: A String specifying the target column name in the trainingData
- `featureColumns`: An optional list of Strings specifying feature columns to be used to predict the target, if not provided, default to use all the other columns in the trainingData, except the one specified by targetColumn
- `parameters`: Model training parameters. See [`MLDecisionTreeRegressor.ModelParameters`](./modelparameters-swift.struct.md) for the defaults.
- `sessionParameters`: Training session parameters. See [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) for the defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeregressor/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-5l3pj)*