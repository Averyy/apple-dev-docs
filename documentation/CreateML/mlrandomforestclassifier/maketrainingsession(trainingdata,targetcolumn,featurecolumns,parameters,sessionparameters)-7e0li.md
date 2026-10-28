# makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates or restores a training session.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- tvOS 16.0+ - Deprecated in 17.0
- visionOS 1.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLRandomForestClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLRandomForestClassifier>
```

**Other overloads**:

```swift
static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLRandomForestClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLRandomForestClassifier>
```

## Return Value

A `MLTrainingSession` that can be used to start or resume training.

## Parameters

- `trainingData`: A DataTable specifying training data.
- `targetColumn`: A String specifying the target column name in the trainingData
- `featureColumns`: An optional list of Strings specifying feature columns to be used to predict the target, if not provided, default to use all the other columns in the trainingData, except the one specified by targetColumn
- `parameters`: Model training parameters. See [`MLRandomForestClassifier.ModelParameters`](./modelparameters-swift.struct.md) for the defaults.
- `sessionParameters`: Training session parameters. See [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) for the defaults.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:)-7e0li)*