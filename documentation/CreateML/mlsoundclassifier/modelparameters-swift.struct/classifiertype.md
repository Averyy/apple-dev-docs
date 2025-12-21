# MLSoundClassifier.ModelParameters.ClassifierType

**Framework**: Create ML  
**Kind**: enum

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
- [MLSoundClassifier.ModelParameters.ClassifierType.logisticRegressor](mlsoundclassifier/modelparameters-swift.struct/classifiertype/logisticregressor.md)
  A statistical model that uses logistic regression to classify an input vector into a category.
- [MLSoundClassifier.ModelParameters.ClassifierType.multilayerPerceptron(layerSizes:)](mlsoundclassifier/modelparameters-swift.struct/classifiertype/multilayerperceptron(layersizes:).md)
  A neural network model that uses three or more layers to classify an input into a category.
### Describing a classifier type
- [var description: String](mlsoundclassifier/modelparameters-swift.struct/classifiertype/description.md)
  A text representation of the classifier type.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLSoundClassifier.ModelParameters.ValidationData](mlsoundclassifier/modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for a sound classifier.
- [MLSoundClassifier.ModelParameters.ModelAlgorithmType](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The algorithm options to train a sound classifier.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType](mlsoundclassifier/modelparameters-swift.struct/featureextractortype.md)
  The feature-extractor options for a sound-classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](mlsoundclassifier/modelparameters-swift.struct/featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/classifiertype)*