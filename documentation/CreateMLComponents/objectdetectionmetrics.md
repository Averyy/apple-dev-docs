# ObjectDetectionMetrics

**Framework**: Create ML Components  
**Kind**: struct  
**Role**: Structure

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
- [init()](./objectdetectionmetrics/init%28%29.md)
### Getting the properties Properties
- [var defaultConfidenceThreshold: Float](./objectdetectionmetrics/defaultconfidencethreshold.md)
  The default confidence threshold. It is used as the confidence threshold for any label which does not have an explicit confidence threshold, while calculating averagePrecision and meanAveragePrecision.
- [var labels: Set<Label>](./objectdetectionmetrics/labels.md)
  A set of labels present in the dataset.
### Calculating the precision
- [func averageOfAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float]) -> [Label : Scalar]](./objectdetectionmetrics/averageofaverageprecisionatvariedthresholds%28predictions,annotations,confidencethresholds%29.md)
  Calculates average of average precision for all the labels, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.
- [func averageOfMeanAveragePrecisionAtVariedThresholds<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float]) -> Scalar](./objectdetectionmetrics/averageofmeanaverageprecisionatvariedthresholds%28predictions,annotations,confidencethresholds%29.md)
  Calculates the average of mean average precision, computed at varied bounding box overlap thresholds. The overlap thresholds range is from `[0.05, 0.95]` with a stride of `0.05`.
- [func averagePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float], overlapThreshold: Double) -> [Label : Scalar]](./objectdetectionmetrics/averageprecision%28predictions,annotations,confidencethresholds,overlapthreshold%29.md)
  Calculates average precision for all the labels at the bounding box overlap threshold.
- [func meanAveragePrecision<Scalar>(predictions: [[DetectedObject<Label>]], annotations: [ObjectDetectionAnnotation<Label>], confidenceThresholds: [Label : Float], overlapThreshold: Double) -> Scalar](./objectdetectionmetrics/meanaverageprecision%28predictions,annotations,confidencethresholds,overlapthreshold%29.md)
  Calculates the mean average precision at the bounding box overlap threshold.
### Extracting labels
- [static func extractLabels(from: [ObjectDetectionAnnotation<Label>]) -> Set<Label>](./objectdetectionmetrics/extractlabels%28from%29.md)
  Extracts all the labels from a list of annotations.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Object detection components
- [struct DetectedObject](./detectedobject.md)
  An item in a detection result.
- [struct ObjectDetectionAnnotation](./objectdetectionannotation.md)
  An object detection annotation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createmlcomponents/objectdetectionmetrics)*