# MLImageClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

The source of a validation dataset for an image classifier.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
enum ValidationData
```

## Topics

### Designating validation data
- [MLImageClassifier.ModelParameters.ValidationData.split(strategy:)](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/split(strategy:).md)
  A validation dataset derived by randomly selecting a portion of the image classifier’s training dataset using the split strategy.
- [MLImageClassifier.ModelParameters.ValidationData.dataSource(_:)](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLImageClassifier.ModelParameters.ValidationData.dictionary(_:)](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/dictionary(_:).md)
  A validation dataset represented by a dictionary.
- [MLImageClassifier.ModelParameters.ValidationData.none](mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/none.md)
  An empty validation dataset that skips the model validation phase after training.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLImageClassifier.FeatureExtractorType](mlimageclassifier/featureextractortype.md)
  The underlying base model that extracts image features for image classifier training session.
- [MLImageClassifier.ImageAugmentationOptions](mlimageclassifier/imageaugmentationoptions.md)
  The variations that the training process can use to generate more training data from the training data you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum)*