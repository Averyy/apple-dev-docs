# MLActionClassifier.Prediction

**Framework**: Create ML  
**Kind**: struct

A collection of predictions, each paired with its confidence, for a range of video frames.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct Prediction
```

## Topics

### Inspecting a prediction
- [var results: [(label: String, confidence: Double)]](mlactionclassifier/prediction/results.md)
  An array of prediction labels and their confidences for an action.
- [var frameRange: Range<Int>](mlactionclassifier/prediction/framerange.md)
  The range of frame rates the action classifier used to make its prediction.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [func prediction(from: URL) throws -> [MLActionClassifier.Prediction]](mlactionclassifier/prediction(from:).md)
  Generates a prediction for each action the classifier recognizes in the video.
- [func predictions(from: [URL]) throws -> [[MLActionClassifier.Prediction]]](mlactionclassifier/predictions(from:).md)
  Generates a sequence of predictions for each video input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/prediction)*