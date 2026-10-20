# MLImageClassifier.ModelParameters.ModelAlgorithmType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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
- [case transferLearning(featureExtractor: MLImageClassifier.FeatureExtractorType, classifier: MLImageClassifier.ModelParameters.ClassifierType)](./modelalgorithmtype/transferlearning%28featureextractor,classifier%29.md)
  Train using a transfer-learning algorithm with a specified feature extractor and classifier.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Creating parameters
- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](./init%28validation,maxiterations,augmentation,algorithm%29.md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](./init%28featureextractor,validation,maxiterations,augmentationoptions%29.md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor:validationData:maxIterations:augmentationOptions:)](./init%28featureextractor,validationdata,maxiterations,augmentationoptions%29.md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [MLImageClassifier.ModelParameters.ClassifierType](./classifiertype.md)
  Type of classifier to be used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype)*