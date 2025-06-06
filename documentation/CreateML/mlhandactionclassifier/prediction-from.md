# prediction(from:)

**Framework**: Create ML  
**Kind**: method

Generates a hand action prediction for a video.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func prediction(from video: URL) throws -> [MLHandActionClassifier.Prediction]
```

#### Return Value

An array of predictions.

## See Also

- [func predictions(from: [URL]) throws -> [[MLHandActionClassifier.Prediction]]](mlhandactionclassifier/predictions(from:).md)
  Generates an array of hand action predictions for each video in a URL array.
- [MLHandActionClassifier.Prediction](mlhandactionclassifier/prediction.md)
  A collection of predictions, each paired with its confidence, for a range of video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/prediction(from:))*