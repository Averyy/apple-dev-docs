# MLObjectDetector.ModelParameters.ModelAlgorithmType.transferLearning(_:)

**Framework**: Create ML  
**Kind**: case

An algorithm that leverages the knowledge of a general purpose model built into the operating system.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case transferLearning(MLObjectDetector.ModelParameters.FeatureExtractorType)
```

#### Discussion

You typically use this transfer-learning algorithm to train an object detector in these situations:

- Your training dataset has a limited number of examples.
- You prefer your object detector’s Core ML model file to be as small as possible.

## See Also

- [MLObjectDetector.ModelParameters.ModelAlgorithmType.darknetYolo](mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype/darknetyolo.md)
  An algorithm that trains a full neural network with your training data.
- [MLObjectDetector.ModelParameters.FeatureExtractorType](mlobjectdetector/modelparameters-swift.struct/featureextractortype.md)
  The underlying base model that extracts image features for an object-detector training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/modelalgorithmtype/transferlearning(_:))*