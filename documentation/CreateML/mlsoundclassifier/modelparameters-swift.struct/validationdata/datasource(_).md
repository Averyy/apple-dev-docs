# MLSoundClassifier.ModelParameters.ValidationData.dataSource(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A validation dataset represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 11.0+
- visionOS 1.0+

## Declaration

```swift
case dataSource(MLSoundClassifier.DataSource)
```

## Discussion

- dataSource: An [`MLSoundClassifier.DataSource`](../../datasource.md) instance that contains a validation dataset.

## See Also

### Designating validation data
- [MLSoundClassifier.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  A validation dataset derived by randomly selecting a portion of the sound classifier’s training dataset using the split strategy.
- [MLSoundClassifier.ModelParameters.ValidationData.dictionary(_:)](./dictionary%28_%29.md)
  A validation dataset represented by a dictionary.
- [MLSoundClassifier.ModelParameters.ValidationData.none](./none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/modelparameters-swift.struct/validationdata/datasource(_:))*