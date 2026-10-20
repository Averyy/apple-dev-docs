# keypointsWithAnnotations(targetFrameRate:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates a data table that contains a column for hand joint locations and a column of hand action annotations.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- visionOS 1.0+

> **Deprecated**: Use extractKeypoints(targetFrameRate:)

## Declaration

```swift
func keypointsWithAnnotations(targetFrameRate: Double = MLHandActionClassifier.__Defaults.targetFrameRate) throws -> MLDataTable
```

## Parameters

- `targetFrameRate`: The number of frames per second the method uses to extract body landmarks from the data source.

  This parameter has no effect if the data source is either:

  - [`MLHandActionClassifier.DataSource.labeledKeypointsDataFrame(_:sessionIdColumn:labelColumn:featureColumn:)`](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  - [`MLHandActionClassifier.DataSource.labeledKeypointsData(table:sessionIdColumn:labelColumn:featureColumn:)`](./labeledkeypointsdata%28table,sessionidcolumn,labelcolumn,featurecolumn%29.md)

## See Also

### Exporting a data source
- [func labeledMedia() throws -> [String : [URL]]](./labeledmedia%28%29.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s video files.
- [func videosWithAnnotations() throws -> MLDataTable](./videoswithannotations%28%29.md)
  Generates a data table that contains a column for the data source’s video file URLs and a column of annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](./stratifiedsplit%28proportions,seed,labelcolumn%29.md)
  Generates a data table by splitting the data source into strata.
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](./extractkeypoints%28targetframerate%29.md)
  Extracts key points from video files if necessary.
- [func gatherAnnotatedFileNames() throws -> DataFrame?](./gatherannotatedfilenames%28%29.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/keypointswithannotations(targetframerate:))*