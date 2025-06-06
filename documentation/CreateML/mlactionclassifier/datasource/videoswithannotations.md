# videosWithAnnotations()

**Framework**: Create ML  
**Kind**: method

Generates a data table of the data source’s video URL locations and action annotations.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func videosWithAnnotations() throws -> MLDataTable
```

#### Return Value

A data table.

#### Discussion

The data table includes a column for the annotation’s label, and if applicable, the annotation’s starting- and ending-time indices.

## See Also

- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](mlactionclassifier/datasource/keypointswithannotations(targetframerate:).md)
  Generates a data table with action annotations of the data source.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](mlactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:).md)
  Generates a data table by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/videoswithannotations())*