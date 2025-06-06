# init(trainingData:parameters:annotationType:)

**Framework**: Create ML  
**Kind**: init

Creates an object detector with a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(trainingData: MLObjectDetector.DataSource, parameters: MLObjectDetector.ModelParameters = .init(), annotationType: MLObjectDetector.AnnotationType) throws
```

#### Discussion

Use this initializer to create an object detector with an [`MLObjectDetector.DataSource`](mlobjectdetector/datasource.md).

- trainingData: A data source that contains the annotated images the task uses to train the object detector.
- annotationType : The format your data source uses for its image annotations.

## See Also

- [init(trainingData: MLDataTable, imageColumn: String, annotationColumn: String, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters) throws](mlobjectdetector/init(trainingdata:imagecolumn:annotationcolumn:annotationtype:parameters:).md)
  Creates an object detector with a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/init(trainingdata:parameters:annotationtype:))*