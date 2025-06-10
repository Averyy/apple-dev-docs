# MLObjectDetector.ModelParameters.ValidationData.dataSource(_:)

**Framework**: Create ML  
**Kind**: case

A validation dataset you provide as a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case dataSource(MLObjectDetector.DataSource)
```

## Parameters

- `dataSource `: An   instance the enumeration case uses as its associated   value.

## See Also

- [MLObjectDetector.ModelParameters.ValidationData.split(strategy:)](mlobjectdetector/modelparameters-swift.struct/validationdata/split(strategy:).md)
  A validation dataset Create ML derives by randomly selecting a portion of the object detector’s training dataset using the split strategy.
- [MLObjectDetector.ModelParameters.ValidationData.dataFrame(_:imageColumn:annotationColumn:)](mlobjectdetector/modelparameters-swift.struct/validationdata/dataframe(_:imagecolumn:annotationcolumn:).md)
  Set validation data from the MLDataTable provided.
- [MLObjectDetector.ModelParameters.ValidationData.table(_:imageColumn:annotationColumn:)](mlobjectdetector/modelparameters-swift.struct/validationdata/table(_:imagecolumn:annotationcolumn:).md)
  A validation dataset you provide as a data table.
- [MLObjectDetector.ModelParameters.ValidationData.none](mlobjectdetector/modelparameters-swift.struct/validationdata/none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/validationdata/datasource(_:))*