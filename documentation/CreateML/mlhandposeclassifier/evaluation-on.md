# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics that describe the hand pose classifier’s performance with a dataset of labeled images.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on annotatedImages: MLHandPoseClassifier.DataSource) throws -> MLClassifierMetrics
```

## See Also

- [var trainingMetrics: MLClassifierMetrics](mlhandposeclassifier/trainingmetrics.md)
  Measurements of the hand pose classifier’s performance on the training dataset.
- [var validationMetrics: MLClassifierMetrics](mlhandposeclassifier/validationmetrics.md)
  Measurements of the hand pose classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandposeclassifier/evaluation(on:))*