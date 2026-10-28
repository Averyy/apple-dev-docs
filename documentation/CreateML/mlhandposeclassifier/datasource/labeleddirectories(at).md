# MLHandPoseClassifier.DataSource.labeledDirectories(at:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Creates a data source from a folder with subfolders that each contain images of a hand pose.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case labeledDirectories(at: URL)
```

## Discussion

- at: The URL to a folder in the file system that contains folders of hand pose images. The data source uses the name of each folder as the classification label for the hand pose images it contains.

## See Also

### Creating a data source
- [MLHandPoseClassifier.DataSource.labeledFiles(at:)](./labeledfiles%28at%29.md)
  Creates a data source from a folder that contains images, each named after the hand pose it represents.
- [case directoryWithImagesAndAnnotation(at: URL, annotationFile: URL, imageColumn: String, labelColumn: String)](./directorywithimagesandannotation%28at,annotationfile,imagecolumn,labelcolumn%29.md)
  Creates a data source from a folder that contains images and an annotation file.
- [MLHandPoseClassifier.DataSource.labeledImageDataFrame(_:imageColumn:labelColumn:)](./labeledimagedataframe%28_,imagecolumn,labelcolumn%29.md)
  Creates a data source from a data frame that contains the location and annotation for a set of image files.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  Creates a data source from a data frame of hand pose observations that each contain the locations of each hand joint and an annotation.
- [case labeledImageData(table: MLDataTable, imageColumn: String, labelColumn: String)](./labeledimagedata%28table,imagecolumn,labelcolumn%29.md)
  Creates a data source from a data table that contains the hand joint locations and annotation for a set of image files.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdata%28table,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  Creates a data source from a data table of hand pose observations that each contain the locations of each hand joint and an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource/labeleddirectories(at:))*