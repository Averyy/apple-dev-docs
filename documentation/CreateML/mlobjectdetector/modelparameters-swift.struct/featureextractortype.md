# MLObjectDetector.ModelParameters.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum

The underlying base model that extracts image features for an object-detector training session.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum FeatureExtractorType
```

## Topics

### Designating a feature extractor
- [MLObjectDetector.ModelParameters.FeatureExtractorType.objectPrint(revision:)](mlobjectdetector/modelparameters-swift.struct/featureextractortype/objectprint(revision:).md)
  A feature extractor you use with a transfer-learning algorithm for object detectors.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLObjectDetector.ModelParameters.ModelAlgorithmType.darknetYolo](mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype/darknetyolo.md)
  An algorithm that trains a full neural network with your training data.
- [case transferLearning(MLObjectDetector.ModelParameters.FeatureExtractorType)](mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype/transferlearning(_:).md)
  An algorithm that leverages the knowledge of a general purpose model built into the operating system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/featureextractortype)*