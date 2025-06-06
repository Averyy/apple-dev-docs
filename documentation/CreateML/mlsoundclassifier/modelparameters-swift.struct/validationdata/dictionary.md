# MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:)

**Framework**: Create ML  
**Kind**: case

A validation dataset represented by a dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case dictionary([String : [URL]])
```

#### Discussion

- dictionary: A validation dataset that uses a collection of labeled audio files represented by a dictionary. Each key of the dictionary is a label, and its value is an array of audio-file URLs.

## See Also

- [MLSoundClassifier.ModelParameters.ValidationData.split(strategy:)](mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  A validation dataset derived by randomly selecting a portion of the sound classifier’s training dataset using the split strategy.
- [MLSoundClassifier.ModelParameters.ValidationData.dataSource(_:)](mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLSoundClassifier.ModelParameters.ValidationData.none](mlsoundclassifier/modelparameters-swift.struct/validationdata/none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:))*