# evaluation(on:imageColumn:annotationColumn:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates metrics by evaluating the object detector’s performance using annotated images in a data table.

**Availability**:
- macOS 10.15+ - Deprecated in 13.0

> **Deprecated**: Use DataSource instead of MLDataTable.

## Declaration

```swift
func evaluation(on annotatedImages: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics
```

#### Return Value

An [`MLObjectDetectorMetrics`](../mlobjectdetectormetrics.md) instance that represents the object detector’s performance on the annotated images.

## Parameters

- `annotatedImages`: An [`MLDataTable`](../mldatatable.md) instance that contains a set of images with object annotations.
- `imageColumn`: The name of the column in the data table that contains the image file URLs.
- `annotationColumn`: The name of the column in the data table that contains the object annotations.

## See Also

### Evaluating an object detector
- [func evaluation(on: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics](./evaluation%28on%29.md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data source.
- [var trainingMetrics: MLObjectDetectorMetrics](./trainingmetrics.md)
  Measurements of the object detector’s performance on the training dataset.
- [var validationMetrics: MLObjectDetectorMetrics](./validationmetrics.md)
  Measurements of the object detector’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/evaluation(on:imagecolumn:annotationcolumn:))*