# bestAvailableAudioFormat(compatibleWith:considering:)

**Framework**: Speech  
**Kind**: method

Retrieves the best-quality audio format that the specified modules can work with, taking into account the natural format of the audio and assets installed on the device.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
static func bestAvailableAudioFormat(compatibleWith modules: [any SpeechModule], considering naturalFormat: AVAudioFormat?) async -> AVAudioFormat?
```

#### Return Value

`nil` if the specified modules require you to install additional assets.

#### Discussion

Use this method to set up an audio pipeline or pre-convert audio to a usable format. In order to keep `CMTime` values sample-accurate, the analyzer does not transparently upsample, downsample, or convert audio input.

## Parameters

- `modules`: A list of modules that will be analyzing the audio.
- `naturalFormat`: An audio format that you prefer to work with, or   if you have no preference.

## See Also

- [static func bestAvailableAudioFormat(compatibleWith: [any SpeechModule]) async -> AVAudioFormat?](speechanalyzer/bestavailableaudioformat(compatiblewith:).md)
  Retrieves the best-quality audio format that the specified modules can work with, from assets installed on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/bestavailableaudioformat(compatiblewith:considering:))*