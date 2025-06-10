# ObjectDetectionMetrics

**Framework**: Create ML Components  
**Kind**: struct

Metrics for object detection model.

**Availability**:
- iOS 17.0+
- iPadOS 17.0+
- Mac Catalyst 17.0+
- macOS 14.0+
- tvOS 17.0+
- visionOS 1.0+

## Declaration

```swift
struct ObjectDetectionMetrics<Label> where Label : Comparable, Label : Decodable, Label : Encodable, Label : Hashable
```

## Topics

### Creating a metrics object
- [init()](objectdetectionmetrics/init.md)
### Getting the properties Properties
- [var defaultConfidenceThreshold: Float](objectdetectionmetrics/defaultconfidencethreshold.md)
  The default confidence threshold. It is used as the confidence threshold for any label which does not have an explicit confidence threshold, while calculating averagePrecision and meanAveragePrecision.
- [var labels: Set<Label>](objectdetectionmetrics/labels.md)
  A set of labels present in the dataset.
### Calculating the precision
- [func averageOfAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float]) -> [Label : Scalar]](objectdetectionmetrics/averageofaverageprecisionatvariedthresholds(predictions:annotations:confidencethresholds:).md)
  Calculates average of average precision for all the labels, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.
- [func averageOfMeanAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float]) -> Scalar](objectdetectionmetrics/averageofmeanaverageprecisionatvariedthresholds(predictions:annotations:confidencethresholds:).md)
  Calculates the average of mean average precision, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.
- [func averagePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float], overlapThreshold: Double) -> [Label : Scalar]](objectdetectionmetrics/averageprecision(predictions:annotations:confidencethresholds:overlapthreshold:).md)
  Calculates average precision for all the labels at the bounding box overlap threshold.
- [func meanAveragePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float], overlapThreshold: Double) -> Scalar](objectdetectionmetrics/meanaverageprecision(predictions:annotations:confidencethresholds:overlapthreshold:).md)
  Calculates the mean average precision at the bounding box overlap threshold.
### Extracting labels
- [static func extractLabels(from: [ObjectDetectionAnnotation<Label>]) -> Set<Label>](objectdetectionmetrics/extractlabels(from:).md)
  Extracts all the labels from a list of annotations.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [struct DetectedObject](detectedobject.md)
  An item in a detection result.
- [struct ObjectDetectionAnnotation](objectdetectionannotation.md)
  An object detection annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionmetrics)*