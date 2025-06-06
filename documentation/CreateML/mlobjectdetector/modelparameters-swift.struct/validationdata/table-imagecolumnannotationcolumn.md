# MLObjectDetector.ModelParameters.ValidationData.table(_:imageColumn:annotationColumn:)

**Framework**: Create ML  
**Kind**: case

A validation dataset you provide as a data table.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case table(MLDataTable, imageColumn: String, annotationColumn: String)
```

#### Discussion

- table : An [`MLDataTable`](mldatatable.md) instance the enumeration case uses as its associated value.
- imageColumn: The name of the column in the data table that contains the image file URLs.
- annotationColumn : The name of the column in the data table that contains the image annotations.

## See Also

- [MLObjectDetector.ModelParameters.ValidationData.split(strategy:)](mlobjectdetector/modelparameters-swift.struct/validationdata/split(strategy:).md)
  A validation dataset Create ML derives by randomly selecting a portion of the object detector’s training dataset using the split strategy.
- [MLObjectDetector.ModelParameters.ValidationData.dataFrame(_:imageColumn:annotationColumn:)](mlobjectdetector/modelparameters-swift.struct/validationdata/dataframe(_:imagecolumn:annotationcolumn:).md)
  Set validation data from the MLDataTable provided.
- [MLObjectDetector.ModelParameters.ValidationData.dataSource(_:)](mlobjectdetector/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset you provide as a data source.
- [MLObjectDetector.ModelParameters.ValidationData.none](mlobjectdetector/modelparameters-swift.struct/validationdata/none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/validationdata/table(_:imagecolumn:annotationcolumn:))*