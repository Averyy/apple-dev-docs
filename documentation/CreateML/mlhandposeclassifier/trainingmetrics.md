# trainingMetrics

**Framework**: Create ML  
**Kind**: property  
**Role**: Instance Property

Measurements of the hand pose classifier’s performance on the training dataset.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
var trainingMetrics: MLClassifierMetrics
```

## See Also

### Evaluating a hand pose classifier
- [func evaluation(on: MLHandPoseClassifier.DataSource) throws -> MLClassifierMetrics](./evaluation%28on%29.md)
  Generates metrics that describe the hand pose classifier’s performance with a dataset of labeled images.
- [var validationMetrics: MLClassifierMetrics](./validationmetrics.md)
  Measurements of the hand pose classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/trainingmetrics)*