# extractKeypoints(targetFrameRate:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Extracts key points from video files if necessary.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- visionOS 1.0+

## Declaration

```swift
func extractKeypoints(targetFrameRate: Double = MLHandActionClassifier.__Defaults.targetFrameRate) throws -> DataFrame
```

#### Return Value

A data frame that contains a column for hand joint locations and a column of hand action annotations.

#### Discussion

If the data source already contains keypoints, this method just renames the data frame columns to the defaults.

## Parameters

- `targetFrameRate`: The number of frames per second the method uses to extract body landmarks from the data source.

## See Also

### Exporting a data source
- [func labeledMedia() throws -> [String : [URL]]](./labeledmedia%28%29.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s video files.
- [func videosWithAnnotations() throws -> MLDataTable](./videoswithannotations%28%29.md)
  Generates a data table that contains a column for the data source’s video file URLs and a column of annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](./keypointswithannotations%28targetframerate%29.md)
  Generates a data table that contains a column for hand joint locations and a column of hand action annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](./stratifiedsplit%28proportions,seed,labelcolumn%29.md)
  Generates a data table by splitting the data source into strata.
- [func gatherAnnotatedFileNames() throws -> DataFrame?](./gatherannotatedfilenames%28%29.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/extractkeypoints(targetframerate:))*