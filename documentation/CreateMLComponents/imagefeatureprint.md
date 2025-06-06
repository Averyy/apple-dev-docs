# ImageFeaturePrint

**Framework**: Create ML Components  
**Kind**: struct

ImageFeaturePrint image feature extractor.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct ImageFeaturePrint
```

## Topics

### Creating the extractor
- [init(from: any Decoder) throws](imagefeatureprint/init(from:).md)
  Creates a new instance by decoding from the given decoder.
- [init(cropAndScale: VNImageCropAndScaleOption, context: CIContext)](imagefeatureprint/init(cropandscale:context:).md)
  Creates a FeaturePrint feature extractor.
- [init(revision: Int, cropAndScale: VNImageCropAndScaleOption, context: CIContext)](imagefeatureprint/init(revision:cropandscale:context:).md)
  Creates a FeaturePrint feature extractor.
### Getting the properties
- [let cropAndScale: VNImageCropAndScaleOption](imagefeatureprint/cropandscale.md)
  The crop and scale options.
- [var revision: Int](imagefeatureprint/revision.md)
  The feature extractor revision number.
- [static let latestRevision: Int](imagefeatureprint/latestrevision.md)
  The latest feature extractor revision.
### Performing the transformation
- [func applied(to: CIImage, eventHandler: EventHandler?) async throws -> MLShapedArray<Float>](imagefeatureprint/applied(to:eventhandler:).md)
  Extracts image features from an image.
### Type Aliases
- [ImageFeaturePrint.Input](imagefeatureprint/input.md)
  The input type.
- [ImageFeaturePrint.Output](imagefeatureprint/output.md)
  The output type.
### Default Implementations
- [CustomDebugStringConvertible Implementations](imagefeatureprint/customdebugstringconvertible-implementations.md)
- [Decodable Implementations](imagefeatureprint/decodable-implementations.md)
- [Encodable Implementations](imagefeatureprint/encodable-implementations.md)
- [Transformer Implementations](imagefeatureprint/transformer-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [Decodable](../Swift/Decodable.md)
- [Encodable](../Swift/Encodable.md)
- [ImageFeatureExtractor](imagefeatureextractor.md)
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

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/imagefeatureprint)*