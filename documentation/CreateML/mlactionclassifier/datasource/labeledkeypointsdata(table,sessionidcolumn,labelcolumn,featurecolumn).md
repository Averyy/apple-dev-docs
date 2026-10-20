# MLActionClassifier.DataSource.labeledKeypointsData(table:sessionIdColumn:labelColumn:featureColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A data table that contains the human body landmark movement data.

**Availability**:
- macOS 11.0+ - Deprecated in 14.0

## Declaration

```swift
case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String = __Defaults.sessionIdColumnName, labelColumn: String = __Defaults.labelColumnName, featureColumn: String = __Defaults.featureColumnName)
```

## Parameters

- `table`: A data table that contains the human body landmark locations and the action annotations.
- `sessionIdColumn`: The name of the column that contains the action session’s unique identifier.
- `labelColumn`: The name of the column that contains the labels of the action the person demonstrates in the session.
- `featureColumn `: The name of the column that contains the movement data.

## See Also

### Extracting key points
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](./extractkeypoints%28targetframerate%29.md)
  Extracts key points from video files if necessary.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  A data source made up of keypoints in a data frame.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](./labeledvideodataframe%28_,videocolumn,labelcolumn,starttimecolumn,endtimecolumn%29.md)
  A data source made up of video references in a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:))*