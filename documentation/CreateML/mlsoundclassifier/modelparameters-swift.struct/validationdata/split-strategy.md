# MLSoundClassifier.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case

A validation dataset derived by randomly selecting a portion of the sound classifier’s training dataset using the split strategy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

#### Discussion

- strategy: The partition method this case uses to create the validation dataset from the training dataset.

## See Also

- [MLSoundClassifier.ModelParameters.ValidationData.dataSource(_:)](mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:)](mlsoundclassifier/modelparameters-swift.struct/validationdata/dictionary(_:).md)
  A validation dataset represented by a dictionary.
- [MLSoundClassifier.ModelParameters.ValidationData.none](mlsoundclassifier/modelparameters-swift.struct/validationdata/none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/split(strategy:))*