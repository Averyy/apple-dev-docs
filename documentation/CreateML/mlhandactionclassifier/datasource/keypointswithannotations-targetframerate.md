# keypointsWithAnnotations(targetFrameRate:)

**Framework**: Create ML  
**Kind**: method

Generates a data table that contains a column for hand joint locations and a column of hand action annotations.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func keypointsWithAnnotations(targetFrameRate: Double = MLHandActionClassifier.__Defaults.targetFrameRate) throws -> MLDataTable
```

## Parameters

- `targetFrameRate`: The number of frames per second the method uses to extract body landmarks from the data source. This parameter has no effect if the data source is either: - [`MLHandActionClassifier.DataSource.labeledKeypointsDataFrame(_:sessionIdColumn:labelColumn:featureColumn:)`](mlhandactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
- [`MLHandActionClassifier.DataSource.labeledKeypointsData(table:sessionIdColumn:labelColumn:featureColumn:)`](mlhandactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)

## See Also

- [func labeledMedia() throws -> [String : [URL]]](mlhandactionclassifier/datasource/labeledmedia.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s video files.
- [func videosWithAnnotations() throws -> MLDataTable](mlhandactionclassifier/datasource/videoswithannotations.md)
  Generates a data table that contains a column for the data source’s video file URLs and a column of annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](mlhandactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:).md)
  Generates a data table by splitting the data source into strata.
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](mlhandactionclassifier/datasource/extractkeypoints(targetframerate:).md)
  Extracts key points from video files if necessary.
- [func gatherAnnotatedFileNames() throws -> DataFrame?](mlhandactionclassifier/datasource/gatherannotatedfilenames.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/keypointswithannotations(targetframerate:))*