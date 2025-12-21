# MLImageClassifier.ImageAugmentationOptions

**Framework**: Create ML  
**Kind**: struct

The variations that the training process can use to generate more training data from the training data you provide.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
struct ImageAugmentationOptions
```

#### Overview

Augmentation generates new images from the training data you supply to increase the amount of training data available to the model.

See [`Improving Your Model’s Accuracy`](improving-your-model-s-accuracy.md) for a discussion about when to use augmentation.

## Topics

### Selecting augmentation options
- [static let crop: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/crop.md)
  An option for augmenting training data by creating cropped versions of each image.
- [static let rotation: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/rotation.md)
  An option for augmenting training data by rotating each image.
- [static let blur: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/blur.md)
  An option for augmenting training data by blurring each image.
- [static let exposure: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/exposure.md)
  An option for augmenting training data by lightening or darkening each image.
- [static let noise: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/noise.md)
  An option for augmenting training data by adding random amounts of noise to each image.
- [static let flip: MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions/flip.md)
  An option for augmenting training data by flipping each image along the horizontal and vertical axes.
### Creating augmentation options
- [init(rawValue: Int)](mlimageclassifier/imageaugmentationoptions/init(rawvalue:).md)
  Creates an augmentation set with the given raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [MLImageClassifier.DataSource](mlimageclassifier/datasource.md)
  A data source for an image classifier.
- [MLImageClassifier.ModelParameters](mlimageclassifier/modelparameters-swift.struct.md)
  Parameters that affect the process of training an image classifier model.
- [MLImageClassifier.FeatureExtractorType](mlimageclassifier/featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
- [MLImageClassifier.CustomFeatureExtractor](mlimageclassifier/customfeatureextractor.md)
  A custom feature extractor a training session uses to train an image classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/imageaugmentationoptions)*