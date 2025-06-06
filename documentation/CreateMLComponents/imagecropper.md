# ImageCropper

**Framework**: Create ML Components  
**Kind**: struct

An image crop transformer.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageCropper
```

## Topics

### Creating the transformer
- [init(cropRectangle: CGRect)](imagecropper/init(croprectangle:).md)
  Creates an image crop transformer. This transformer is used to crop an image to the `cropRectangle`.
### Getting the properties
- [var cropRectangle: CGRect](imagecropper/croprectangle.md)
  The crop rectangle within the image bounds.
### Performing the transformation
- [func applied(to: CIImage, eventHandler: EventHandler?) throws -> CIImage](imagecropper/applied(to:eventhandler:).md)
  Perform the image crop operation on the input pixelBuffer.
### Type Aliases
- [ImageCropper.Input](imagecropper/input.md)
  The input type.
- [ImageCropper.Output](imagecropper/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](imagecropper/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](imagecropper/decodable-implementations.md)
- [Encodable Implementations](imagecropper/encodable-implementations.md)
- [Transformer Implementations](imagecropper/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
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
- [struct ImageRotator](imagerotator.md)
  An image rotating transformer.
- [struct RandomImageNoiseGenerator](randomimagenoisegenerator.md)
  A transformer that adds random noise to an image.
- [struct MLModelImageFeatureExtractor](mlmodelimagefeatureextractor.md)
  An image feature extractor provided by an MLModel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagecropper)*