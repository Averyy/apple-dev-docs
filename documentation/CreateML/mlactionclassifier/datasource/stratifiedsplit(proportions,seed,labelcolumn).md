# stratifiedSplit(proportions:seed:labelColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates a data table by splitting the data source into strata.

**Availability**:
- macOS 11.0+ - Deprecated in 14.0

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

### Generating data tables from a data source
- [func videosWithAnnotations() throws -> MLDataTable](./videoswithannotations%28%29.md)
  Generates a data table of the data source’s video URL locations and action annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](./keypointswithannotations%28targetframerate%29.md)
  Generates a data table with action annotations of the data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:))*