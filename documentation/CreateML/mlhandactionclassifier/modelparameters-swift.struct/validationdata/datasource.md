# MLHandActionClassifier.ModelParameters.ValidationData.dataSource(_:)

**Framework**: Create ML  
**Kind**: case

Creates a validation dataset from a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case dataSource(MLHandActionClassifier.DataSource)
```

#### Discussion

- dataSource: An [`MLHandActionClassifier.DataSource`](mlhandactionclassifier/datasource.md) instance.

## See Also

- [MLHandActionClassifier.ModelParameters.ValidationData.split(strategy:)](mlhandactionclassifier/modelparameters-swift.struct/validationdata/split(strategy:).md)
  Creates a validation dataset by randomly selecting a portion of the hand action classifier task’s training dataset with a split strategy.
- [MLHandActionClassifier.ModelParameters.ValidationData.none](mlhandactionclassifier/modelparameters-swift.struct/validationdata/none.md)
  Creates an empty validation dataset, which tells the task to skip the model validation phase in a training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/modelparameters-swift.struct/validationdata/datasource(_:))*