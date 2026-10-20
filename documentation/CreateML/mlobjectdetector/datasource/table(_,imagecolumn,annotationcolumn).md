# MLObjectDetector.DataSource.table(_:imageColumn:annotationColumn:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

An object-detector data source you create with a data table.

**Availability**:
- macOS 11.0+ - Deprecated in 14.0

## Declaration

```swift
case table(MLDataTable, imageColumn: String, annotationColumn: String)
```

## Parameters

- `table`: An [`MLDataTable`](../../mldatatable.md) instance that contains a column of image file locations and a column of object annotations.
- `imageColumn`: The name of the column in the data table that contains the URL for an image.
- `annotationColumn`: The name of the column in the data table that contains the object annotations for an image.

## See Also

### Creating a data source
- [MLObjectDetector.DataSource.directoryWithImagesAndJsonAnnotation(at:)](./directorywithimagesandjsonannotation%28at%29.md)
  An object-detector data source you create by selecting a directory that contains image files and exactly one JSON annotation file.
- [MLObjectDetector.DataSource.directoryWithImages(at:annotationFile:)](./directorywithimages%28at,annotationfile%29.md)
  An object-detector data source you create by selecting the location of a directory of image files, and the location of a JSON annotation file.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/table(_:imagecolumn:annotationcolumn:))*