# predictions(from:)

**Framework**: Create ML  
**Kind**: method

Generates predictions for an array of audio files.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 10.15+
- visionOS 1.0+

## Declaration

```swift
func predictions(from audioFiles: [URL]) throws -> [String]
```

#### Return Value

An array of prediction labels for the audio files.

## Parameters

- `audioFiles`: An array of audio-file URLs you want the sound classifier to categorize.

## See Also

- [func predictions(from: [URL], overlapFactor: Double, predictionTimeWindowSize: TimeInterval) throws -> [String]](mlsoundclassifier/predictions(from:overlapfactor:predictiontimewindowsize:).md)
  Generates predictions that use an overlap factor and time window size for an array of audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/createml/mlsoundclassifier/predictions(from:))*