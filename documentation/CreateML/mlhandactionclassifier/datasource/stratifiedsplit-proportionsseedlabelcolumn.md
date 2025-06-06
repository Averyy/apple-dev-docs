# stratifiedSplit(proportions:seed:labelColumn:)

**Framework**: Create ML  
**Kind**: method

Generates a data table by splitting the data source into strata.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func stratifiedSplit(proportions: [Double], seed: Int = timestampSeed(), labelColumn: String) throws -> MLDataTable
```

#### Return Value

A new data table.

## Parameters

- `proportions`: An array of proportions, each in the range  .
- `seed`: A seed number for the random-number generator.
- `labelColumn`: The name of the column that you want to stratify.

## See Also

- [func labeledMedia() throws -> [String : [URL]]](mlhandactionclassifier/datasource/labeledmedia.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s video files.
- [func videosWithAnnotations() throws -> MLDataTable](mlhandactionclassifier/datasource/videoswithannotations.md)
  Generates a data table that contains a column for the data source’s video file URLs and a column of annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](mlhandactionclassifier/datasource/keypointswithannotations(targetframerate:).md)
  Generates a data table that contains a column for hand joint locations and a column of hand action annotations.
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](mlhandactionclassifier/datasource/extractkeypoints(targetframerate:).md)
  Extracts key points from video files if necessary.
- [func gatherAnnotatedFileNames() throws -> DataFrame?](mlhandactionclassifier/datasource/gatherannotatedfilenames.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:))*