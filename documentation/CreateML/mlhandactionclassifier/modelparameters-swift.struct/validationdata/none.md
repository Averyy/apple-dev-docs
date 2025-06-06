# MLHandActionClassifier.ModelParameters.ValidationData.none

**Framework**: Create ML  
**Kind**: case

Creates an empty validation dataset, which tells the task to skip the model validation phase in a training session.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case none
```

#### Discussion

This case prevents Create ML from creating a validation dataset from your training dataset. You typically use it when your training dataset is small and can’t spare any data to validate the model.

## See Also

- [MLHandActionClassifier.ModelParameters.ValidationData.dataSource(_:)](mlhandactionclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  Creates a validation dataset from a data source.
- [MLHandActionClassifier.ModelParameters.ValidationData.split(strategy:)](mlhandactionclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  Creates a validation dataset by randomly selecting a portion of the hand action classifier task’s training dataset with a split strategy.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.struct/validationdata/none)*