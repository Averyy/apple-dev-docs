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

- [func evaluation(on: [String : [URL]]) -> MLClassifierMetrics](mlsoundclassifier/evaluation(on:)-8kplo.md)
  Generates metrics by evaluating the sound classifier’s performance on a dataset represented by a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)-7fmux)*