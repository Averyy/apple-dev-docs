# MLHandPoseClassifier.DataSource.labeledKeypointsData(table:sessionIdColumn:labelColumn:featureColumn:)

**Framework**: Create ML  
**Kind**: case

Creates a data source from a data table of hand pose observations that each contain the locations of each hand joint and an annotation.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
case labeledKeypointsData(table: MLDataTable, sessionIdColumn: String = __Defaults.sessionIdColumnName, labelColumn: String = __Defaults.labelColumnName, featureColumn: String = __Defaults.featureColumnName)
```

#### Discussion

- table : A data table that contains the hand-joint locations and annotations for a set of hand poses.
- sessionIdColumn: The name of the column in the data table that contains the session identifiers.
- labelColumn: The name of the column in the data table that contains the hand pose label names.
- featureColumn: The name of the column in the data table that contains the hand-joint location data. Each entry in the column must be an [`MLMultiArray`](https://developer.apple.com/documentation/CoreML/MLMultiArray) instance — which you must wrap in an [`MLDataValue.MultiArrayType`](mldatavalue/multiarraytype.md) — that contains three dimensions: - The first dimension has a size of one.
- The second dimension has three channels: the x-coordinate, the y-coordinate, and the confidence value, respectively. - The third dimension has 21 channels, one for each hand joint.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/datasource/labeledkeypointsdata(table:sessionidcolumn:labelcolumn:featurecolumn:))*