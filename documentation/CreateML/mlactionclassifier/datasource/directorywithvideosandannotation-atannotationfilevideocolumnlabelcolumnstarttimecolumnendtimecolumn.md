# MLActionClassifier.DataSource.directoryWithVideosAndAnnotation(at:annotationFile:videoColumn:labelColumn:startTimeColumn:endTimeColumn:)

**Framework**: Create ML  
**Kind**: case

The location of a directory of video files, and the location of an action annotation file.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String? = nil, endTimeColumn: String? = nil)
```

## Parameters

- `at`: The location of a directory that contains video files.
- `annotationFile`: The location of a JSON or CSV file with object annotations for the images.
- `videoColumn`: The name of the column that contains the URLs to the video files.
- `labelColumn`: The name of the column that contains the labels of the action the person demonstrates in the video file.
- `startTimeColumn`: The name of the column that contains the action’s starting-time in the video file.
- `endTimeColumn `: The name of the column that contains the action’s ending-time in the video file.

## See Also

- [MLActionClassifier.DataSource.labeledDirectories(at:)](mlactionclassifier/datasource/labeleddirectories(at:).md)
  The location of a folder with subfolders each of which contain sample videos of an action.
- [MLActionClassifier.DataSource.labeledFiles(at:)](mlactionclassifier/datasource/labeledfiles(at:).md)
  The location of a folder that contains video files whose names you use to label corresponding actions.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data table that contains the locations of the video files and the action annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/directorywithvideosandannotation(at:annotationfile:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:))*