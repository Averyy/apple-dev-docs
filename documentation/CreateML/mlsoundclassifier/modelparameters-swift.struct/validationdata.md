# MLSoundClassifier.ModelParameters.ValidationData

**Framework**: Create ML  
**Kind**: enum

The source of a validation dataset for a sound classifier.

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
- [MLSoundClassifier.ModelParameters.ValidationData.split(strategy:)](mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  A validation dataset derived by randomly selecting a portion of the sound classifier’s training dataset using the split strategy.
- [MLSoundClassifier.ModelParameters.ValidationData.dataSource(_:)](mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:)](mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:).md)
  A validation dataset represented by a dictionary.
- [MLSoundClassifier.ModelParameters.ValidationData.none](mlsoundclassifier/modelparameters-swift.struct/validationdata/none.md)
  An empty validation dataset that skips the model validation phase after training.

## See Also

- [MLSoundClassifier.ModelParameters.ModelAlgorithmType](mlsoundclassifier/modelparameters-swift.struct/modelalgorithmtype.md)
  The algorithm options to train a sound classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata)*