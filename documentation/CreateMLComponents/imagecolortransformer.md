# ImageColorTransformer

**Framework**: Create ML Components  
**Kind**: struct

An image color transformer.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageColorTransformer
```

## Topics

### Creating a color transformer
- [init(brightness: Float?, contrast: Float?, hue: Float?, saturation: Float?)](imagecolortransformer/init(brightness:contrast:hue:saturation:).md)
  Creates an image color transformer.
### Getting the properties
- [var brightness: Float?](imagecolortransformer/brightness.md)
  The brightness adjustment, between 0.0 and 1.0.
- [var contrast: Float?](imagecolortransformer/contrast.md)
  The contrast adjustment, between 0.0 and 1.0.
- [var hue: Float?](imagecolortransformer/hue.md)
  The hue adjustment, between 0.0 and 1.0.
- [var saturation: Float?](imagecolortransformer/saturation.md)
  The saturation adjustment, between 0.0 and 1.0.
### Applying the transformation
- [func applied(to: CIImage, eventHandler: EventHandler?) -> CIImage](imagecolortransformer/applied(to:eventhandler:).md)
  Performs the image color transformation operation on the input image.

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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagecolortransformer)*