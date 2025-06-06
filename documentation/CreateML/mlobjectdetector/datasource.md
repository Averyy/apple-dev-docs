# MLObjectDetector.DataSource

**Framework**: Create ML  
**Kind**: enum

A data source for an object detector.

**Availability**:
- macOS 10.15+

## Declaration

```swift
enum DataSource
```

#### Overview

You use a data source to specify the training dataset for an [`MLObjectDetector`](mlobjectdetector.md) training session. An object-detector data source represents a set of images and an annotation for each object in an image.

Each object annotation consists of the object’s name, or , and its location in the image. A single image can have multiple objects and, therefore, multiple annotations. For example, you can train an object detector with images of dining tables, along with annotations for bananas, croissants, and beverages. Each image can have one or more instances of an object, or any combination of objects.

## Topics

### Creating a data source
- [MLObjectDetector.DataSource.directoryWithImagesAndJsonAnnotation(at:)](mlobjectdetector/datasource/directorywithimagesandjsonannotation(at:).md)
  An object-detector data source you create by selecting a directory that contains image files and exactly one JSON annotation file.
- [MLObjectDetector.DataSource.directoryWithImages(at:annotationFile:)](mlobjectdetector/datasource/directorywithimages(at:annotationfile:).md)
  An object-detector data source you create by selecting the location of a directory of image files, and the location of a JSON annotation file.
- [case table(MLDataTable, imageColumn: String, annotationColumn: String)](mlobjectdetector/datasource/table(_:imagecolumn:annotationcolumn:).md)
  An object-detector data source you create with a data table.
### Getting the annotated file names
- [func gatherAnnotatedFileNames() throws -> DataFrame](mlobjectdetector/datasource/gatherannotatedfilenames.md)
  Processes the data source and returns a data frame that contains file URLs and annotations.
### Getting the data frame
- [case frame(DataFrame, imageColumn: String, annotationColumn: String)](mlobjectdetector/datasource/frame(_:imagecolumn:annotationcolumn:).md)
  Data specified by a `DataFrame` containing a column for image file paths and a column with annotations.
### Retrieving the data
- [func imagesWithObjectAnnotations() throws -> MLDataTable](mlobjectdetector/datasource/imageswithobjectannotations.md)
  Generates a data table where each row represents an image, and its columns are the image file URLs and its annotations.
### Splitting the data
- [func stratifiedSplit(proportions: [Double], seed: Int, annotationColumn: String) throws -> MLDataTable](mlobjectdetector/datasource/stratifiedsplit(proportions:seed:annotationcolumn:).md)
  Generates a new data table by splitting the data source using the specified proportions.

## See Also

- [MLObjectDetector.AnnotationType](mlobjectdetector/annotationtype.md)
  The available types of image annotations.
- [MLObjectDetector.ModelParameters](mlobjectdetector/modelparameters-swift.struct.md)
  Parameters that affect the process of training an object detection model.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/datasource)*