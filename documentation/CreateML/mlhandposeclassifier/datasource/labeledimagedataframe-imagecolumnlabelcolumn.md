# MLHandPoseClassifier.DataSource.labeledImageDataFrame(_:imageColumn:labelColumn:)

**Framework**: Create ML  
**Kind**: case

Creates a data source from a data frame that contains the location and annotation for a set of image files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case labeledImageDataFrame(DataFrame, imageColumn: String = __Defaults.imageColumnName, labelColumn: String = __Defaults.labelColumnName)
```

#### Discussion

- dataFrame: A data frame that contains the locations of annotations for each hand pose image file.
- imageColumn: The name of the column in the data frame that contains the image filenames.
- labelColumn: The name of the column in the data frame that contains the hand pose label names.

## See Also

- [MLHandPoseClassifier.DataSource.labeledDirectories(at:)](mlhandposeclassifier/datasource/labeleddirectories(at:).md)
  Creates a data source from a folder with subfolders that each contain images of a hand pose.
- [MLHandPoseClassifier.DataSource.labeledFiles(at:)](mlhandposeclassifier/datasource/labeledfiles(at:).md)
  Creates a data source from a folder that contains images, each named after the hand pose it represents.
- [case directoryWithImagesAndAnnotation(at: URL, annotationFile: URL, imageColumn: String, labelColumn: String)](mlhandposeclassifier/datasource/directorywithimagesandannotation(at:annotationfile:imagecolumn:labelcolumn:).md)
  Creates a data source from a folder that contains images and an annotation file.
- [case labeledKeypointsDataFrame(DataFrame, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandposeclassifier/datasource/labeledkeypointsdataframe(_:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data frame of hand pose observations that each contain the locations of each hand joint and an annotation.
- [case labeledImageData(table: MLDataTable, imageColumn: String, labelColumn: String)](mlhandposeclassifier/datasource/labeledimagedata(table:imagecolumn:labelcolumn:).md)
  Creates a data source from a data table that contains the hand joint locations and annotation for a set of image files.
- [case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String, labelColumn: String, featureColumn: String)](mlhandposeclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:).md)
  Creates a data source from a data table of hand pose observations that each contain the locations of each hand joint and an annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource/labeledimagedataframe(_:imagecolumn:labelcolumn:))*