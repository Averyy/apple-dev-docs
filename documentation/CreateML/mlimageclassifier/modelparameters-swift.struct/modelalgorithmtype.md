# MLImageClassifier.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum

The model algorithm to use for training an image classifier.

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

### Designating an algorithm type
- [case transferLearning(featureExtractor: MLImageClassifier.FeatureExtractorType, classifier: MLImageClassifier.ModelParameters.ClassifierType)](mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype/transferlearning(featureextractor:classifier:).md)
  Train using a transfer-learning algorithm with a specified feature extractor and classifier.
### Describing an algorithm type
- [var description: String](mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype/description.md)
  A textual representation of this instance.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](mlimageclassifier/modelparameters-swift.struct/init(validation:maxiterations:augmentation:algorithm:).md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validation:maxiterations:augmentationoptions:).md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validationData: MLImageClassifier.DataSource, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:)-42gf1.md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validationData: [String : [URL]]?, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:)-5we70.md)
  Creates a new set of image classifier parameters with validation data represented by a dictionary.
- [MLImageClassifier.ModelParameters.ClassifierType](mlimageclassifier/modelparameters-swift.struct/classifiertype.md)
  Type of classifier to be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype)*