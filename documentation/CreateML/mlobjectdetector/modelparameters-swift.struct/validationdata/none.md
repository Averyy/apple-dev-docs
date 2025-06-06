# MLObjectDetector.ModelParameters.ValidationData.none

**Framework**: Create ML  
**Kind**: case

An empty validation dataset that skips the model validation phase after training.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case none
```

#### Discussion

Use this case when you don’t have validation data while preventing Create ML from using any of your training dataset for validation.

## See Also

- [MLObjectDetector.ModelParameters.ValidationData.split(strategy:)](mlobjectdetector/modelparameters-swift.struct/validationdata/split(strategy:).md)
  A validation dataset Create ML derives by randomly selecting a portion of the object detector’s training dataset using the split strategy.
- [MLObjectDetector.ModelParameters.ValidationData.dataFrame(_:imageColumn:annotationColumn:)](mlobjectdetector/modelparameters-swift.struct/validationdata/dataframe(_:imagecolumn:annotationcolumn:).md)
  Set validation data from the MLDataTable provided.
- [MLObjectDetector.ModelParameters.ValidationData.dataSource(_:)](mlobjectdetector/modelparameters-swift.struct/validationdata/datasource(_:).md)
  A validation dataset you provide as a data source.
- [MLObjectDetector.ModelParameters.ValidationData.table(_:imageColumn:annotationColumn:)](mlobjectdetector/modelparameters-swift.struct/validationdata/table(_:imagecolumn:annotationcolumn:).md)
  A validation dataset you provide as a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/validationdata/none)*