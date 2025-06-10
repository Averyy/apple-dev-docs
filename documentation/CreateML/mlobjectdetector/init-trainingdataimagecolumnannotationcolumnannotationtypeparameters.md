# init(trainingData:imageColumn:annotationColumn:annotationType:parameters:)

**Framework**: Create ML  
**Kind**: init

Creates an object detector with a data table.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(trainingData: MLDataTable, imageColumn: String, annotationColumn: String, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters = ModelParameters()) throws
```

#### Discussion

Use this initializer to create an object detector with an [`MLDataTable`](mldatatable.md).

## Parameters

- `trainingData`: An   that contains the annotated images the task uses to train the object   detector.
- `imageColumn`: The name of the column in the data table that contains the image file URLs.
- `annotationColumn`: The name of the column in the data table that contains the image annotations.
- `parameters`: An   instance you use to set the model   configuration settings for the training session.

## See Also

- [init(trainingData: MLObjectDetector.DataSource, parameters: MLObjectDetector.ModelParameters, annotationType: MLObjectDetector.AnnotationType) throws](mlobjectdetector/init(trainingdata:parameters:annotationtype:).md)
  Creates an object detector with a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/init(trainingdata:imagecolumn:annotationcolumn:annotationtype:parameters:))*