# MLActionClassifier.Prediction

**Framework**: Create ML  
**Kind**: struct  
**Role**: Structure

A collection of predictions, each paired with its confidence, for a range of video frames.

**Availability**:
- macOS 11.0+

## Declaration

```swift
struct Prediction
```

## Topics

### Inspecting a prediction
- [var results: [(label: String, confidence: Double)]](./prediction/results.md)
  An array of prediction labels and their confidences for an action.
- [var frameRange: Range<Int>](./prediction/framerange.md)
  The range of frame rates the action classifier used to make its prediction.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Testing an action classifier
- [func prediction(from: URL) throws -> [MLActionClassifier.Prediction]](./prediction%28from%29.md)
  Generates a prediction for each action the classifier recognizes in the video.
- [func predictions(from: [URL]) throws -> [[MLActionClassifier.Prediction]]](./predictions%28from%29.md)
  Generates a sequence of predictions for each video input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/prediction)*