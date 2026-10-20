# MLObjectDetector.DataSource.directoryWithImages(at:annotationFile:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

An object-detector data source you create by selecting the location of a directory of image files, and the location of a JSON annotation file.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case directoryWithImages(at: URL, annotationFile: URL)
```

## Parameters

- `directoryWithImages`: The location of a directory that contains image files.
- `annotationFile`: The location of a JSON file with object annotations for the images.

## See Also

### Creating a data source
- [MLObjectDetector.DataSource.directoryWithImagesAndJsonAnnotation(at:)](./directorywithimagesandjsonannotation%28at%29.md)
  An object-detector data source you create by selecting a directory that contains image files and exactly one JSON annotation file.
- [case table(MLDataTable, imageColumn: String, annotationColumn: String)](./table%28_,imagecolumn,annotationcolumn%29.md)
  An object-detector data source you create with a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/directorywithimages(at:annotationfile:))*