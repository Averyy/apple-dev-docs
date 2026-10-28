# init(trainingData:parameters:annotationType:)

**Framework**: Create ML  
**Kind**: init  
**Role**: Initializer

Creates an object detector with a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
init(trainingData: MLObjectDetector.DataSource, parameters: MLObjectDetector.ModelParameters = .init(), annotationType: MLObjectDetector.AnnotationType) throws
```

## Discussion

Use this initializer to create an object detector with an [`MLObjectDetector.DataSource`](./datasource.md).

## Parameters

- `trainingData`: A data source that contains the annotated images the task uses to train the object detector.
- `parameters`: An [`MLObjectDetector.ModelParameters`](./modelparameters-swift.struct.md) instance you use to set the model configuration settings for the training session.
- `annotationType`: The format your data source uses for its image annotations.

## See Also

### Training an object detector synchronously
- [init(trainingData: MLDataTable, imageColumn: String, annotationColumn: String, annotationType: MLObjectDetector.AnnotationType, parameters: MLObjectDetector.ModelParameters) throws](./init%28trainingdata,imagecolumn,annotationcolumn,annotationtype,parameters%29.md)
  Creates an object detector with a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/init(trainingdata:parameters:annotationtype:))*