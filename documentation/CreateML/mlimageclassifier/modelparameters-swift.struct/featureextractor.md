# featureExtractor

**Framework**: Create ML  
**Kind**: property

The underlying base model the training session uses to extract image features as it trains an image classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
var featureExtractor: MLImageClassifier.FeatureExtractorType { get set }
```

#### Discussion

When you train an image classifier with Create ML, you don’t train a complete model that converts images to labels. Instead, Create ML leverages a , which is another model that identifies a set of general but distinguishing image characteristics. You can either use Create ML’s `scenePrint` feature extractor or provide your own custom feature extractor.

In either case, you train your model to map the feature extractor’s output to labels in a process known as . Your model effectively borrows the knowledge of the feature extractor to accelerate its own training process while requiring fewer training images.

## See Also

- [var algorithm: MLImageClassifier.ModelParameters.ModelAlgorithmType](mlimageclassifier/modelparameters-swift.struct/algorithm.md)
  Model algorithm to be used
- [var validation: MLImageClassifier.ModelParameters.ValidationData](mlimageclassifier/modelparameters-swift.struct/validation.md)
  The image classifier’s validation dataset.
- [var maxIterations: Int](mlimageclassifier/modelparameters-swift.struct/maxiterations.md)
  The maximum number of iterations the training session can use.
- [var augmentationOptions: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/modelparameters-swift.struct/augmentationoptions.md)
  The variations the training session uses to generate more variety in the training dataset.
- [var validationData: [String : [URL]]?](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.property.md)
  A set of images that the training process uses for validation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/featureextractor)*