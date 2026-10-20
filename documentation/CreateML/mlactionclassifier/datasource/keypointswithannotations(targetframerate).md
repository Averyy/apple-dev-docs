# keypointsWithAnnotations(targetFrameRate:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates a data table with action annotations of the data source.

**Availability**:
- macOS 11.0+ - Deprecated in 14.0

> **Deprecated**: Use extractKeypoints(targetFrameRate:)

## Declaration

```swift
func keypointsWithAnnotations(targetFrameRate: Double = MLActionClassifier.__Defaults.targetFrameRate) throws -> MLDataTable
```

#### Return Value

A data table.

## Parameters

- `targetFrameRate`: The number of frames per second the method uses to extract body landmarks from the data source. This no effect if the data source is an [`MLActionClassifier.DataSource.labeledKeypointsDataFrame(_:sessionIdColumn:labelColumn:featureColumn:)`](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md) or an [`MLActionClassifier.DataSource.labeledKeypointsData(table:sessionIdColumn:labelColumn:featureColumn:)`](./labeledkeypointsdata%28table,sessionidcolumn,labelcolumn,featurecolumn%29.md).

## See Also

### Generating data tables from a data source
- [func videosWithAnnotations() throws -> MLDataTable](./videoswithannotations%28%29.md)
  Generates a data table of the data source’s video URL locations and action annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](./stratifiedsplit%28proportions,seed,labelcolumn%29.md)
  Generates a data table by splitting the data source into strata.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/keypointswithannotations(targetframerate:))*