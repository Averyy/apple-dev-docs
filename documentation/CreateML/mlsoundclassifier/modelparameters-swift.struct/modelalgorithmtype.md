# MLSoundClassifier.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

The algorithm options to train a sound classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Designating an algorithm
- [case transferLearning(featureExtractor: MLSoundClassifier.ModelParameters.FeatureExtractorType, classifier: MLSoundClassifier.ModelParameters.ClassifierType)](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:).md)
  An algorithm that leverages the knowledge of a general-purpose model built into the operating system.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType](mlsoundclassifier/modelparameters-swift.struct/featureextractortype.md)
  The feature-extractor options for a sound-classifier training algorithm.
- [MLSoundClassifier.ModelParameters.ClassifierType](mlsoundclassifier/modelparameters-swift.struct/classifiertype.md)
  The classifier options for a sound classifier training algorithm.
### Describing an algorithm
- [var description: String](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/description.md)
  A text representation of the training algorithm.
### Comparing algorithms
- [static func == (MLSoundClassifier.ModelParameters.ModelAlgorithmType, MLSoundClassifier.ModelParameters.ModelAlgorithmType) -> Bool](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Default Implementations
- [Equatable Implementations](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype/equatable-implementations.md)

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLSoundClassifier.ModelParameters.ValidationData](mlsoundclassifier/modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for a sound classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype)*