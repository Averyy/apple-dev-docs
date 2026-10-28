# init(featureExtractor:validationData:maxIterations:augmentationOptions:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates a new set of image classifier parameters with validation data represented by a dictionary.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
init(featureExtractor: MLImageClassifier.FeatureExtractorType = .scenePrint(revision: 1), validationData: [String : [URL]]?, maxIterations: Int = 25, augmentationOptions: MLImageClassifier.ImageAugmentationOptions = [])
```

**Other overloads**:

```swift
init(featureExtractor: MLImageClassifier.FeatureExtractorType = .scenePrint(revision: 1), validationData: MLImageClassifier.DataSource, maxIterations: Int = 25, augmentationOptions: MLImageClassifier.ImageAugmentationOptions = [])
```

## Parameters

- `featureExtractor`: A versioned feature extractor.
- `validationData`: Validation data represented by a dictionary.
- `maxIterations`: The maximum number of training iterations to use during training. The default is 25.
- `augmentationOptions`: The image augmentation options to use to increase the training data variety.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/init(featureextractor:validationdata:maxiterations:augmentationoptions:)-5we70)*