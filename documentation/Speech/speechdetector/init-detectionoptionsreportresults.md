# init(detectionOptions:reportResults:)

**Framework**: Speech  
**Kind**: init

Creates a speech detector.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)
```

## Parameters

- `detectionOptions`: Instance of   that allows clients to customize the behavior of   beyond its default settings.
- `reportResults`: Enables the   sequence to report the VAD model’s results (and any relevant errors) back to clients. The default behavior is that   does not report results or errors back to the client and merely enables VAD as a power optimization.

## See Also

- [convenience init()](speechdetector/init.md)
  Creates a speech detector with default settings.
- [SpeechDetector.DetectionOptions](speechdetector/detectionoptions.md)
  Allows clients to customize an instance of a speech detector.
- [SpeechDetector.SensitivityLevel](speechdetector/sensitivitylevel.md)
  Determines how “aggressive” the voice activity detection (VAD) model will be.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/init(detectionoptions:reportresults:))*