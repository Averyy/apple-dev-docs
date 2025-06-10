# init()

**Framework**: Speech  
**Kind**: init

Creates a speech detector with default settings.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
convenience init()
```

#### Discussion

The default settings enable the VAD model with a value of [`SpeechDetector.SensitivityLevel.medium`](speechdetector/sensitivitylevel/medium.md) and do not report the VAD model’s moment-to-moment results in its result sequence.

## See Also

- [init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)](speechdetector/init(detectionoptions:reportresults:).md)
  Creates a speech detector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/init())*