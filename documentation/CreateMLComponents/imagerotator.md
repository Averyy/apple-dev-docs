# ImageRotator

**Framework**: Create ML Components  
**Kind**: struct

An image rotating transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageRotator
```

## Mentions

- [Augmenting images to expand your training data](augmenting-images-to-expand-your-training-data.md)

## Topics

### Creating the transformer
- [init(angle: Double)](imagerotator/init(angle:).md)
  Creates a transformer that rotates an image by a specified angle.
### Getting the angle
- [var angle: Double](imagerotator/angle.md)
  The angle, in radians, by which to rotate the coordinate space of the specified context. Positive values rotate counterclockwise and negative values rotate clockwise.
### Performing the transformation
- [func applied(to: CIImage, eventHandler: EventHandler?) -> CIImage](imagerotator/applied(to:eventhandler:).md)
  Rotates the image and then scales and crops the rotated image to fit the extent of the input image.
### Type Aliases
- [ImageRotator.Input](imagerotator/input.md)
  The input type.
- [ImageRotator.Output](imagerotator/output.md)
  The output type.
### Default Implementations
- [Transformer Implementations](imagerotator/transformer-implementations.md)

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
- [struct ImageFlipper](imageflipper.md)
  An image flipper transformer.
- [struct RandomImageNoiseGenerator](randomimagenoisegenerator.md)
  A transformer that adds random noise to an image.
- [struct MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
  An image feature extractor provided by an MLModel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagerotator)*