# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Generates an array of hand action predictions for each video in a URL array.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func predictions(from videos: [URL]) throws -> [[MLHandActionClassifier.Prediction]]
```

#### Return Value

A array of prediction arrays. The index of each inner array corresponds to the video URL index in the input array.

## Parameters

- `videos`: An array of video file URLs.

## See Also

- [func prediction(from: URL) throws -> [MLHandActionClassifier.Prediction]](mlhandactionclassifier/prediction(from:).md)
  Generates a hand action prediction for a video.
- [MLHandActionClassifier.Prediction](mlhandactionclassifier/prediction.md)
  A collection of predictions, each paired with its confidence, for a range of video frames.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlhandactionclassifier/predictions(from:))*