# MLSoundClassifier.ModelParameters.ModelAlgorithmType.transferLearning(featureExtractor:classifier:)

**Framework**: Create ML  
**Kind**: case

An algorithm that leverages the knowledge of a general-purpose model built into the operating system.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case transferLearning(featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, classifier: MLSoundClassifier.ModelParameters.ClassifierType)
```

#### Discussion

You typically use this transfer-learning algorithm to train an object detector in these situations:

- Your training dataset has a limited number of examples.
- You prefer your object detector’s Core ML model file to be as small as possible.

## Parameters

- `featureExtractor`: The extractor type the algorithm uses to detect features from the audio data.
- `classifier`: The model type the algorithm uses to classify audio data.

## See Also

- [MLSoundClassifier.ModelParameters.FeatureExtractorType](mlsoundclassifier/modelparameters-swift.struct/featureextractortype.md)
  The feature-extractor options for a sound-classifier training algorithm.
- [MLSoundClassifier.ModelParameters.ClassifierType](mlsoundclassifier/modelparameters-swift.struct/classifiertype.md)
  The classifier options for a sound classifier training algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:))*