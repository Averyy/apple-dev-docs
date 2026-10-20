# MLHandPoseClassifier.ModelParameters.ValidationData.dataSource(_:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Creates a validation dataset from a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case dataSource(MLHandPoseClassifier.DataSource)
```

## Parameters

- `dataSource`: An [`MLHandPoseClassifier.DataSource`](../../datasource.md) instance.

## See Also

### Designating validation data
- [MLHandPoseClassifier.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  Creates a validation dataset by randomly selecting a portion of the hand pose classifier task’s training dataset with a split strategy.
- [MLHandPoseClassifier.ModelParameters.ValidationData.none](./none.md)
  Creates an empty validation dataset, which tells the task to skip the model validation phase in a training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/validationdata/datasource(_:))*