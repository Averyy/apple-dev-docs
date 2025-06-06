# MLImageClassifier.FeatureExtractorType.custom(_:)

**Framework**: Create ML  
**Kind**: case

A feature extractor that you provide as a Core ML model file or a layer within that file.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case custom(MLImageClassifier.CustomFeatureExtractor)
```

#### Discussion

A custom feature extractor is a neural network model you provide to an [`MLImageClassifier`](mlimageclassifier.md). The feature extractor can be a layer within the model or the model itself. In either case, the neural network must take an image as input and output an [`MLMultiArray`](https://developer.apple.com/documentation/CoreML/MLMultiArray).

## Parameters

- `_`: Custom feature extractor to be used for extracting features.

## See Also

- [MLImageClassifier.FeatureExtractorType.scenePrint(revision:)](mlimageclassifier/featureextractortype/sceneprint(revision:).md)
  A feature extractor trained on millions of images.
- [MLImageClassifier.CustomFeatureExtractor](mlimageclassifier/customfeatureextractor.md)
  A custom feature extractor a training session uses to train an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/featureextractortype/custom(_:))*