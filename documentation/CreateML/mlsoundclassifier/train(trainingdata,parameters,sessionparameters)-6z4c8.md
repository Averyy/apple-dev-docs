# train(trainingData:parameters:sessionParameters:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Type Method

Begins an asynchronous sound classifier training session with a training dataset represented by a dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
static func train(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters = .init(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLSoundClassifier>
```

**Other overloads**:

```swift
static func train(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters = ModelParameters(), sessionParameters: MLTrainingSessionParameters = _defaultSessionParameters) throws -> MLJob<MLSoundClassifier>
```

## Return Value

An [`MLJob`](../mljob.md) that represents the sound classifier training session.

## Parameters

- `trainingData`: A collection of labeled audio files represented by a dictionary. The keys of this dictionary are the labels, and the values are the associated audio-file URLs.
- `parameters`: An [`MLSoundClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.
- `sessionParameters`: An [`MLTrainingSessionParameters`](../mltrainingsessionparameters.md) instance you use to configure the training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/train(trainingdata:parameters:sessionparameters:)-6z4c8)*