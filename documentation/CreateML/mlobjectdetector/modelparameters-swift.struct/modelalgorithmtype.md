# MLObjectDetector.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

An object-detector training algorithm.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum ModelAlgorithmType
```

## Topics

### Designating an algorithm
- [MLObjectDetector.ModelParameters.ModelAlgorithmType.darknetYolo](./modelalgorithmtype/darknetyolo.md)
  An algorithm that trains a full neural network with your training data.
- [case transferLearning(MLObjectDetector.ModelParameters.FeatureExtractorType)](./modelalgorithmtype/transferlearning%28_%29.md)
  An algorithm that leverages the knowledge of a general purpose model built into the operating system.
- [MLObjectDetector.ModelParameters.FeatureExtractorType](./featureextractortype.md)
  The underlying base model that extracts image features for an object-detector training session.
### Comparing algorithms
- [static func == (MLObjectDetector.ModelParameters.ModelAlgorithmType, MLObjectDetector.ModelParameters.ModelAlgorithmType) -> Bool](./modelalgorithmtype/eqeq%28_,_%29.md)
  Returns a Boolean value that indicates whether two algorithm are equal.

## Relationships

### Conforms To
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLObjectDetector.ModelParameters.ValidationData](./validationdata.md)
  A validation dataset for an object detector.
- [MLObjectDetector.ModelParameters.FeatureExtractorType](./featureextractortype.md)
  The underlying base model that extracts image features for an object-detector training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype)*