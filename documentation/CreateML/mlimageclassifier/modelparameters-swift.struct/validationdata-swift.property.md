# validationData

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

A set of images that the training process uses for validation.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 10.15
- visionOS 1.0+

> **Deprecated**: Use the validation property instead.

## Declaration

```swift
var validationData: [String : [URL]]? { get set }
```

## See Also

### Accessing the training parameters
- [var algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType](./algorithm.md)
  Model algorithm to be used
- [var featureExtractor: MLImageClassifier.FeatureExtractorType](./featureextractor.md)
  The underlying base model the training session uses to extract image features as it trains an image classifier.
- [var validation: MLImageClassifier.ModelParameters.ValidationData](./validation.md)
  The image classifier’s validation dataset.
- [var maxIterations: Int](./maxiterations.md)
  The maximum number of iterations the training session can use.
- [var augmentationOptions: MLImageClassifier.ImageAugmentationOptions](./augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/validationdata-swift.property)*