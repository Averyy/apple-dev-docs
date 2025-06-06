# MLActionClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum

A data source for an action classifier.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum DataSource
```

## Mentions

- [Building an Action Classifier Data Source](building-an-action-classifier-data-source.md)

## Topics

### Creating a data source
- [MLActionClassifier.DataSource.labeledDirectories(at:)](mlactionclassifier/datasource/labeleddirectories(at:).md)
  The location of a folder with subfolders each of which contain sample videos of an action.
- [MLActionClassifier.DataSource.labeledFiles(at:)](mlactionclassifier/datasource/labeledfiles(at:).md)
  The location of a folder that contains video files whose names you use to label corresponding actions.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/directorywithvideosandannotation(at:annotationfile:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  The location of a directory of video files, and the location of an action annotation file.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodata(table:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data table that contains the locations of the video files and the action annotations.
### Extracting key points
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](mlactionclassifier/datasource/extractkeypoints(targetframerate:).md)
  Extracts key points from video files if necessary.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlactionclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
  A data source made up of keypoints in a data frame.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlactionclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  A data table that contains the human body landmark movement data.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](mlactionclassifier/datasource/labeledvideodataframe(_:videocolumn:labelcolumn:starttimecolumn:endtimecolumn:).md)
  A data source made up of video references in a data frame.
### Getting annotated file names
- [func gatherAnnotatedFileNames() throws -> DataFrame?](mlactionclassifier/datasource/gatherannotatedfilenames.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.
### Generating data tables from a data source
- [func videosWithAnnotations() throws -> MLDataTable](mlactionclassifier/datasource/videoswithannotations.md)
  Generates a data table of the data source’s video URL locations and action annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](mlactionclassifier/datasource/keypointswithannotations(targetframerate:).md)
  Generates a data table with action annotations of the data source.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](mlactionclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:).md)
  Generates a data table by splitting the data source into strata.

## See Also

- [MLActionClassifier.ModelParameters](mlactionclassifier/modelparameters-swift.struct.md)
  Parameters that affect the training process of an action classifier.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource)*