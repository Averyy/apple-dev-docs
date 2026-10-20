# validationMetrics

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Measurements of the object detector’s performance on the validation dataset.

**Availability**:
- macOS 10.15+

## Declaration

```swift
var validationMetrics: MLObjectDetectorMetrics { get }
```

## See Also

### Evaluating an object detector
- [func evaluation(on: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics](./evaluation%28on%29.md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data source.
- [func evaluation(on: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics](./evaluation%28on,imagecolumn,annotationcolumn%29.md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data table.
- [var trainingMetrics: MLObjectDetectorMetrics](./trainingmetrics.md)
  Measurements of the object detector’s performance on the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/validationmetrics)*