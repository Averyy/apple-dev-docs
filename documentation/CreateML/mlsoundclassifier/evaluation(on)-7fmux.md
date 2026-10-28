# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

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

**Other overloads**:

```swift
func evaluation(on testingData: [String : [URL]]) -> MLClassifierMetrics
```

## Return Value

An [`MLClassifierMetrics`](../mlclassifiermetrics.md) instance that contains the evaluation results.

## Parameters

- `testingData`: A collection of labeled audio files represented by an [`MLSoundClassifier.DataSource`](./datasource.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)-7fmux)*