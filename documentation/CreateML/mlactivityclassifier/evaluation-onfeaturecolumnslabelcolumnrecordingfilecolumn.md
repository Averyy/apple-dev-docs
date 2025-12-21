# evaluation(on:featureColumns:labelColumn:recordingFileColumn:)

**Framework**: Create ML  
**Kind**: method

Generates metrics describing the activity classifier’s performance on labeled activities in a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func evaluation(on testingData: MLActivityClassifier.DataSource, featureColumns: [String], labelColumn: String? = nil, recordingFileColumn: String? = nil) -> MLClassifierMetrics
```

#### Return Value

An [`MLClassifierMetrics`](mlclassifiermetrics.md) instance.

## Parameters

- `testingData`: The activity data that you provide to test this model, contained in an   .
- `featureColumns`: The names of the columns that contain sensor data.
- `labelColumn`: The name of the column that contain the activity labels. The method ignores this parameter if   the data source uses a labeled directory.
- `recordingFileColumn`: The name of the column that contain the recording file names. The method ignores this   parameter if the data source uses a labeled directory.

## See Also

- [var trainingMetrics: MLClassifierMetrics](mlactivityclassifier/trainingmetrics.md)
  Measurements of the activity classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](mlactivityclassifier/validationmetrics.md)
  Measurements of the activity classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/evaluation(on:featurecolumns:labelcolumn:recordingfilecolumn:))*