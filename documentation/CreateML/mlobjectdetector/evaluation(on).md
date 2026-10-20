# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates metrics by evaluating the object detector’s performance using annotated images in a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func evaluation(on annotatedImages: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics
```

#### Return Value

An [`MLObjectDetectorMetrics`](../mlobjectdetectormetrics.md) instance that represents the object detector’s performance on the annotated images.

## Parameters

- `annotatedImages`: An [`MLObjectDetector.DataSource`](./datasource.md) instance that contains a set of images with object annotations.

## See Also

### Evaluating an object detector
- [func evaluation(on: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics](./evaluation%28on,imagecolumn,annotationcolumn%29.md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data table.
- [var trainingMetrics: MLObjectDetectorMetrics](./trainingmetrics.md)
  Measurements of the object detector’s performance on the training dataset.
- [var validationMetrics: MLObjectDetectorMetrics](./validationmetrics.md)
  Measurements of the object detector’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/evaluation(on:))*