# ImageScaler

**Framework**: Create ML Components  
**Kind**: struct

An image scaling transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageScaler
```

## Topics

### Creating a transformer
- [init(targetSize: CGSize)](imagescaler/init(targetsize:).md)
  Creates an image scaler transformer. This transformer is used to scale an image to the `targetSize`.
- [init(targetHeight: Double)](imagescaler/init(targetheight:).md)
  Creates an image scaler transformer that preserves the aspect ratio.
- [init(targetWidth: Double)](imagescaler/init(targetwidth:).md)
  Creates an image scaler transformer that preserves the aspect ratio.
### Getting the target image size
- [var targetSize: CGSize](imagescaler/targetsize.md)
  The target image size.
### Performing the transformation
- [func applied(to: CIImage, eventHandler: EventHandler?) throws -> CIImage](imagescaler/applied(to:eventhandler:).md)
  Perform the image scaler operation on the input pixelBuffer.

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
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
- [struct ImageRotator](imagerotator.md)
  An image rotating transformer.
- [struct RandomImageNoiseGenerator](randomimagenoisegenerator.md)
  A transformer that adds random noise to an image.
- [struct MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
  An image feature extractor provided by an MLModel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagescaler)*