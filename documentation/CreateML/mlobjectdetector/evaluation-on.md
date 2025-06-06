# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics by evaluating the object detector’s performance using annotated images in a data source.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func evaluation(on annotatedImages: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics
```

#### Return Value

An [`MLObjectDetectorMetrics`](mlobjectdetectormetrics.md) instance that represents the object detector’s performance on the annotated images.

## Parameters

- `annotatedImages`: An   instance that   contains a set of images with object annotations.

## See Also

- [func evaluation(on: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics](mlobjectdetector/evaluation(on:imagecolumn:annotationcolumn:).md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/evaluation(on:))*