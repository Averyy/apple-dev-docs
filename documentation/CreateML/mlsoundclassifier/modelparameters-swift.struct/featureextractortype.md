# MLSoundClassifier.ModelParameters.FeatureExtractorType

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

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

## Overview

Use the [`MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)`](./featureextractortype/audiofeatureprint%28type,revision%29.md) feature extractor to create a model with the following advantages over `vggish`:

- More accurate predictions
- Lower latency
- Smaller model file size
- Less training time

Use [`MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)`](./featureextractortype/vggish%28revision%29.md) to support older OS versions.

## Topics

### Designating a feature extractor
- [case audioFeaturePrint(type: MLSoundClassifier.ModelParameters.FeaturePrintType, revision: Int)](./featureextractortype/audiofeatureprint%28type,revision%29.md)
  Represents the Audio Feature Print extractor.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](./featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)](./featureextractortype/vggish%28revision%29.md)
  Represents the VGGish feature extractor, which is compatible with older OS versions.
### Describing a feature extractor
- [var description: String](./featureextractortype/description.md)
  A text representation of the feature-extractor type.

## Relationships

### Conforms To
- [CustomStringConvertible](../../../Swift/customstringconvertible.md)
- [Equatable](../../../Swift/equatable.md)
- [Sendable](../../../Swift/sendable.md)
- [SendableMetatype](../../../Swift/sendablemetatype.md)

## See Also

### Supporting types
- [MLSoundClassifier.ModelParameters.ValidationData](./validationdata.md)
  The source of a validation dataset for a sound classifier.
- [MLSoundClassifier.ModelParameters.ModelAlgorithmType](./modelalgorithmtype.md)
  The algorithm options to train a sound classifier.
- [MLSoundClassifier.ModelParameters.ClassifierType](./classifiertype.md)
  The classifier options for a sound classifier training algorithm.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](./featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype)*