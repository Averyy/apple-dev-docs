# MLActionClassifier.ModelParameters.ValidationData.dataSource(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A validation dataset represented by a data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case dataSource(MLActionClassifier.DataSource)
```

## See Also

### Designating validation data
- [MLActionClassifier.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  A validation dataset derived by randomly selecting a portion of the action classifier’s training dataset using the split strategy.
- [MLActionClassifier.ModelParameters.ValidationData.none](./none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/validationdata/datasource(_:))*