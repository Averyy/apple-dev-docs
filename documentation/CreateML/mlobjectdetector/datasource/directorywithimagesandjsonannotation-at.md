# MLObjectDetector.DataSource.directoryWithImagesAndJsonAnnotation(at:)

**Framework**: Create ML  
**Kind**: case

An object-detector data source you create by selecting a directory that contains image files and exactly one JSON annotation file.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case directoryWithImagesAndJsonAnnotation(at: URL)
```

## Parameters

- `directoryWithImagesAndJsonAnnotation`: The location of a directory that contains exactly one JSON   annotation file and all the image files the JSON file’s annotations refer to.

## See Also

- [MLObjectDetector.DataSource.directoryWithImages(at:annotationFile:)](mlobjectdetector/datasource/directorywithimages(at:annotationfile:).md)
  An object-detector data source you create by selecting the location of a directory of image files, and the location of a JSON annotation file.
- [case table(MLDataTable, imageColumn: String, annotationColumn: String)](mlobjectdetector/datasource/table(_:imagecolumn:annotationcolumn:).md)
  An object-detector data source you create with a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/directorywithimagesandjsonannotation(at:))*