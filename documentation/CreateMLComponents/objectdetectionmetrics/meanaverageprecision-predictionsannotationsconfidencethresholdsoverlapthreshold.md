# meanAveragePrecision(predictions:annotations:confidenceThresholds:overlapThreshold:)

**Framework**: Create ML Components  
**Kind**: method

Calculates the mean average precision at the bounding box overlap threshold.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func meanAveragePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float] = [:], overlapThreshold: Double = 0.5) -> Scalar where Scalar : BinaryFloatingPoint
```

#### Return Value

The mean average precision at the overlap threshold.

## Parameters

- `predictions`: A list of all the predictions from an object detection model. Each element in the list is a list of predictions from one image.
- `annotations`: A list of all the annotations. Each element is an   object from one image.
- `confidenceThresholds`: Confidence thresholds for each label. The values will always be between 0.0 and 1.0.   If any label does not have a threshold, the   is used for that label. The default value is  .
- `overlapThreshold`: The overlap threshold for the bounding boxes. The value will always be between 0.0 and 1.0. The default value is  .

## See Also

- [func averageOfAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float]) -> [Label : Scalar]](objectdetectionmetrics/averageofaverageprecisionatvariedthresholds(predictions:annotations:confidencethresholds:).md)
  Calculates average of average precision for all the labels, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.
- [func averageOfMeanAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float]) -> Scalar](objectdetectionmetrics/averageofmeanaverageprecisionatvariedthresholds(predictions:annotations:confidencethresholds:).md)
  Calculates the average of mean average precision, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.
- [func averagePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float], overlapThreshold: Double) -> [Label : Scalar]](objectdetectionmetrics/averageprecision(predictions:annotations:confidencethresholds:overlapthreshold:).md)
  Calculates average precision for all the labels at the bounding box overlap threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionmetrics/meanaverageprecision(predictions:annotations:confidencethresholds:overlapthreshold:))*