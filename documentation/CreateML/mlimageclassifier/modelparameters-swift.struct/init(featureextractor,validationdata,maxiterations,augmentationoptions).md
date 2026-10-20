# init(featureExtractor:validationData:maxIterations:augmentationOptions:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new set of image classifier parameters with validation data represented by a data source.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
init(featureExtractor: MLImageClassifier.FeatureExtractorType = .scenePrint(revision: 1), validationData: MLImageClassifier.DataSource, maxIterations: Int = 25, augmentationOptions: MLImageClassifier.ImageAugmentationOptions = [])
```

**Other overloads**:

```swift
init(featureExtractor: MLImageClassifier.FeatureExtractorType = .scenePrint(revision: 1), validationData: [String : [URL]]?, maxIterations: Int = 25, augmentationOptions: MLImageClassifier.ImageAugmentationOptions = [])
```

## Parameters

- `featureExtractor`: A versioned feature extractor.
- `validationData`: The validation datasource.
- `maxIterations`: The maximum number of training iterations to use during training. The default is 25.
- `augmentationOptions`: The image augmentation options to use to increase the training data variety.

## See Also

### Creating parameters
- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](./init%28validation,maxiterations,augmentation,algorithm%29.md)
  Creates model training parameters.
- [init(featureExtractor: MLImageClassifier.FeatureExtractorType, validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentationOptions: MLImageClassifier.ImageAugmentationOptions)](./init%28featureextractor,validation,maxiterations,augmentationoptions%29.md)
  Creates a new set of training parameters for an image classifier with a validation dataset.
- [MLImageClassifier.ModelParameters.ClassifierType](./classifiertype.md)
  Type of classifier to be used.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](./modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:))*