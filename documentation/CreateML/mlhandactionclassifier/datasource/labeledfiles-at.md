# MLHandActionClassifier.DataSource.labeledFiles(at:)

**Framework**: Create ML  
**Kind**: case

Creates a data source from a folder that contains videos, each named after the hand action they represent.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case labeledFiles(at: URL)
```

#### Discussion

Create a hand action data source from a directory of videos with the `labeledFiles` case. You must name each video file with a hand action label, followed by a period and an arbitrary string, ending with the video file’s extension. For example, you can name a hand action classifier’s training files `Wave.3.mov`, `MoveCloser.1.mov`, `MoveCloser.2.mov`, and so on.

In this example, a hand action classifier would have at least two class labels:

- `Wave`
- `MoveCloser`

## Parameters

- `at`: The URL to a folder in the file system that contains folders of hand action videos. The data source   uses each file’s name before the first period as its classification label.

## See Also

- [MLHandActionClassifier.DataSource.labeledDirectories(at:)](mlhandactionclassifier/datasource/labeleddirectories(at:).md)
  Creates a data source from a folder with subfolders that each contain videos of a hand action.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlhandactionclassifier/datasource/directorywithvideosandannotation(at:annotationfile:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  Creates a data source from a folder that contains videos and an annotation file.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlhandactionclassifier/datasource/labeledvideodataframe(_:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  Creates a data source from a data frame that contains the location and annotation for a set of video files.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlhandactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  Creates a data source from a data table that contains the location and annotation for a set of video files.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data frame of hand action observations that each contain the locations of each hand joint and an annotation.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data table of hand action observations that each contain the locations of each hand joint and an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource/labeledfiles(at:))*