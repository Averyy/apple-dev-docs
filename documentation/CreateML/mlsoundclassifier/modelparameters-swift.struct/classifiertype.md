# MLSoundClassifier.ModelParameters.ClassifierType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The classifier options for a sound classifier training algorithm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum ClassifierType
```

## Topics

### Designating an algorithm’s classifier
- [MLSoundClassifier.ModelParameters.ClassifierType.logisticRegressor](./classifiertype/logisticregressor.md)
  A statistical model that uses logistic regression to classify an input vector into a category.
- [MLSoundClassifier.ModelParameters.ClassifierType.multilayerPerceptron(layerSizes:)](./classifiertype/multilayerperceptron%28layersizes%29.md)
  A neural network model that uses three or more layers to classify an input into a category.
### Describing a classifier type
- [var description: String](./classifiertype/description.md)
  A text representation of the classifier type.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Hashable](../../../Swift/hashable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLSoundClassifier.ModelParameters.ValidationData](./validationdata.md)
  The source of a validation dataset for a sound classifier.
- [MLSoundClassifier.ModelParameters.ModelAlgorithmType](./modelalgorithmtype.md)
  The algorithm options to train a sound classifier.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType](./featureextractortype.md)
  The feature-extractor options for a sound-classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](./featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)*