# MLActionClassifier.DataSource.labeledKeypointsData(table:sessionIdColumn:labelColumn:featureColumn:)

**Framework**: Create ML  
**Kind**: case

A data table that contains the human body landmark movement data.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String = __Defaults.sessionIdColumnName, labelColumn: String = __Defaults.labelColumnName, featureColumn: String = __Defaults.featureColumnName)
```

## Parameters

- `table`: A data table that contains the human body landmark locations and the action annotations.
- `sessionIdColumn`: The name of the column that contains the action session’s unique identifier.
- `labelColumn`: The name of the column that contains the labels of the action the person demonstrates in   the session.
- `featureColumn `: The name of the column that contains the movement data.

## See Also

- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](mlactionclassifier/datasource/extractkeypoints(targetframerate:).md)
  Extracts key points from video files if necessary.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
  A data source made up of keypoints in a data frame.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodataframe(_:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data source made up of video references in a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:))*