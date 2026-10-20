# MLActionClassifier.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A validation dataset derived by randomly selecting a portion of the action classifier’s training dataset using the split strategy.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

## See Also

### Designating validation data
- [MLActionClassifier.ModelParameters.ValidationData.dataSource(_:)](./datasource%28_%29.md)
  A validation dataset represented by a data source.
- [MLActionClassifier.ModelParameters.ValidationData.none](./none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/validationdata/split(strategy:))*