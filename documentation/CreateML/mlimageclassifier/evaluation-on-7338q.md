# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics describing the image classifier’s performance on labeled images represented by a dictionary.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on labeledImages: [String : [URL]]) -> MLClassifierMetrics
```

#### Return Value

The metrics that indicate the performance of the classifier when operating on the input dataset.

## Parameters

- `labeledImages`: A dictionary with keys that are labels, and values that are arrays of image URLs   corresponding to those labels.

## See Also

- [func evaluation(on: MLImageClassifier.DataSource) -> MLClassifierMetrics](mlimageclassifier/evaluation(on:)-9p8mi.md)
  Generates metrics describing the image classifier’s performance on labeled images represented by a data source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/evaluation(on:)-7338q)*