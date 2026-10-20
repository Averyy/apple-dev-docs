# MLActionClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum  
**Role**: Enumeration

A data source for an action classifier.

**Availability**:
- macOS 11.0+

## Declaration

```swift
enum DataSource
```

## Mentions

- [Building an Action Classifier Data Source](../building-an-action-classifier-data-source.md)

## Topics

### Creating a data source
- [MLActionClassifier.DataSource.labeledDirectories(at:)](./datasource/labeleddirectories%28at%29.md)
  The location of a folder with subfolders each of which contain sample videos of an action.
- [MLActionClassifier.DataSource.labeledFiles(at:)](./datasource/labeledfiles%28at%29.md)
  The location of a folder that contains video files whose names you use to label corresponding actions.
- [case directoryWithVideosAndAnnotation(at: URL, annotationFile: URL, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](./datasource/directorywithvideosandannotation%28at,annotationfile,videocolumn,labelcolumn,starttimecolumn,endtimecolumn%29.md)
  The location of a directory of video files, and the location of an action annotation file.
- [case labeledVideoData(table: MLDataTable, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](./datasource/labeledvideodata%28table,videocolumn,labelcolumn,starttimecolumn,endtimecolumn%29.md)
  A data table that contains the locations of the video files and the action annotations.
### Extracting key points
- [func extractKeypoints(targetFrameRate: Double) throws -> DataFrame](./datasource/extractkeypoints%28targetframerate%29.md)
  Extracts key points from video files if necessary.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./datasource/labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  A data source made up of keypoints in a data frame.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./datasource/labeledkeypointsdata%28table,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  A data table that contains the human body landmark movement data.
- [case labeledVideoDataFrame(DataFrame, videoColumn: String, labelColumn: String, startTimeColumn: String?, endTimeColumn: String?)](./datasource/labeledvideodataframe%28_,videocolumn,labelcolumn,starttimecolumn,endtimecolumn%29.md)
  A data source made up of video references in a data frame.
### Getting annotated file names
- [func gatherAnnotatedFileNames() throws -> DataFrame?](./datasource/gatherannotatedfilenames%28%29.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.
### Generating data tables from a data source
- [func videosWithAnnotations() throws -> MLDataTable](./datasource/videoswithannotations%28%29.md)
  Generates a data table of the data source’s video URL locations and action annotations.
- [func keypointsWithAnnotations(targetFrameRate: Double) throws -> MLDataTable](./datasource/keypointswithannotations%28targetframerate%29.md)
  Generates a data table with action annotations of the data source.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](./datasource/stratifiedsplit%28proportions,seed,labelcolumn%29.md)
  Generates a data table by splitting the data source into strata.

## See Also

### Supporting types
- [MLActionClassifier.ModelParameters](./modelparameters-swift.struct.md)
  Parameters that affect the training process of an action classifier.
- [MLActionClassifier.VideoAugmentationOptions](./videoaugmentationoptions.md)
  The video augmentations for an action classifier training session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/datasource)*