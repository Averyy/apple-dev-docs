# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics by evaluating the sound classifier’s performance on a dataset represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on testingData: MLSoundClassifier.DataSource) -> MLClassifierMetrics
```

#### Return Value

An [`MLClassifierMetrics`](mlclassifiermetrics.md) instance that contains the evaluation results.

## Parameters

- `testingData`: A collection of labeled audio files represented by an  .

## See Also

- [var trainingMetrics: MLClassifierMetrics](mlsoundclassifier/trainingmetrics.md)
  Measurements of the classifier’s performance on the training data set.
- [var validationMetrics: MLClassifierMetrics](mlsoundclassifier/validationmetrics.md)
  Measurements of the image classifier’s performance on the validation dataset.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:))*