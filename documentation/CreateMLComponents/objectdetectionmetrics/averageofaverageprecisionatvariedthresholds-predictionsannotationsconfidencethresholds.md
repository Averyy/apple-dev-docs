# averageOfAveragePrecisionAtVariedThresholds(predictions:annotations:confidenceThresholds:)

**Framework**: Create ML Components  
**Kind**: method

Calculates average of average precision for all the labels, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
func averageOfAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float] = [:]) -> [Label : Scalar] where Scalar : BinaryFloatingPoint
```

#### Return Value

Average of average precision for all the labels, computed at varied bounding box overlap thresholds.

## Parameters

- `predictions`: A list of all the predictions from an object detection model. Each element in the list is a list of predictions from one image.
- `annotations`: A list of all the annotations. Each element is an   object from one image.
- `confidenceThresholds`: Confidence thresholds for each label. The values will always be between 0.0 and 1.0.   If any label does not have a threshold, the   is used for that label. The default value is  .

## See Also

- [func averageOfMeanAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float]) -> Scalar](objectdetectionmetrics/averageofmeanaverageprecisionatvariedthresholds(predictions:annotations:confidencethresholds:).md)
  Calculates the average of mean average precision, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.
- [func averagePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float], overlapThreshold: Double) -> [Label : Scalar]](objectdetectionmetrics/averageprecision(predictions:annotations:confidencethresholds:overlapthreshold:).md)
  Calculates average precision for all the labels at the bounding box overlap threshold.
- [func meanAveragePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float], overlapThreshold: Double) -> Scalar](objectdetectionmetrics/meanaverageprecision(predictions:annotations:confidencethresholds:overlapthreshold:).md)
  Calculates the mean average precision at the bounding box overlap threshold.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionmetrics/averageofaverageprecisionatvariedthresholds(predictions:annotations:confidencethresholds:))*