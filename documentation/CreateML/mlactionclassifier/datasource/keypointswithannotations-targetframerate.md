# keypointsWithAnnotations(targetFrameRate:)

**Framework**: Create ML  
**Kind**: method

Generates a data table with action annotations of the data source.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func keypointsWithAnnotations(targetFrameRate: Double = MLActionClassifier.__Defaults.targetFrameRate) throws -> MLDataTable
```

#### Return Value

A data table.

## Parameters

- `targetFrameRate`: The number of frames per second the method uses to extract body landmarks from the   data source. This no effect if the data source is an     or an   .

## See Also

- [func videosWithAnnotations() throws -> MLDataTable](mlactionclassifier/datasource/videoswithannotations.md)
  Generates a data table of the data source’s video URL locations and action annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](mlactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:).md)
  Generates a data table by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/keypointswithannotations(targetframerate:))*