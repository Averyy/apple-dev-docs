# MLActionClassifier.DataSource.labeledDirectories(at:)

**Framework**: Create ML  
**Kind**: case

The location of a folder with subfolders each of which contain sample videos of an action.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case labeledDirectories(at: URL)
```

#### Discussion

The action classifier task uses each subfolder’s name as the label for an action.

## See Also

- [MLActionClassifier.DataSource.labeledFiles(at:)](mlactionclassifier/datasource/labeledfiles(at:).md)
  The location of a folder that contains video files whose names you use to label corresponding actions.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/directorywithvideosandannotation(at:annotationfile:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  The location of a directory of video files, and the location of an action annotation file.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data table that contains the locations of the video files and the action annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/labeleddirectories(at:))*