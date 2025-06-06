# labeledSensorData(featureColumns:labelColumn:recordingFileColumn:)

**Framework**: Create ML  
**Kind**: method

Generates a data table from the contents of the data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func labeledSensorData(featureColumns: [String], labelColumn: String? = nil, recordingFileColumn: String? = nil) throws -> MLDataTable
```

#### Return Value

A new [`MLDataTable`](mldatatable.md) instance.

#### Discussion

The `labelColumn` and `recordingFileColumn` parameters are optional if the data source is [`MLActivityClassifier.DataSource.labeledDirectories(at:)`](mlactivityclassifier/datasource/labeleddirectories(at:).md). If `nil`, the method names the data table’s label column and data file column “label” and “recordingFile”, respectively.

## Parameters

- `featureColumns`: The names of the feature columns the method includes in the   it   generates.
- `labelColumn`: The name of the label column. This parameter must not be   if the data source uses   .
- `recordingFileColumn`: The name of the column with the recording file names. This parameter must not be    if the data source uses   .

## See Also

- [func stratifiedSplit(proportions: [Double], seed: Int, featureColumns: [String], labelColumn: String, recordingFileColumn: String) throws -> MLDataTable](mlactivityclassifier/datasource/stratifiedsplit(proportions:seed:featurecolumns:labelcolumn:recordingfilecolumn:).md)
  Generates a data table by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource/labeledsensordata(featurecolumns:labelcolumn:recordingfilecolumn:))*