# predictions(from:overlapFactor:predictionTimeWindowSize:)

**Framework**: Create ML  
**Kind**: method

Generates predictions that use an overlap factor and time window size for an array of audio files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- visionOS 1.0+

## Declaration

```swift
func predictions(from audioFiles: [URL], overlapFactor: Double, predictionTimeWindowSize: TimeInterval) throws -> [String]
```

#### Return Value

An array of prediction labels for the audio files.

## Parameters

- `audioFiles`: An array of audio-file URLs you want the sound classifier to categorize.
- `overlapFactor`: The amount of overlap between successive analysis windows when the model analyzes a block of   audio data.
- `predictionTimeWindowSize`: The duration of the audio buffer the method sends to the model for each   prediction.

## See Also

- [func predictions(from: [URL]) throws -> [String]](mlsoundclassifier/predictions(from:).md)
  Generates predictions for an array of audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:))*