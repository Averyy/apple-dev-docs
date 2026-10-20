# MLSoundClassifier.ModelParameters.FeatureExtractorType.audioFeaturePrint(type:revision:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Represents the Audio Feature Print extractor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case audioFeaturePrint(type: MLSoundClassifier.ModelParameters.FeaturePrintType = .sound, revision: Int = 1)
```

#### Discussion

The case uses the newest version of [`MLSoundClassifier.ModelParameters.FeaturePrintType.sound`](../featureprinttype/sound.md) if you don’t provide associated values for `type` and `revision`.

## Parameters

- `type`: An Audio Feature Print extractor type.
- `revision`: A version of the extractor you pass to `type`.

## See Also

### Designating a feature extractor
- [MLSoundClassifier.ModelParameters.FeaturePrintType](../featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.
- [MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)](./vggish%28revision%29.md)
  Represents the VGGish feature extractor, which is compatible with older OS versions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/audiofeatureprint(type:revision:))*