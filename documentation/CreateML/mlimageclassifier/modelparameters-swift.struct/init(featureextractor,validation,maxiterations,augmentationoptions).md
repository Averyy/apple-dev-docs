# init(featureExtractor:validation:maxIterations:augmentationOptions:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new set of training parameters for an image classifier with a validation dataset.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 11.0
- visionOS 1.0+

> **Deprecated**: Use featureExtractor in ModelAlgorithm Type instead.

## Declaration

```swift
init(featureExtractor: MLImageClassifier.FeatureExtractorType = .scenePrint(revision: 1), validation: MLImageClassifier.ModelParameters.ValidationData = .split(strategy: .automatic), maxIterations: Int = 25, augmentationOptions: MLImageClassifier.ImageAugmentationOptions = [])
```

## Parameters

- `featureExtractor`: The feature extractor you want Create ML to use during the training session.
- `validation`: A validation dataset.
- `maxIterations`: The maximum number of training iterations to use during training. The default is 25.
- `augmentationOptions`: The image augmentation options to use to increase the training data variety.

## See Also

### Creating parameters
- [init(validation: MLImageClassifier.ModelParameters.ValidationData, maxIterations: Int, augmentation: MLImageClassifier.ImageAugmentationOptions, algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType)](./init%28validation,maxiterations,augmentation,algorithm%29.md)
  Creates model training parameters.
- [init(featureExtractor:validationData:maxIterations:augmentationOptions:)](./init%28featureextractor,validationdata,maxiterations,augmentationoptions%29.md)
  Creates a new set of image classifier parameters with validation data represented by a data source.
- [MLImageClassifier.ModelParameters.ClassifierType](./classifiertype.md)
  Type of classifier to be used.
- [MLImageClassifier.ModelParameters.ModelAlgorithmType](./modelalgorithmtype.md)
  The model algorithm to use for training an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validation:maxiterations:augmentationoptions:))*