# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics describing the image classifier’s performance on labeled images represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on labeledImages: MLImageClassifier.DataSource) -> MLClassifierMetrics
```

#### Return Value

The metrics that indicate the performance of the classifier when operating on the input dataset.

## Parameters

- `labeledImages`: A set of labeled images in a data source.

## See Also

- [var trainingMetrics: MLClassifierMetrics](mlimageclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlimageclassifier/validationmetrics.md)
  Measurements of the image classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/evaluation(on:))*