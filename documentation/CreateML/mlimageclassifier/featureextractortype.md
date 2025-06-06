# MLImageClassifier.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum

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
- [MLImageClassifier.FeatureExtractorType.scenePrint(revision:)](mlimageclassifier/featureextractortype/sceneprint(revision:).md)
  A feature extractor trained on millions of images.
- [case custom(MLImageClassifier.CustomFeatureExtractor)](mlimageclassifier/featureextractortype/custom(_:).md)
  A feature extractor that you provide as a Core ML model file or a layer within that file.
- [MLImageClassifier.CustomFeatureExtractor](mlimageclassifier/customfeatureextractor.md)
  A custom feature extractor a training session uses to train an image classifier.
### Describing a feature extractor type
- [var description: String](mlimageclassifier/featureextractortype/description.md)
  A text representation of the feature extractor.
- [var debugDescription: String](mlimageclassifier/featureextractortype/debugdescription.md)
  A text representation of the feature extractor that’s suitable for output during debugging.
- [var playgroundDescription: Any](mlimageclassifier/featureextractortype/playgrounddescription.md)
  A description of the feature extractor shown in a playground.
### Default Implementations
- [CustomDebugStringConvertible Implementations](mlimageclassifier/featureextractortype/customdebugstringconvertible-implementations.md)
- [CustomPlaygroundDisplayConvertible Implementations](mlimageclassifier/featureextractortype/customplaygrounddisplayconvertible-implementations.md)
- [CustomStringConvertible Implementations](mlimageclassifier/featureextractortype/customstringconvertible-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomPlaygroundDisplayConvertible](../Swift/CustomPlaygroundDisplayConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLImageClassifier.ModelParameters.ValidationData](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum.md)
  The source of a validation dataset for an image classifier.
- [MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/featureextractortype)*