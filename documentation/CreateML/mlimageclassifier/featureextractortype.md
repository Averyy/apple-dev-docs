# MLImageClassifier.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

The underlying base model that extracts image features for image classifier training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
enum FeatureExtractorType
```

#### Overview

Create ML has one built-in feature extractor: `scenePrint`. Alternatively, you can provide your own custom feature extractor from an `.mlmodel` file or a specific layer within a model file.

## Topics

### Selecting a feature extractor type
- [MLImageClassifier.FeatureExtractorType.scenePrint(revision:)](./featureextractortype/sceneprint%28revision%29.md)
  A feature extractor trained on millions of images.
- [case custom(MLImageClassifier.CustomFeatureExtractor)](./featureextractortype/custom%28_%29.md)
  A feature extractor that you provide as a Core ML model file or a layer within that file.
- [MLImageClassifier.CustomFeatureExtractor](./customfeatureextractor.md)
  A custom feature extractor a training session uses to train an image classifier.
### Describing a feature extractor type
- [var description: String](./featureextractortype/description.md)
  A text representation of the feature extractor.
- [var debugDescription: String](./featureextractortype/debugdescription.md)
  A text representation of the feature extractor that’s suitable for output during debugging.
- [var playgroundDescription: Any](./featureextractortype/playgrounddescription.md)
  A description of the feature extractor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](./featureextractortype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](./featureextractortype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](./featureextractortype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../../Swift/copyable.md)
- [CustomDebugStringConvertible](../../Swift/customdebugstringconvertible.md)
- [CustomPlaygroundDisplayConvertible](../../Swift/customplaygrounddisplayconvertible.md)
- [CustomStringConvertible](../../Swift/customstringconvertible.md)
- [Escapable](../../Swift/escapable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLImageClassifier.DataSource](./datasource.md)
  A data source for an image classifier.
- [MLImageClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training an image classifier model.
- [MLImageClassifier.CustomFeatureExtractor](./customfeatureextractor.md)
  A custom feature extractor a training session uses to train an image classifier.
- [MLImageClassifier.ImageAugmentationOptions](./imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/featureextractortype)*