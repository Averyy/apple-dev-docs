# init(mlModel:)

**Framework**: Sound Analysis  
**Kind**: init

Creates a request that uses a custom sound classification model.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.1+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

## Declaration

```swift
init(mlModel: MLModel) throws
```

## Mentions

- [Classifying Sounds in an Audio File](classifying-sounds-in-an-audio-file.md)

#### Discussion

The model you provide must accept audio data as input and produce a classification dictionary output that contains the probability of each category. For example, you can generate a sound classifier model by creating an [`MLSoundClassifier`](https://developer.apple.com/documentation/CreateML/MLSoundClassifier) and training it with your own audio files.

## Parameters

- `mlModel`: A Core ML sound classification model.

## See Also

- [init(classifierIdentifier: SNClassifierIdentifier) throws](snclassifysoundrequest/init(classifieridentifier:).md)
  Creates a request that uses the framework’s built-in sound classification model.
- [struct SNClassifierIdentifier](snclassifieridentifier.md)
  An identifier that represents the versions of the framework’s sound classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/soundanalysis/snclassifysoundrequest/init(mlmodel:))*