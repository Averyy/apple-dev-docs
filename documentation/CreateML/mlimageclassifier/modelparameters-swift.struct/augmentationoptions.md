# augmentationOptions

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

The variations the training session uses to generate more variety in the training dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var augmentationOptions: MLImageClassifier.ImageAugmentationOptions
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
- [var validationData: [String : [URL]]?](./validationdata-swift.property.md)
  A set of images that the training process uses for validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/augmentationoptions)*