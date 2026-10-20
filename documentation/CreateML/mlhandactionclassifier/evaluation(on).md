# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates metrics describing the hand action classifier’s performance on labeled videos.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on annotatedVideos: MLHandActionClassifier.DataSource) throws -> MLClassifierMetrics
```

## Parameters

- `annotatedVideos`: An [`MLHandActionClassifier.DataSource`](./datasource.md) instance.

## See Also

### Evaluating a hand action classifier
- [var trainingMetrics: MLClassifierMetrics](./trainingmetrics.md)
  Measurements of the hand action classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](./validationmetrics.md)
  Measurements of the hand action classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/evaluation(on:))*