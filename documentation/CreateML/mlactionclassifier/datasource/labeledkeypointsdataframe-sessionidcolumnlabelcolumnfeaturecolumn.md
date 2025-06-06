# MLActionClassifier.DataSource.labeledKeypointsDataFrame(_:sessionIdColumn:labelColumn:featureColumn:)

**Framework**: Create ML  
**Kind**: case

A data source made up of keypoints in a data frame.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String = __Defaults.sessionIdColumnName, labelColumn: String = __Defaults.labelColumnName, featureColumn: String = __Defaults.featureColumnName)
```

#### Discussion

The data frame must contain a column of session identifiers, a column of labels, and a column of keypoints. Each set of keypoints must be a multi-dimensional 1x3x18 array containing the x, y, z coordinates of each of the 18 keypoints. See `VNRecognizedPointsObservation` for more details.

## Parameters

- `dataFrame`: A   containing keypoints and labels.
- `sessionIdColumn`: The name of the column containing session identifiers. Defaults to “session_id”.
- `labelColumn`: The name of the column containing the labels. Defaults to “label”.
- `featureColumn`: The name of the column containing the keypoints. Defaults to “keypoints”.

## See Also

- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](mlactionclassifier/datasource/extractkeypoints(targetframerate:).md)
  Extracts key points from video files if necessary.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  A data table that contains the human body landmark movement data.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodataframe(_:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data source made up of video references in a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:))*