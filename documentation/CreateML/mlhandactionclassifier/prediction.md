# MLHandActionClassifier.Prediction

**Framework**: Create ML  
**Kind**: struct

A collection of predictions, each paired with its confidence, for a range of video frames.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
struct Prediction
```

## Topics

### Inspecting a prediction
- [var results: [(label: String, confidence: Double)]](mlhandactionclassifier/prediction/results.md)
  An array of prediction labels and their confidences for a hand action.
- [var frameRange: Range<Int>](mlhandactionclassifier/prediction/framerange.md)
  The range of frame rates the hand action classifier used to make its prediction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func prediction(from: URL) throws -> [MLHandActionClassifier.Prediction]](mlhandactionclassifier/prediction(from:).md)
  Generates a hand action prediction for a video.
- [func predictions(from: [URL]) throws -> [[MLHandActionClassifier.Prediction]]](mlhandactionclassifier/predictions(from:).md)
  Generates an array of hand action predictions for each video in a URL array.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/prediction)*