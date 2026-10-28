# MLActionClassifier.DataSource.labeledVideoDataFrame(_:videoColumn:labelColumn:startTimeColumn:endTimeColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

A data source made up of video references in a data frame.

**Availability**:
- macOS 12.0+

## Declaration

```swift
case labeledVideoDataFrame(DataFrame, videoColumn: String = __Defaults.videoColumnName, labelColumn: String = __Defaults.labelColumnName, startTimeColumn: String? = nil, endTimeColumn: String? = nil)
```

## Discussion

The data frame must contain a column of video file paths and a column of labels. It can also contain columns with start and end times.

## Parameters

- `dataFrame`: A `DataFrame` containing video paths and labels.
- `videoColumn`: The name of the column containing the video paths. Defaults to “videoPath”.
- `labelColumn`: The name of the column containing the labels. Defaults to “label”.
- `startTimeColumn`: The name of the column containing the start time. If `nil` start time is 0.
- `endTimeColumn`: The name of the column containing the end time. If `nil` end time is the end of the video.

## See Also

### Extracting key points
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](./extractkeypoints%28targetframerate%29.md)
  Extracts key points from video files if necessary.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  A data source made up of keypoints in a data frame.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdata%28table,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  A data table that contains the human body landmark movement data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/labeledvideodataframe(_:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:))*