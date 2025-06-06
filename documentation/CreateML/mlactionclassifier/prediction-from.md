# prediction(from:)

**Framework**: Create ML  
**Kind**: method

Generates a prediction for each action the classifier recognizes in the video.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func prediction(from video: URL) throws -> [MLActionClassifier.Prediction]
```

#### Return Value

An array of predictions.

#### Discussion

- video: The location of a video you want the action classifier to analyze.

## See Also

- [func predictions(from: [URL]) throws -> [[MLActionClassifier.Prediction]]](mlactionclassifier/predictions(from:).md)
  Generates a sequence of predictions for each video input.
- [MLActionClassifier.Prediction](mlactionclassifier/prediction.md)
  A collection of predictions, each paired with its confidence, for a range of video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/prediction(from:))*