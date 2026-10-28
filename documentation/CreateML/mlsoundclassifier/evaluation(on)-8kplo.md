# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates metrics by evaluating the sound classifier’s performance on a dataset represented by a dictionary.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.15+ - Deprecated in 11.0
- visionOS 1.0+

> **Deprecated**: Use DataSource.filesByLabel to provide dictionary testing data instead.

## Declaration

```swift
func evaluation(on testingData: [String : [URL]]) -> MLClassifierMetrics
```

**Other overloads**:

```swift
func evaluation(on testingData: MLSoundClassifier.DataSource) -> MLClassifierMetrics
```

## Return Value

An [`MLClassifierMetrics`](../mlclassifiermetrics.md) instance that contains the evaluation results.

## Parameters

- `testingData`: A collection of labeled audio files represented by a dictionary. Each key of the dictionary is a label, and its value is an array of audio-file URLs.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/evaluation(on:)-8kplo)*