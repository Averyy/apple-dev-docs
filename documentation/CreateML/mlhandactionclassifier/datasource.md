# MLHandActionClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum

A hand action classifier dataset that contains annotated videos or hand joint location data.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
enum DataSource
```

## Topics

### Creating a data source
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
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data frame of hand action observations that each contain the locations of each hand joint and an annotation.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data table of hand action observations that each contain the locations of each hand joint and an annotation.
### Exporting a data source
- [func labeledMedia() throws -> [String : [URL]]](mlhandactionclassifier/datasource/labeledmedia.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s video files.
- [func videosWithAnnotations() throws -> MLDataTable](mlhandactionclassifier/datasource/videoswithannotations.md)
  Generates a data table that contains a column for the data source’s video file URLs and a column of annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](mlhandactionclassifier/datasource/keypointswithannotations(targetframerate:).md)
  Generates a data table that contains a column for hand joint locations and a column of hand action annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](mlhandactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:).md)
  Generates a data table by splitting the data source into strata.
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](mlhandactionclassifier/datasource/extractkeypoints(targetframerate:).md)
  Extracts key points from video files if necessary.
- [func gatherAnnotatedFileNames() throws -> DataFrame?](mlhandactionclassifier/datasource/gatherannotatedfilenames.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.

## See Also

- [MLHandActionClassifier.ModelParameters](mlhandactionclassifier/modelparameters-swift.struct.md)
  A set of parameters that affect the training process of a hand action classifier task.
- [MLHandActionClassifier.VideoAugmentationOptions](mlhandactionclassifier/videoaugmentationoptions.md)
  Options a hand action classification training session can use to generate additional training data from the videos you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/datasource)*