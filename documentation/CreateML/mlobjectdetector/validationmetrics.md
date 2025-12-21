# validationMetrics

**Framework**: Create ML  
**Kind**: property

Measurements of the object detector’s performance on the validation dataset.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var validationMetrics: MLObjectDetectorMetrics { get }
```

## See Also

- [func evaluation(on: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics](mlobjectdetector/evaluation(on:).md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data source.
- [func evaluation(on: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics](mlobjectdetector/evaluation(on:imagecolumn:annotationcolumn:).md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data table.
- [var trainingMetrics: MLObjectDetectorMetrics](mlobjectdetector/trainingmetrics.md)
  Measurements of the object detector’s performance on the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/validationmetrics)*