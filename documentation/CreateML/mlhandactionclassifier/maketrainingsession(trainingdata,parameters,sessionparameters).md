# makeTrainingSession(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Creates an asynchronous hand action classifier’s training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
static func makeTrainingSession(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>
```

## Return Value

An [`MLTrainingSession`](../mltrainingsession.md) that represents the action classifier training session.

## Parameters

- `trainingData`: An [`MLHandActionClassifier.DataSource`](./datasource.md) instance.
- `parameters`: An [`MLHandActionClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

### Training a hand action classifier asynchronously
- [static func train(trainingData: MLHandActionClassifier.DataSource, parameters: MLHandActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLHandActionClassifier>](./train%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous hand action classifier’s training session.
- [static func resume(MLTrainingSession<MLHandActionClassifier>) throws -> MLJob<MLHandActionClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous hand action classifier’s training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLHandActionClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Recreates an asynchronous hand action classifier’s training session by restoring its saved state from the file system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/maketrainingsession(trainingdata:parameters:sessionparameters:))*