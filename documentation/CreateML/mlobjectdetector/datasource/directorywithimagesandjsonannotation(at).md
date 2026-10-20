# MLObjectDetector.DataSource.directoryWithImagesAndJsonAnnotation(at:)

**Framework**: Create ML  
**Kind**: case  
**Role**: Case

An object-detector data source you create by selecting a directory that contains image files and exactly one JSON annotation file.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case directoryWithImagesAndJsonAnnotation(at: URL)
```

## Parameters

- `directoryWithImagesAndJsonAnnotation`: The location of a directory that contains exactly one JSON annotation file and all the image files the JSON file’s annotations refer to.

## See Also

### Creating a data source
- [MLObjectDetector.DataSource.directoryWithImages(at:annotationFile:)](./directorywithimages%28at,annotationfile%29.md)
  An object-detector data source you create by selecting the location of a directory of image files, and the location of a JSON annotation file.
- [case table(MLDataTable, imageColumn: String, annotationColumn: String)](./table%28_,imagecolumn,annotationcolumn%29.md)
  An object-detector data source you create with a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/directorywithimagesandjsonannotation(at:))*