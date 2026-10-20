# labeledSensorData(featureColumns:labelColumn:recordingFileColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates a data table from the contents of the data source.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

> **Deprecated**: Use gatherAnnotatedFeatures(featureColumns:labelColumn:recordingFileColumn:)

## Declaration

```swift
func labeledSensorData(featureColumns: [String], labelColumn: String? = nil, recordingFileColumn: String? = nil) throws -> MLDataTable
```

#### Return Value

A new [`MLDataTable`](../../mldatatable.md) instance.

#### Discussion

The `labelColumn` and `recordingFileColumn` parameters are optional if the data source is [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](./labeleddirectories%28at%29.md). If `nil`, the method names the data table’s label column and data file column “label” and “recordingFile”, respectively.

## Parameters

- `featureColumns`: The names of the feature columns the method includes in the [`MLDataTable`](../../mldatatable.md) it generates.
- `labelColumn`: The name of the label column. This parameter must not be `nil` if the data source uses [`MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)`](./directorywithdataandannotation%28at,annotationfilename,timestampcolumn,labelstarttimecolumn,labelendtimecolumn%29.md).
- `recordingFileColumn`: The name of the column with the recording file names. This parameter must not be `nil` if the data source uses [`MLActivityClassifier.DataSource.directoryWithDataAndAnnotation(at:annotationFileName:timeStampColumn:labelStartTimeColumn:labelEndTimeColumn:)`](./directorywithdataandannotation%28at,annotationfilename,timestampcolumn,labelstarttimecolumn,labelendtimecolumn%29.md).

## See Also

### Generating data tables from a data source
- [func stratifiedSplit(proportions: [Double], seed: Int, featureColumns: [String], labelColumn: String, recordingFileColumn: String) throws -> MLDataTable](./stratifiedsplit%28proportions,seed,featurecolumns,labelcolumn,recordingfilecolumn%29.md)
  Generates a data table by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource/labeledsensordata(featurecolumns:labelcolumn:recordingfilecolumn:))*