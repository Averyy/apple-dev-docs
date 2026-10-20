# validationMetrics

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Measurements of the hand action classifier’s performance on the validation dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var validationMetrics: MLClassifierMetrics
```

## See Also

### Evaluating a hand action classifier
- [func evaluation(on: MLHandActionClassifier.DataSource) throws -> MLClassifierMetrics](./evaluation%28on%29.md)
  Generates metrics describing the hand action classifier’s performance on labeled videos.
- [var trainingMetrics: MLClassifierMetrics](./trainingmetrics.md)
  Measurements of the hand action classifier’s performance on the training dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/validationmetrics)*