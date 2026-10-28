# train(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins an asynchronous action classifier training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
static func train(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLActionClassifier>
```

## Return Value

An [`MLJob`](../mljob.md) that represents the action classifier training session.

## Parameters

- `trainingData`: A collection of labeled videos represented by a data source.
- `parameters`: An [`MLActionClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

### Training an action classifier asynchronously
- [static func makeTrainingSession(trainingData: MLActionClassifier.DataSource, parameters: MLActionClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for an action classifier.
- [static func resume(MLTrainingSession<MLActionClassifier>) throws -> MLJob<MLActionClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous action classifier training session.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLActionClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for an action classifier by restoring an existing training session’s state from its parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/train(trainingdata:parameters:sessionparameters:))*