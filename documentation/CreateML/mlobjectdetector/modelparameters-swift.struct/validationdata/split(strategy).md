# MLObjectDetector.ModelParameters.ValidationData.split(strategy:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A validation dataset Create ML derives by randomly selecting a portion of the object detector’s training dataset using the split strategy.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case split(strategy: MLSplitStrategy)
```

## Parameters

- `strategy`: An [`MLSplitStrategy`](../../../mlsplitstrategy.md) instance the enumeration case uses to select a portion of the object detector’s training dataset as its associated value.

## See Also

### Designating validation data
- [MLObjectDetector.ModelParameters.ValidationData.dataFrame(_:imageColumn:annotationColumn:)](./dataframe%28_,imagecolumn,annotationcolumn%29.md)
  Set validation data from the MLDataTable provided.
- [MLObjectDetector.ModelParameters.ValidationData.dataSource(_:)](./datasource%28_%29.md)
  A validation dataset you provide as a data source.
- [MLObjectDetector.ModelParameters.ValidationData.table(_:imageColumn:annotationColumn:)](./table%28_,imagecolumn,annotationcolumn%29.md)
  A validation dataset you provide as a data table.
- [MLObjectDetector.ModelParameters.ValidationData.none](./none.md)
  An empty validation dataset that skips the model validation phase after training.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/modelparameters-swift.struct/validationdata/split(strategy:))*