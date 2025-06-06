# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics by evaluating the sound classifier’s performance on a dataset represented by a dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on testingData: [String : [URL]]) -> MLClassifierMetrics
```

#### Return Value

An [`MLClassifierMetrics`](mlclassifiermetrics.md) instance that contains the evaluation results.

## Parameters

- `testingData`: A collection of labeled audio files represented by a dictionary. Each key of the dictionary is   a label, and its value is an array of audio-file URLs.

## See Also

- [func evaluation(on: MLSoundClassifier.DataSource) -> MLClassifierMetrics](mlsoundclassifier/evaluation(on:)-7fmux.md)
  Generates metrics by evaluating the sound classifier’s performance on a dataset represented by a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)-8kplo)*