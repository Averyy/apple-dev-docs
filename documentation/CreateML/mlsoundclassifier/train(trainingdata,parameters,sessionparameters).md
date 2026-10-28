# train(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins an asynchronous sound classifier training session with a training dataset represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLSoundClassifier>
```

**Other overloads**:

```swift
static func train(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLSoundClassifier>
```

## Return Value

An [`MLJob`](../mljob.md) that represents the sound classifier training session.

## Parameters

- `trainingData`: A collection of labeled audio files represented by an [`MLSoundClassifier.DataSource`](./datasource.md).
- `parameters`: An [`MLSoundClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.

## See Also

### Training a sound classifier asynchronously
- [static func makeTrainingSession(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](./maketrainingsession%28trainingdata,parameters,sessionparameters%29.md)
  Creates an asynchronous training session for a sound classifier.
- [static func resume(MLTrainingSession<MLSoundClassifier>) throws -> MLJob<MLSoundClassifier>](./resume%28_%29.md)
  Begins or continues an asynchronous training session for a sound classifier.
- [static func restoreTrainingSession(sessionParameters: MLTrainingSessionParameters) throws -> MLTrainingSession<MLSoundClassifier>](./restoretrainingsession%28sessionparameters%29.md)
  Creates an asynchronous training session for a sound classifier by restoring an existing training session’s state from its parameters.
- [static func extractFeatures(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.FeatureExtractionParameters, sessionParameters: MLTrainingSessionParameters) throws -> MLJob<MLSoundClassifier.DataSource>](./extractfeatures%28trainingdata,parameters,sessionparameters%29.md)
  Begins an asynchronous session that extracts sound features from a data source of sound files.
- [MLSoundClassifier.FeatureExtractionParameters](./featureextractionparameters.md)
  Parameters that affect the process of extracting sound features from audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/train(trainingdata:parameters:sessionparameters:))*