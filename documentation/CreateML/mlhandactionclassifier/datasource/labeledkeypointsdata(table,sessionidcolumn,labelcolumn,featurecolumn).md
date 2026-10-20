# MLHandActionClassifier.DataSource.labeledKeypointsData(table:sessionIdColumn:labelColumn:featureColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Creates a data source from a data table of hand action observations that each contain the locations of each hand joint and an annotation.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- visionOS 1.0+

## Declaration

```swift
case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String = __Defaults.sessionIdColumnName, labelColumn: String = __Defaults.labelColumnName, featureColumn: String = __Defaults.featureColumnName)
```

## Parameters

- `table `: A data table that contains the hand-joint locations and annotations for a set of hand actions.
- `sessionIdColumn`: The name of the column in the data table that contains the session identifiers.
- `labelColumn`: The name of the column in the data table that contains the hand action label names.
- `featureColumn`: The name of the column in the data table that contains the hand-joint location data. Each entry in the column must be an [`MLMultiArray`](../../../CoreML/mlmultiarray.md) instance — which you must wrap in an [`MLDataValue.MultiArrayType`](../../mldatavalue/multiarraytype.md) — that contains three dimensions:

  - The first dimension has a size of one.
  - The second dimension has three channels: the x-coordinate, the y-coordinate, and the confidence value, respectively.
  - The third dimension has 21 channels, one for each hand joint.

## See Also

### Creating a data source
- [MLHandActionClassifier.DataSource.labeledDirectories(at:)](./labeleddirectories%28at%29.md)
  Creates a data source from a folder with subfolders that each contain videos of a hand action.
- [MLHandActionClassifier.DataSource.labeledFiles(at:)](./labeledfiles%28at%29.md)
  Creates a data source from a folder that contains videos, each named after the hand action they represent.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](./directorywithvideosandannotation%28at,annotationfile,videocolumn,labelcolumn,starttimecolumn,endtimecolumn%29.md)
  Creates a data source from a folder that contains videos and an annotation file.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](./labeledvideodataframe%28_,videocolumn,labelcolumn,starttimecolumn,endtimecolumn%29.md)
  Creates a data source from a data frame that contains the location and annotation for a set of video files.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](./labeledvideodata%28table,videocolumn,labelcolumn,starttimecolumn,endtimecolumn%29.md)
  Creates a data source from a data table that contains the location and annotation for a set of video files.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  Creates a data source from a data frame of hand action observations that each contain the locations of each hand joint and an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:))*