# MLSoundClassifier.ModelParameters.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum

The feature-extractor options for a sound-classifier training algorithm.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
enum FeatureExtractorType
```

#### Overview

Use the [`MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)`](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:).md) feature extractor to create a model with the following advantages over `vggish`:

- More accurate predictions
- Lower latency
- Smaller model file size
- Less training time

Use [`MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)`](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:).md) to support older OS versions.

## Topics

### Designating a feature extractor
- [case audioFeaturePrint(type: MLSoundClassifier.ModelParameters.FeaturePrintType, revision: Int)](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:).md)
  Represents the Audio Feature Print extractor.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](mlsoundclassifier/modelparameters-swift.struct/featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:).md)
  Represents the VGGish feature extractor, which is compatible with older OS versions.
### Describing a feature extractor
- [var description: String](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/description.md)
  A text representation of the feature-extractor type.

## Relationships

### Conforms To
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [MLSoundClassifier.ModelParameters.ValidationData](mlsoundclassifier/modelparameters-swift.struct/validationdata.md)
  The source of a validation dataset for a sound classifier.
- [MLSoundClassifier.ModelParameters.ModelAlgorithmType](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The algorithm options to train a sound classifier.
- [MLSoundClassifier.ModelParameters.ClassifierType](mlsoundclassifier/modelparameters-swift.struct/classifiertype.md)
  The classifier options for a sound classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](mlsoundclassifier/modelparameters-swift.struct/featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)*