# MLObjectDetector.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case

A validation dataset Create ML derives by randomly selecting a portion of the object detector’s training dataset using the split strategy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

#### Discussion

- strategy: An [`MLSplitStrategy`](mlsplitstrategy.md) instance the enumeration case uses to select a portion of the object detector’s training dataset as its associated value.

## See Also

- [MLObjectDetector.ModelParameters.ValidationData.dataFrame(_:imageColumn:annotationColumn:)](mlobjectdetector/modelparameters-swift.struct/validationdata/dataframe(_:imagecolumn:annotationcolumn:).md)
  Set validation data from the MLDataTable provided.
- [MLObjectDetector.ModelParameters.ValidationData.dataSource(_:)](mlobjectdetector/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset you provide as a data source.
- [MLObjectDetector.ModelParameters.ValidationData.table(_:imageColumn:annotationColumn:)](mlobjectdetector/modelparameters-swift.struct/validationdata/table(_:imagecolumn:annotationcolumn:).md)
  A validation dataset you provide as a data table.
- [MLObjectDetector.ModelParameters.ValidationData.none](mlobjectdetector/modelparameters-swift.struct/validationdata/none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/validationdata/split(strategy:))*