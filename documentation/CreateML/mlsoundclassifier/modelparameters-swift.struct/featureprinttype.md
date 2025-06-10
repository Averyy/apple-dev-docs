# MLSoundClassifier.ModelParameters.FeaturePrintType

**Framework**: Create ML  
**Kind**: enum

The type options for an Audio Feature Print feature extractor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum FeaturePrintType
```

## Topics

### Designating a feature-print type
- [MLSoundClassifier.ModelParameters.FeaturePrintType.sound](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/sound.md)
  Creates a feature print type for a sound classifier.
### Describing a feature-print type
- [var description: String](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/description.md)
  A text representation of the feature-print type.
### Comparing feature-print types
- [static func == (MLSoundClassifier.ModelParameters.FeaturePrintType, MLSoundClassifier.ModelParameters.FeaturePrintType) -> Bool](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/==(_:_:).md)
  Returns a Boolean value indicating whether two values are equal.
- [static func != (Self, Self) -> Bool](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/!=(_:_:).md)
  Returns a Boolean value indicating whether two values are not equal.
### Hashing a feature-print type
- [func hash(into: inout Hasher)](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/hash(into:).md)
  Hashes the essential components of this value by feeding them into the given hasher.
- [var hashValue: Int](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/hashvalue.md)
  The hash value.
### Default Implementations
- [Equatable Implementations](mlsoundclassifier/modelparameters-swift.struct/featureprinttype/equatable-implementations.md)

## Relationships

### Conforms To
- [Copyable](../Swift/Copyable.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case audioFeaturePrint(type: MLSoundClassifier.ModelParameters.FeaturePrintType, revision: Int)](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:).md)
  Represents the Audio Feature Print extractor.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)](mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:).md)
  Represents the VGGish feature extractor, which is compatible with older OS versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureprinttype)*