# MLImageClassifier.CustomFeatureExtractor

**Framework**: Create ML  
**Kind**: struct

A custom feature extractor a training session uses to train an image classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
struct CustomFeatureExtractor
```

## Topics

### Creating a custom feature extractor
- [init(modelPath: URL, outputName: String?)](mlimageclassifier/customfeatureextractor/init(modelpath:outputname:).md)
  Creates a custom feature extractor given a model file and an optional output layer name.
### Configuring a custom feature extractor
- [var modelPath: URL](mlimageclassifier/customfeatureextractor/modelpath.md)
  The location of a neural network `.mlmodel` file that takes an image as an input.
- [var outputName: String?](mlimageclassifier/customfeatureextractor/outputname.md)
  The name of the output from a feature extraction layer within the model.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [MLImageClassifier.FeatureExtractorType.scenePrint(revision:)](mlimageclassifier/featureextractortype/sceneprint(revision:).md)
  A feature extractor trained on millions of images.
- [case custom(MLImageClassifier.CustomFeatureExtractor)](mlimageclassifier/featureextractortype/custom(_:).md)
  A feature extractor that you provide as a Core ML model file or a layer within that file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/customfeatureextractor)*