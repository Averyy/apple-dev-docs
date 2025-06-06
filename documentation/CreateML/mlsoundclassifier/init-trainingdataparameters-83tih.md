# init(trainingData:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates a sound classifier with a training dataset represented by a dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
init(trainingData: [String : [URL]], parameters: MLSoundClassifier.ModelParameters = ModelParameters()) throws
```

## Parameters

- `trainingData`: A dictionary that contains a collection of labeled audio files. Each of the dictionary’s keys   is a label, and each key’s value is an array of audio-file URLs.
- `parameters`: An   instance you use to configure the model   for the training session.

## See Also

- [init(trainingData: MLSoundClassifier.DataSource, parameters: MLSoundClassifier.ModelParameters) throws](mlsoundclassifier/init(trainingdata:parameters:)-bztx.md)
  Creates a sound classifier with a training dataset represented by a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/init(trainingdata:parameters:)-83tih)*