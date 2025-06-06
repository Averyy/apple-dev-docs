# MLActionClassifier.ModelParameters.ValidationData.none

**Framework**: Create ML  
**Kind**: case

An empty validation dataset that skips the model validation phase after training.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case none
```

#### Discussion

Use this case when you don’t have validation data while preventing Create ML from using any of your training dataset for validation.

## See Also

- [MLActionClassifier.ModelParameters.ValidationData.dataSource(_:)](mlactionclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset represented by a data source.
- [MLActionClassifier.ModelParameters.ValidationData.split(strategy:)](mlactionclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  A validation dataset derived by randomly selecting a portion of the action classifier’s training dataset using the split strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/modelparameters-swift.struct/validationdata/none)*