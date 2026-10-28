# evaluation(on:)

**Framework**: Create ML  
**Kind**: method  
**Role**: Instance Method

Generates metrics describing the image classifier’s performance on labeled images represented by a dictionary.

**Availability**:
- iOS 15.0+ - Deprecated in 16.0
- iPadOS 15.0+ - Deprecated in 16.0
- Mac Catalyst 15.0+ - Deprecated in 16.0
- macOS 10.14+ - Deprecated in 11.0
- visionOS 1.0+

> **Deprecated**: Use DataSource.filesByLabel to provide dictionary training data instead.

## Declaration

```swift
func evaluation(on labeledImages: [String : [URL]]) -> MLClassifierMetrics
```

**Other overloads**:

```swift
func evaluation(on labeledImages: MLImageClassifier.DataSource) -> MLClassifierMetrics
```

## Return Value

The metrics that indicate the performance of the classifier when operating on the input dataset.

## Parameters

- `labeledImages`: A dictionary with keys that are labels, and values that are arrays of image URLs corresponding to those labels.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/evaluation(on:)-7338q)*