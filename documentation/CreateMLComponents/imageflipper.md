# ImageFlipper

**Framework**: Create ML Components  
**Kind**: struct

An image flipper transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageFlipper
```

## Topics

### Creating a transformer
- [init(orientation: ImageFlipper.Orientation)](imageflipper/init(orientation:).md)
  Creates an image flipper.
- [ImageFlipper.Orientation](imageflipper/orientation-swift.enum.md)
  The orientation to flip the image.
### Getting the orientation
- [var orientation: ImageFlipper.Orientation](imageflipper/orientation-swift.property.md)
  The orientation to flip the image.
### Performing the transformation
- [func applied(to: CIImage, eventHandler: EventHandler?) -> CIImage](imageflipper/applied(to:eventhandler:).md)
  Performs the image flipper operation on the input image.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
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
- [struct ImageExposureAdjuster](imageexposureadjuster.md)
  An image exposure adjusting transformer.
- [struct ImageRotator](imagerotator.md)
  An image rotating transformer.
- [struct RandomImageNoiseGenerator](randomimagenoisegenerator.md)
  A transformer that adds random noise to an image.
- [struct MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
  An image feature extractor provided by an MLModel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imageflipper)*