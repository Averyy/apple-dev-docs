# evaluation(on:featureColumns:labelColumn:recordingFileColumn:)

**Framework**: Create ML  
**Kind**: method

Generates metrics describing the activity classifier’s performance on labeled activities in a data table.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func evaluation(on testingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String) -> MLClassifierMetrics
```

#### Return Value

An [`MLClassifierMetrics`](mlclassifiermetrics.md) instance.

## Parameters

- `testingData`: The activity data that you provide to test this model, contained in an  .
- `featureColumns`: The names of the columns that contain the sensor data.
- `labelColumn`: The name of the column that contain the activity labels.
- `recordingFileColumn`: The name of the column that contain the recording file names.

## See Also

- [func evaluation(on: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String?, recordingFileColumn: String?) -> MLClassifierMetrics](mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:)-1ib5p.md)
  Generates metrics describing the activity classifier’s performance on labeled activities in a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:)-3r5em)*