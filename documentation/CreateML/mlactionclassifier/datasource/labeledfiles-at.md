# MLActionClassifier.DataSource.labeledFiles(at:)

**Framework**: Create ML  
**Kind**: case

The location of a folder that contains video files whose names you use to label corresponding actions.

**Availability**:
- macOS 11.0+

## Declaration

```swift
case labeledFiles(at: URL)
```

#### Discussion

Use this case to create a data source from a folder of all your sample video files. Name each file using the action’s label, followed by a period and an arbitrary string, followed by the file extension. For example, an exercise action classifier might have files named squat.3.mov, lunge.1.mov, lunge.2.mov, and so on.

## See Also

- [MLActionClassifier.DataSource.labeledDirectories(at:)](mlactionclassifier/datasource/labeleddirectories(at:).md)
  The location of a folder with subfolders each of which contain sample videos of an action.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/directorywithvideosandannotation(at:annotationfile:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  The location of a directory of video files, and the location of an action annotation file.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data table that contains the locations of the video files and the action annotations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource/labeledfiles(at:))*