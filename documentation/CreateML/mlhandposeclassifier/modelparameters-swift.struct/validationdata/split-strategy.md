# MLHandPoseClassifier.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case

Creates a validation dataset by randomly selecting a portion of the hand pose classifier task’s training dataset with a split strategy.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

## Parameters

- `strategy`: An   instance.

## See Also

- [MLHandPoseClassifier.ModelParameters.ValidationData.dataSource(_:)](mlhandposeclassifier/modelparameters-swift.struct/validationdata/datasource(_:).md)
  Creates a validation dataset from a data source.
- [MLHandPoseClassifier.ModelParameters.ValidationData.none](mlhandposeclassifier/modelparameters-swift.struct/validationdata/none.md)
  Creates an empty validation dataset, which tells the task to skip the model validation phase in a training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/modelparameters-swift.struct/validationdata/split(strategy:))*