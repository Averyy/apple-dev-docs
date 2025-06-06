# evaluation(on:imageColumn:annotationColumn:)

**Framework**: Create ML  
**Kind**: method

Generates metrics by evaluating the object detector’s performance using annotated images in a data table.

**Availability**:
- macOS 10.15+

## Declaration

```swift
func evaluation(on annotatedImages: MLDataTable, imageColumn: String, annotationColumn: String) -> MLObjectDetectorMetrics
```

#### Return Value

An [`MLObjectDetectorMetrics`](mlobjectdetectormetrics.md) instance that represents the object detector’s performance on the annotated images.

## Parameters

- `annotatedImages`: An   instance that contains a set of   images with object annotations.
- `imageColumn`: The name of the column in the data table that contains   the image file URLs.
- `annotationColumn`: The name of the column in the data table that   contains the object annotations.

## See Also

- [func evaluation(on: MLObjectDetector.DataSource) -> MLObjectDetectorMetrics](mlobjectdetector/evaluation(on:).md)
  Generates metrics by evaluating the object detector’s performance using annotated images in a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlobjectdetector/evaluation(on:imagecolumn:annotationcolumn:))*