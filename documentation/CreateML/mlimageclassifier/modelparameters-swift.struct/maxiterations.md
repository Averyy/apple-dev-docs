# maxIterations

**Framework**: Create ML  
**Kind**: property

The maximum number of iterations the training session can use.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var maxIterations: Int
```

## See Also

- [var algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType](mlimageclassifier/modelparameters-swift.struct/algorithm.md)
  Model algorithm to be used
- [var featureExtractor: MLImageClassifier.FeatureExtractorType](mlimageclassifier/modelparameters-swift.struct/featureextractor.md)
  The underlying base model the training session uses to extract image features as it trains an image classifier.
- [var validation: MLImageClassifier.ModelParameters.ValidationData](mlimageclassifier/modelparameters-swift.struct/validation.md)
  The image classifier’s validation dataset.
- [var augmentationOptions: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.
- [var validationData: [String : [URL]]?](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  A set of images that the training process uses for validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/maxiterations)*