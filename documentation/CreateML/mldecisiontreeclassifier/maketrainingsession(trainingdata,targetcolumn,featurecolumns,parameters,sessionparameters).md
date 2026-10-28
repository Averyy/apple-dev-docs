# makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

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
static func makeTrainingSession(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLDecisionTreeClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>
```

**Other overloads**:

```swift
static func makeTrainingSession(trainingData: MLDataTable, targetColumn: String, featureColumns: [String]? = nil, parameters: MLDecisionTreeClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>
```

## Return Value

A `MLTrainingSession` that can be used to start or resume training.

## Parameters

- `trainingData`: A `DataFrame` specifying training data.
- `targetColumn`: A String specifying the target column name in the trainingData
- `featureColumns`: An optional list of Strings specifying feature columns to be used to predict the target, if not provided, default to use all the other columns in the trainingData, except the one specified by targetColumn
- `parameters`: Model training parameters. See [`MLDecisionTreeClassifier.ModelParameters`](./modelparameters-swift.struct.md) for the defaults.
- `sessionParameters`: Training session parameters. See [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) for the defaults.

## See Also

### Training a decision tree classifier asynchronously
- [init(trainingData:targetColumn:featureColumns:parameters:)](./init%28trainingdata,targetcolumn,featurecolumns,parameters%29.md)
  Creates a decision tree classifier.
- [static func resume(MLTrainingSession<MLDecisionTreeClassifier>) throws -> MLJob<MLDecisionTreeClassifier>](./resume%28_%29.md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLDecisionTreeClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Restores an existing training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mldecisiontreeclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:))*