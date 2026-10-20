# MLObjectDetector.ModelParameters.ValidationData.dataFrame(_:imageColumn:annotationColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Set validation data from the MLDataTable provided.

**Availability**:
- macOS 13.0+

## Declaration

```swift
case dataFrame(DataFrame, imageColumn: String, annotationColumn: String)
```

## See Also

### Designating validation data
- [MLObjectDetector.ModelParameters.ValidationData.split(strategy:)](./split%28strategy%29.md)
  A validation dataset Create ML derives by randomly selecting a portion of the object detector’s training dataset using the split strategy.
- [MLObjectDetector.ModelParameters.ValidationData.dataSource(_:)](./datasource%28_%29.md)
  A validation dataset you provide as a data source.
- [MLObjectDetector.ModelParameters.ValidationData.table(_:imageColumn:annotationColumn:)](./table%28_,imagecolumn,annotationcolumn%29.md)
  A validation dataset you provide as a data table.
- [MLObjectDetector.ModelParameters.ValidationData.none](./none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/validationdata/dataframe(_:imagecolumn:annotationcolumn:))*