# MLHandActionClassifier.DataSource.labeledKeypointsDataFrame(_:sessionIdColumn:labelColumn:featureColumn:)

**Framework**: Create ML  
**Kind**: case

Creates a data source from a data frame of hand action observations that each contain the locations of each hand joint and an annotation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String = __Defaults.sessionIdColumnName, labelColumn: String = __Defaults.labelColumnName, featureColumn: String = __Defaults.featureColumnName)
```

## Parameters

- `dataFrame `: A data frame that contains the hand-joint locations and annotations for a set of hand   actions.
- `sessionIdColumn`: The name of the column in the data frame that contains the session identifiers.
- `labelColumn`: The name of the column in the data frame that contains the hand action label names.
- `featureColumn`: The name of the column in the data frame that contains the hand-joint location data.   Each entry in the column must be a    instance that contains three dimensions:

## See Also

- [MLHandActionClassifier.DataSource.labeledDirectories(at:)](mlhandactionclassifier/datasource/labeleddirectories(at:).md)
  Creates a data source from a folder with subfolders that each contain videos of a hand action.
- [MLHandActionClassifier.DataSource.labeledFiles(at:)](mlhandactionclassifier/datasource/labeledfiles(at:).md)
  Creates a data source from a folder that contains videos, each named after the hand action they represent.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlhandactionclassifier/datasource/directorywithvideosandannotation(at:annotationfile:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  Creates a data source from a folder that contains videos and an annotation file.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlhandactionclassifier/datasource/labeledvideodataframe(_:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  Creates a data source from a data frame that contains the location and annotation for a set of video files.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlhandactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  Creates a data source from a data table that contains the location and annotation for a set of video files.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data table of hand action observations that each contain the locations of each hand joint and an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:))*