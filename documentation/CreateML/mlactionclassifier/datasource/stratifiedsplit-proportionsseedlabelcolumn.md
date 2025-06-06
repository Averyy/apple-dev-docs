# stratifiedSplit(proportions:seed:labelColumn:)

**Framework**: Create ML  
**Kind**: method

Generates a data table by splitting the data source into strata.

**Availability**:
- macOS 11.0+

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

- [func videosWithAnnotations() throws -> MLDataTable](mlactionclassifier/datasource/videoswithannotations.md)
  Generates a data table of the data source’s video URL locations and action annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](mlactionclassifier/datasource/keypointswithannotations(targetframerate:).md)
  Generates a data table with action annotations of the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:))*