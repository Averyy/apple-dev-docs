# makeTrainingSession(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method

Creates or restores a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters = ModelParameters(
            validation: .split(strategy: .automatic),
            augmentation: [],
            algorithm: .transferLearning(
                featureExtractor: .scenePrint(revision: 1),
                classifier: .logisticRegressor
            )
        ), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLImageClassifier>
```

#### Return Value

A `MLTrainingSession` that can be used to start or resume training.

## Parameters

- `trainingData`: Data source for training.
- `parameters`: Model training parameters. See   for the defaults.
- `sessionParameters`: Training session parameters. See   for the defaults.

## See Also

- [static func train(trainingData: MLImageClassifier.DataSource, parameters: MLImageClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLImageClassifier>](mlimageclassifier/train(trainingdata:parameters:sessionparameters:).md)
  Begins an asynchronous image classifier training session with a training dataset represented by a data source.
- [static func resume(MLTrainingSession<MLImageClassifier>) throws -> MLJob<MLImageClassifier>](mlimageclassifier/resume(_:).md)
  Begins or continues an asynchronous image classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLImageClassifier>](mlimageclassifier/restoretrainingsession(sessionparameters:).md)
  Creates an asynchronous training session for an image classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))*