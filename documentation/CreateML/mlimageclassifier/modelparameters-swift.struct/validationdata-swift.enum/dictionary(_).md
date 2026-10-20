# MLImageClassifier.ModelParameters.ValidationData.dictionary(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A validation dataset represented by a dictionary.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 11.0
- visionOS 1.0+

> **Deprecated**: Use DataSource.filesByLabel to provide dictionary validation data instead.

## Declaration

```swift
case dictionary([String : [URL]])
```

## See Also

### Designating validation data
- [MLImageClassifier.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  A validation dataset derived by randomly selecting a portion of the image classifier’s training dataset using the split strategy.
- [MLImageClassifier.ModelParameters.ValidationData.dataSource(_:)](./datasource%28_%29.md)
  A validation dataset represented by a data source.
- [MLImageClassifier.ModelParameters.ValidationData.none](./none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/modelparameters-swift.struct/validationdata-swift.enum/dictionary(_:))*