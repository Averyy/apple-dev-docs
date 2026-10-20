# MLHandPoseClassifier.DataSource.labeledImageData(table:imageColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

Creates a data source from a data table that contains the hand joint locations and annotation for a set of image files.

**Availability**:
- iOS 15.0+ - Deprecated in 17.0
- iPadOS 15.0+ - Deprecated in 17.0
- Mac Catalyst 15.0+ - Deprecated in 17.0
- macOS 12.0+ - Deprecated in 14.0
- visionOS 1.0+

## Declaration

```swift
case labeledImageData(table: MLDataTable, imageColumn: String = __Defaults.imageColumnName, labelColumn: String = __Defaults.labelColumnName)
```

#### Discussion

- table: A data table that contains the locations of annotations for each hand pose image file.
- imageColumn: The name of the column in the data table that contains the image filenames.
- labelColumn: The name of the column in the data table that contains the hand pose label names.

## See Also

### Creating a data source
- [MLHandPoseClassifier.DataSource.labeledDirectories(at:)](./labeleddirectories%28at%29.md)
  Creates a data source from a folder with subfolders that each contain images of a hand pose.
- [MLHandPoseClassifier.DataSource.labeledFiles(at:)](./labeledfiles%28at%29.md)
  Creates a data source from a folder that contains images, each named after the hand pose it represents.
- [case directoryWithImagesAndAnnotation(at: URL, annotationFile: URL, imageColumn: String, labelColumn: String)](./directorywithimagesandannotation%28at,annotationfile,imagecolumn,labelcolumn%29.md)
  Creates a data source from a folder that contains images and an annotation file.
- [MLHandPoseClassifier.DataSource.labeledImageDataFrame(_:imageColumn:labelColumn:)](./labeledimagedataframe%28_,imagecolumn,labelcolumn%29.md)
  Creates a data source from a data frame that contains the location and annotation for a set of image files.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdataframe%28_,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  Creates a data source from a data frame of hand pose observations that each contain the locations of each hand joint and an annotation.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](./labeledkeypointsdata%28table,sessionidcolumn,labelcolumn,featurecolumn%29.md)
  Creates a data source from a data table of hand pose observations that each contain the locations of each hand joint and an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource/labeledimagedata(table:imagecolumn:labelcolumn:))*