# ImageExposureAdjuster

**Framework**: Create ML Components  
**Kind**: struct

An image exposure adjusting transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageExposureAdjuster
```

## Topics

### Creating an exposure adjuster
- [init(amount: Double)](imageexposureadjuster/init(amount:).md)
  Creates an image exposure adjusting transformer.
### Getting the amount
- [var amount: Double](imageexposureadjuster/amount.md)
  The amount to adjust the exposure of the image. The larger the value, the brighter the exposure.
### Performing the transformation
- [func applied(to: CIImage, eventHandler: EventHandler?) -> CIImage](imageexposureadjuster/applied(to:eventhandler:).md)
  Adjusts the exposure of the input image.
### Type Aliases
- [ImageExposureAdjuster.Input](imageexposureadjuster/input.md)
  The input type.
- [ImageExposureAdjuster.Output](imageexposureadjuster/output.md)
  The output type.
### Default Implementations
- [Transformer Implementations](imageexposureadjuster/transformer-implementations.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [Transformer](transformer.md)

## See Also

- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)
  Improve your model by using transformed versions of your training images.
- [Creating a multi-label image classifier](creating-a-multi-label-image-classifier.md)
  Train a machine learning model to assign multiple labels to an image.
- [struct ImageReader](imagereader.md)
  An image file reader.
- [protocol ImageFeatureExtractor](imagefeatureextractor.md)
  A transformer that takes an image and outputs image features.
- [struct ImageCropper](imagecropper.md)
  An image crop transformer.
- [struct ImageScaler](imagescaler.md)
  An image scaling transformer.
- [struct ImageFeaturePrint](imagefeatureprint.md)
  ImageFeaturePrint image feature extractor.
- [struct ImageBlur](imageblur.md)
  An image blurring transformer.
- [struct ImageColorTransformer](imagecolortransformer.md)
  An image color transformer.
- [struct ImageFlipper](imageflipper.md)
  An image flipper transformer.
- [struct ImageRotator](imagerotator.md)
  An image rotating transformer.
- [struct RandomImageNoiseGenerator](randomimagenoisegenerator.md)
  A transformer that adds random noise to an image.
- [struct MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
  An image feature extractor provided by an MLModel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imageexposureadjuster)*