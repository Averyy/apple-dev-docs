# MLActionClassifier.DataSource.labeledVideoData(table:videoColumn:labelColumn:startTimeColumn:endTimeColumn:)

**Framework**: Create ML  
**Kind**: case

A data table that contains the locations of the video files and the action annotations.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case labeledVideoData(table: MLDataTable, videoColumn: String = __Defaults.videoColumnName, labelColumn: String = __Defaults.labelColumnName, startTimeColumn: String? = nil, endTimeColumn: String? = nil)
```

## Parameters

- `table`: A data table that contains the video file locations and the action annotations.
- `videoColumn`: The name of the column that contains the URLs to the video files.
- `labelColumn`: The name of the column that contains the labels of the action the person demonstrates in   the video file.
- `startTimeColumn`: The name of the column that contains the action’s starting-time index in the video   file.
- `endTimeColumn `: The name of the column that contains the action’s ending-time index in the video file.

## See Also

- [MLActionClassifier.DataSource.labeledDirectories(at:)](mlactionclassifier/datasource/labeleddirectories(at:).md)
  The location of a folder with subfolders each of which contain sample videos of an action.
- [MLActionClassifier.DataSource.labeledFiles(at:)](mlactionclassifier/datasource/labeledfiles(at:).md)
  The location of a folder that contains video files whose names you use to label corresponding actions.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/directorywithvideosandannotation(at:annotationfile:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  The location of a directory of video files, and the location of an action annotation file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:))*