# init(detectionOptions:reportResults:)

**Framework**: Speech  
**Kind**: init

Creates a speech detector.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(detectionOptions: SpeechDetector.DetectionOptions, reportResults: Bool)
```

## Parameters

- `detectionOptions`: Instance of   that allows clients to customize the behavior of   beyond its default settings.
- `reportResults`: Enables the   sequence to report the VAD model’s results (and any relevant errors) back to clients. The default behavior is that   does not report results or errors back to the client.

## See Also

- [convenience init()](speechdetector/init.md)
  Creates a speech detector with default settings.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechdetector/init(detectionoptions:reportresults:))*