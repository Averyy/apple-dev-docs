# stratifiedSplit(proportions:seed:labelColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates a data table by splitting the data source into strata.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- visionOS 1.0+

> **Deprecated**: Use DataFrame.stratifiedSplit(on:by:)

## Declaration

```swift
func stratifiedSplit(proportions: [Double], seed: Int = timestampSeed(), labelColumn: String) throws -> MLDataTable
```

## Return Value

A new data table.

## Parameters

- `proportions`: An array of proportions, each in the range `[0.0, 1.0]`.
- `seed`: A seed number for the random-number generator.
- `labelColumn`: The name of the column that you want to stratify.

## See Also

### Exporting a data source
- [func labeledMedia() throws -> [String : [URL]]](./labeledmedia%28%29.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s video files.
- [func videosWithAnnotations() throws -> MLDataTable](./videoswithannotations%28%29.md)
  Generates a data table that contains a column for the data source’s video file URLs and a column of annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](./keypointswithannotations%28targetframerate%29.md)
  Generates a data table that contains a column for hand joint locations and a column of hand action annotations.
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](./extractkeypoints%28targetframerate%29.md)
  Extracts key points from video files if necessary.
- [func gatherAnnotatedFileNames() throws -> DataFrame?](./gatherannotatedfilenames%28%29.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:))*