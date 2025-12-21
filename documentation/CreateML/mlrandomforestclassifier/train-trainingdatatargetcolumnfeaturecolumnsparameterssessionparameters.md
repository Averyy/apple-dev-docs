# train(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Trains a random forest classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: DataFrame, targetColumn: String, featureColumns: [String]? = nil, parameters: MLRandomForestClassifier.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLRandomForestClassifier>
```

#### Return Value

A `MLJob` that can be used to observe training progress.

#### Discussion

If `sessionDirectory` is provided it will save training progress. If there is progress already saved training will resume from the last checkpoint.

## Parameters

- `trainingData`: A   specifying training data.
- `targetColumn`: A String specifying the target column name in the trainingData
- `featureColumns`: An optional list of Strings specifying feature columns to be   used to predict the target, if not provided, default to use all the   other columns in the trainingData, except the one specified by targetColumn
- `parameters`: Model training parameters. See   for the defaults.
- `sessionParameters`: Training session parameters. See   for the defaults.

## See Also

- [static makeTrainingSession(trainingData:targetColumn:featureColumns:parameters:sessionParameters:)](mlrandomforestclassifier/maketrainingsession(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:).md)
  Creates or restores a training session.
- [static func resume(MLTrainingSession<MLRandomForestClassifier>) throws -> MLJob<MLRandomForestClassifier>](mlrandomforestclassifier/resume(_:).md)
  Resumes a training session from the last checkpoint if available.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLRandomForestClassifier>](mlrandomforestclassifier/restoretrainingsession(sessionparameters:).md)
  Restores an existing training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlrandomforestclassifier/train(trainingdata:targetcolumn:featurecolumns:parameters:sessionparameters:))*