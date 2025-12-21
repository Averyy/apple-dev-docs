# MLObjectDetector.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

An object-detector training algorithm.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Designating an algorithm
- [MLObjectDetector.ModelParameters.ModelAlgorithmType.darknetYolo](mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype/darknetyolo.md)
  An algorithm that trains a full neural network with your training data.
- [case transferLearning(MLObjectDetector.ModelParameters.FeatureExtractorType)](mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype/transferlearning(_:).md)
  An algorithm that leverages the knowledge of a general purpose model built into the operating system.
- [MLObjectDetector.ModelParameters.FeatureExtractorType](mlobjectdetector/modelparameters-swift.struct/featureextractortype.md)
  The underlying base model that extracts image features for an object-detector training session.
### Comparing algorithms
- [static func == (MLObjectDetector.ModelParameters.ModelAlgorithmType, MLObjectDetector.ModelParameters.ModelAlgorithmType) -> Bool](mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype/==(_:_:).md)
  Returns a Boolean value that indicates whether two algorithm are equal.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLObjectDetector.ModelParameters.ValidationData](mlobjectdetector/modelparameters-swift.struct/validationdata.md)
  A validation dataset for an object detector.
- [MLObjectDetector.ModelParameters.FeatureExtractorType](mlobjectdetector/modelparameters-swift.struct/featureextractortype.md)
  The underlying base model that extracts image features for an object-detector training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype)*