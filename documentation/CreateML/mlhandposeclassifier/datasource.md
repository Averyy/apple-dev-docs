# MLHandPoseClassifier.DataSource

**Framework**: Create ML  
**Kind**: enum

A hand pose classifier dataset that contains annotated images or hand joint location data.

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
- [MLHandPoseClassifier.DataSource.labeledDirectories(at:)](mlhandposeclassifier/datasource/labeleddirectories(at:).md)
  Creates a data source from a folder with subfolders that each contain images of a hand pose.
- [MLHandPoseClassifier.DataSource.labeledFiles(at:)](mlhandposeclassifier/datasource/labeledfiles(at:).md)
  Creates a data source from a folder that contains images, each named after the hand pose it represents.
- [case directoryWithImagesAndAnnotation(at: URL, annotationFile: URL, imageColumn: String, labelColumn: String)](mlhandposeclassifier/datasource/directorywithimagesandannotation(at:annotationfile:imagecolumn:labelcolumn:).md)
  Creates a data source from a folder that contains images and an annotation file.
- [MLHandPoseClassifier.DataSource.labeledImageDataFrame(_:imageColumn:labelColumn:)](mlhandposeclassifier/datasource/labeledimagedataframe(_:imagecolumn:labelcolumn:).md)
  Creates a data source from a data frame that contains the location and annotation for a set of image files.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandposeclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data frame of hand pose observations that each contain the locations of each hand joint and an annotation.
- [case labeledImageData(table: MLDataTable, imageColumn: String, labelColumn: String)](mlhandposeclassifier/datasource/labeledimagedata(table:imagecolumn:labelcolumn:).md)
  Creates a data source from a data table that contains the hand joint locations and annotation for a set of image files.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandposeclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data table of hand pose observations that each contain the locations of each hand joint and an annotation.
### Extracting keypoints
- [func extractKeypoints() throws -> DataFrame](mlhandposeclassifier/datasource/extractkeypoints.md)
  Extracts key points from video files if necessary.
### Getting annotated file names
- [func gatherAnnotatedFileNames() throws -> DataFrame?](mlhandposeclassifier/datasource/gatherannotatedfilenames.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.
### Exporting a data source
- [func labeledMedia() throws -> [String : [URL]]](mlhandposeclassifier/datasource/labeledmedia.md)
  Generates a dictionary that contains the data source’s classification labels paired with an array of URLs to the label’s image files.
- [func imagesWithAnnotations() throws -> MLDataTable](mlhandposeclassifier/datasource/imageswithannotations.md)
  Generates a data table that contains a column for the data source’s image file URLs and a column of annotations.
- [func keypointsWithAnnotations() throws -> MLDataTable](mlhandposeclassifier/datasource/keypointswithannotations.md)
  Generates a data table that contains a column for hand joint locations and hand pose annotations.
- [func stratifiedSplit(proportions: [Double], seed: Int, labelColumn: String) throws -> MLDataTable](mlhandposeclassifier/datasource/stratifiedsplit(proportions:seed:labelcolumn:).md)
  Generates a data table by splitting the data source into strata.

## See Also

- [MLHandPoseClassifier.ModelParameters](mlhandposeclassifier/modelparameters-swift.struct.md)
  A set of parameters that affect the training process of a hand pose classifier task.
- [MLHandPoseClassifier.ImageAugmentationOptions](mlhandposeclassifier/imageaugmentationoptions.md)
  Options a hand pose classification training session can use to generate additional training data from the images you provide.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource)*