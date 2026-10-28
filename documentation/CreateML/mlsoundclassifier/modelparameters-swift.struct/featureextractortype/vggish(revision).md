# MLSoundClassifier.ModelParameters.FeatureExtractorType.vggish(revision:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Represents the VGGish feature extractor, which is compatible with older OS versions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case vggish(revision: Int = 1)
```

## Discussion

The case uses the newest version if you don’t provide an associated value for `revision`.

## Parameters

- `revision`: A version of the VGGish feature extractor.

## See Also

### Designating a feature extractor
- [case audioFeaturePrint(type: MLSoundClassifier.ModelParameters.FeaturePrintType, revision: Int)](./audiofeatureprint%28type,revision%29.md)
  Represents the Audio Feature Print extractor.
- [MLSoundClassifier.ModelParameters.FeaturePrintType](../featureprinttype.md)
  The type options for an Audio Feature Print feature extractor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/featureextractortype/vggish(revision:))*