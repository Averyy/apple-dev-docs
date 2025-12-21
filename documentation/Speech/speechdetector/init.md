# init()

**Framework**: Speech  
**Kind**: init

Creates a speech detector with default settings.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init()
```

#### Discussion

The default settings enable the VAD model with a value of [`SpeechDetector.SensitivityLevel.medium`](speechdetector/sensitivitylevel/medium.md) and do not report the VAD model’s moment-to-moment results in its result sequence.

## See Also

- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](speechdetector/init(detectionoptions:reportresults:).md)
  Creates a speech detector.
- [SpeechDetector.DetectionOptions](speechdetector/detectionoptions.md)
  Allows clients to customize an instance of a speech detector.
- [SpeechDetector.SensitivityLevel](speechdetector/sensitivitylevel.md)
  Determines how “aggressive” the voice activity detection (VAD) model will be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/init())*