# MLImageClassifier.CustomFeatureExtractor

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

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
- [init(modelPath: URL, outputName: String?)](./customfeatureextractor/init%28modelpath,outputname%29.md)
  Creates a custom feature extractor given a model file and an optional output layer name.
### Configuring a custom feature extractor
- [var modelPath: URL](./customfeatureextractor/modelpath.md)
  The location of a neural network `.mlmodel` file that takes an image as an input.
- [var outputName: String?](./customfeatureextractor/outputname.md)
  The name of the output from a feature extraction layer within the model.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLImageClassifier.DataSource](./datasource.md)
  A data source for an image classifier.
- [MLImageClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the process of training an image classifier model.
- [MLImageClassifier.FeatureExtractorType](./featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
- [MLImageClassifier.ImageAugmentationOptions](./imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/customfeatureextractor)*