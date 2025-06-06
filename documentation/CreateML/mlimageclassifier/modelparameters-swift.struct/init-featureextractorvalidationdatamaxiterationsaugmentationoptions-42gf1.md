# init(featureExtractor:validationData:maxIterations:augmentationOptions:)

**Framework**: Create ML  
**Kind**: init

Creates a new set of image classifier parameters with validation data represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
init(featureExtractor: MLImageClassifier.FeatureExtractorType = .scenePrint(revision: 1), validationData: MLImageClassifier.DataSource, maxIterations: Int = 25, augmentationOptions: MLImageClassifier.ImageAugmentationOptions = [])
```

## Parameters

- `featureExtractor`: A versioned feature extractor.
- `validationData`: The validation datasource.
- `maxIterations`: The maximum number of training iterations to use during training. The default is 25.
- `augmentationOptions`: The image augmentation options to use to increase the training data variety.

## See Also

- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](mlimageclassifier/modelparameters-swift.struct/init(validation:maxiterations:augmentation:algorithm:).md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validation:maxiterations:augmentationoptions:).md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validationData: [String : [URL]]?, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:)-5we70.md)
  Creates a new set of image classifier parameters with validation data represented by a dictionary.
- [MLImageClassifier.ModelParameters.ClassifierType](mlimageclassifier/modelparameters-swift.struct/classifiertype.md)
  Type of classifier to be used.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](mlimageclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:)-42gf1)*