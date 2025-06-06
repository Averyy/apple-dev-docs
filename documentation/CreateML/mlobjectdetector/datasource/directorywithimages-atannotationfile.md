# MLObjectDetector.DataSource.directoryWithImages(at:annotationFile:)

**Framework**: Create ML  
**Kind**: case

An object-detector data source you create by selecting the location of a directory of image files, and the location of a JSON annotation file.

**Availability**:
- macOS 10.15+

## Declaration

```swift
case directoryWithImages(at: URL, annotationFile: URL)
```

#### Discussion

- directoryWithImages: The location of a directory that contains image files.
- annotationFile: The location of a JSON file with object annotations for the images.

## See Also

- [MLObjectDetector.DataSource.directoryWithImagesAndJsonAnnotation(at:)](mlobjectdetector/datasource/directorywithimagesandjsonannotation(at:).md)
  An object-detector data source you create by selecting a directory that contains image files and exactly one JSON annotation file.
- [case table(MLDataTable, imageColumn: String, annotationColumn: String)](mlobjectdetector/datasource/table(_:imagecolumn:annotationcolumn:).md)
  An object-detector data source you create with a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource/directorywithimages(at:annotationfile:))*