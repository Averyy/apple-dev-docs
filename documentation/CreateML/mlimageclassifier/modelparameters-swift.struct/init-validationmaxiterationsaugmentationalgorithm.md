# init(validation:maxIterations:augmentation:algorithm:)

**Framework**: Create ML  
**Kind**: init

Creates model training parameters.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
init(validation: MLImageClassifier.ModelParameters.ValidationData = __Defaults.validation, maxIterations: Int = __Defaults.maximumIterations, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType = __Defaults.algorithm)
```

## Parameters

- `validation`: Labeled data that the model evaluates on for validation. The default is   .
- `maxIterations`: The maximum number of training iterations to use during training. The default is 25.
- `augmentation`: The image augmentation options to use to increase the training data variety. If no data   augmentation needs to be applied, use   as input. Otherwise, inputs take the form  .
- `algorithm`: The type of model algorithm to use for training. The default is a logistic regression   classifier with a   feature extractor.

## See Also

- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validation:maxiterations:augmentationoptions:).md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor:validationData:maxIterations:augmentationOptions:)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:).md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [MLImageClassifier.ModelParameters.ClassifierType](mlimageclassifier/modelparameters-swift.struct/classifiertype.md)
  Type of classifier to be used.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/init(validation:maxiterations:augmentation:algorithm:))*