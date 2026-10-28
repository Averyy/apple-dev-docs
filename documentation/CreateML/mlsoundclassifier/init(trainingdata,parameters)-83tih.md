# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a sound classifier with a training dataset represented by a dictionary.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 11.0
- visionOS 1.0+

> **Deprecated**: Use DataSource.filesByLabel to provide dictionary training data instead.

## Declaration

```swift
init(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters = ModelParameters()) throws
```

**Other overloads**:

```swift
init(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters = ModelParameters()) throws
```

## Parameters

- `trainingData`: A dictionary that contains a collection of labeled audio files. Each of the dictionary’s keys is a label, and each key’s value is an array of audio-file URLs.
- `parameters`: An [`MLSoundClassifier.ModelParameters`](./modelparameters-swift.struct.md) instance you use to configure the model for the training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:)-83tih)*