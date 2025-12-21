# MLModelImageFeatureExtractor

**Framework**: Create ML Components  
**Kind**: struct

An image feature extractor provided by an MLModel.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+

## Declaration

```swift
struct MLModelImageFeatureExtractor
```

## Topics

### Creating the extractor
- [init(model: MLModel, inputName: String, outputName: String, context: CIContext) throws](mlmodelimagefeatureextractor/init(model:inputname:outputname:context:).md)
  Creates an image feature extractor from a CoreML model.
- [init(contentsOf: URL, configuration: MLModelConfiguration, inputName: String, outputName: String, context: CIContext) async throws](mlmodelimagefeatureextractor/init(contentsof:configuration:inputname:outputname:context:).md)
  Creates an image feature extractor from a CoreML model URL.
### Getting the properties
- [let inputName: String](mlmodelimagefeatureextractor/inputname.md)
  The model’s input feature name.
- [let model: MLModel](mlmodelimagefeatureextractor/model.md)
  The CoreML model with .mlmodel extension.
- [let outputName: String](mlmodelimagefeatureextractor/outputname.md)
  The model’s output feature name.
### Applying
- [func applied(to: CIImage, eventHandler: EventHandler?) async throws -> MLShapedArray<Float>](mlmodelimagefeatureextractor/applied(to:eventhandler:).md)
  Uses the CoreML model to create image features from the input pixel buffer.
- [MLModelImageFeatureExtractor.Error](mlmodelimagefeatureextractor/error.md)
  CoreML Extraction error.

## Relationships

### Conforms To
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/mlmodelimagefeatureextractor)*