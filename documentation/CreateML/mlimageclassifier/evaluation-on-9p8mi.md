# evaluation(on:)

**Framework**: Create ML  
**Kind**: method

Generates metrics describing the image classifier’s performance on labeled images represented by a data source.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.14+
- visionOS 1.0+

## Declaration

```swift
func evaluation(on labeledImages: MLImageClassifier.DataSource) -> MLClassifierMetrics
```

## Mentions

- [Creating an Image Classifier Model](creating-an-image-classifier-model.md)

#### Return Value

The metrics that indicate the performance of the classifier when operating on the input dataset.

## Parameters

- `labeledImages`: A set of labeled images in a data source.

## See Also

- [func evaluation(on: [String : [URL]]) -> MLClassifierMetrics](mlimageclassifier/evaluation(on:)-7338q.md)
  Generates metrics describing the image classifier’s performance on labeled images represented by a dictionary.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlimageclassifier/evaluation(on:)-9p8mi)*