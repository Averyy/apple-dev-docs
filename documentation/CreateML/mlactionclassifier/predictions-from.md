# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Generates a sequence of predictions for each video input.

**Availability**:
- macOS 11.0+

## Declaration

```swift
func predictions(from videos: [URL]) throws -> [[MLActionClassifier.Prediction]]
```

#### Return Value

A array of prediction arrays. The index of each inner array corresponds to the video index in the input array.

#### Discussion

- videos: An array of locations to videos you want the action classifier to analyze.

## See Also

- [func prediction(from: URL) throws -> [MLActionClassifier.Prediction]](mlactionclassifier/prediction(from:).md)
  Generates a prediction for each action the classifier recognizes in the video.
- [MLActionClassifier.Prediction](mlactionclassifier/prediction.md)
  A collection of predictions, each paired with its confidence, for a range of video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlactionclassifier/predictions(from:))*