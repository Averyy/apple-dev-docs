# stratifiedSplit(proportions:seed:featureColumns:labelColumn:recordingFileColumn:)

**Framework**: Create ML  
**Kind**: method

Generates a data table by splitting the data source into strata.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func stratifiedSplit(proportions: [Double], seed: Int = timestampSeed(), featureColumns: [String], labelColumn: String, recordingFileColumn: String) throws -> MLDataTable
```

#### Return Value

A new [`MLDataTable`](mldatatable.md) instance.

## Parameters

- `proportions`: An array of proportions, each in the range  .
- `seed`: A seed number for the random-number generator.
- `featureColumns`: The names of the feature columns the method includes in the data table.
- `labelColumn`: The name of the label column the methods stratifies.
- `recordingFileColumn`: The name of the column with the data file names.

## See Also

- [func labeledSensorData(featureColumns: [String], labelColumn: String?, recordingFileColumn: String?) throws -> MLDataTable](mlactivityclassifier/datasource/labeledsensordata(featurecolumns:labelcolumn:recordingfilecolumn:).md)
  Generates a data table from the contents of the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource/stratifiedsplit(proportions:seed:featurecolumns:labelcolumn:recordingfilecolumn:))*