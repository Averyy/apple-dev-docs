# evaluation(on:featureColumns:labelColumn:recordingFileColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates metrics describing the activity classifier’s performance on labeled activities in a data table.

**Availability**:
- macOS 10.15+ - Deprecated in 14.0

## Declaration

```swift
func evaluation(on testingData: MLDataTable, featureColumns: [String], labelColumn: String, recordingFileColumn: String) -> MLClassifierMetrics
```

**Other overloads**:

```swift
func evaluation(on testingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String? = nil, recordingFileColumn: String? = nil) -> MLClassifierMetrics
```

## Return Value

An [`MLClassifierMetrics`](../mlclassifiermetrics.md) instance.

## Parameters

- `testingData`: The activity data that you provide to test this model, contained in an [`MLDataTable`](../mldatatable.md).
- `featureColumns`: The names of the columns that contain the sensor data.
- `labelColumn`: The name of the column that contain the activity labels.
- `recordingFileColumn`: The name of the column that contain the recording file names.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:)-3r5em)*