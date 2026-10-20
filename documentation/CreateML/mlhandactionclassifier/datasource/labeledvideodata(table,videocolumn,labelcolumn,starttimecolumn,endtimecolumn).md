# MLHandActionClassifier.DataSource.labeledVideoData(table:videoColumn:labelColumn:startTimeColumn:endTimeColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Creates a data source from a data table that contains the location and annotation for a set of video files.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- visionOS 1.0+

## Declaration

```swift
case labeledVideoData(table: MLDataTable, videoColumn: String = __Defaults.videoColumnName, labelColumn: String = __Defaults.labelColumnName, startTimeColumn: String? = nil, endTimeColumn: String? = nil)
```

#### Discussion

- endTimeColumn: The name of the column in the data table that contains the hand action’s ending-time in the video file. Otherwise `nil`, if every video example ends at the end of the video file.

## Parameters

- `table`: A data table that contains the locations of annotations for each hand action video file.
- `videoColumn`: The name of the column in the data table that contains the video filenames.
- `labelColumn`: The name of the column in the data table that contains the hand action label names.
- `startTimeColumn`: The name of the column in the data table that contains the hand action’s starting-time index in the video file. Otherwise `nil`, if every video example starts at the beginning of the video file.

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
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  Creates a data source from a data frame of hand action observations that each contain the locations of each hand joint and an annotation.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdata%28table,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  Creates a data source from a data table of hand action observations that each contain the locations of each hand joint and an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:))*