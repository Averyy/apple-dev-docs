# extractKeypoints(targetFrameRate:)

**Framework**: Create ML  
**Kind**: method

Extracts key points from video files if necessary.

**Availability**:
- macOS 14.0+

## Declaration

```swift
func extractKeypoints(targetFrameRate: Double = MLHandActionClassifier.__Defaults.targetFrameRate) throws -> DataFrame
```

#### Return Value

A data frame that contains a column for hand joint locations and a column of hand action annotations.

#### Discussion

If the data source already contains keypoints, this method just renames the data frame columns to the defaults.

## Parameters

- `targetFrameRate`: The number of frames per second the method uses to extract body landmarks from the   data source.

## See Also

- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
  A data source made up of keypoints in a data frame.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  A data table that contains the human body landmark movement data.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodataframe(_:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data source made up of video references in a data frame.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/extractkeypoints(targetframerate:))*