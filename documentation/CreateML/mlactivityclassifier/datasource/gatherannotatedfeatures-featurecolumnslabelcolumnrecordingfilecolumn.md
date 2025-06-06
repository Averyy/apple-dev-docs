# gatherAnnotatedFeatures(featureColumns:labelColumn:recordingFileColumn:)

**Framework**: Create ML  
**Kind**: method

Processes the data source and returns a data frame that contains features, labels and file names.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func gatherAnnotatedFeatures(featureColumns: [String], labelColumn: String = "label", recordingFileColumn: String? = nil) throws -> DataFrame
```

## Parameters

- `featureColumns`: The names of the feature columns.
- `labelColumn`: The name of the column with the labels.
- `recordingFileColumn`: The name of the column with the recording file names, if any.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactivityclassifier/datasource/gatherannotatedfeatures(featurecolumns:labelcolumn:recordingfilecolumn:))*