# bestAvailableAudioFormat(compatibleWith:)

**Framework**: Speech  
**Kind**: method

Retrieves the best-quality audio format that the specified modules can work with, from assets installed on the device.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
static func bestAvailableAudioFormat(compatibleWith modules: [any SpeechModule]) async -> AVAudioFormat?
```

#### Return Value

`nil` if the specified modules require you to install additional assets.

#### Discussion

Use this method to set up an audio pipeline or pre-convert audio to a usable format. In order to keep `CMTime` values sample-accurate, the analyzer does not transparently upsample, downsample, or convert audio input.

## Parameters

- `modules`: A list of modules that will be analyzing the audio.

## See Also

- [static func bestAvailableAudioFormat(compatibleWith: [any SpeechModule], considering: AVAudioFormat?) async -> AVAudioFormat?](speechanalyzer/bestavailableaudioformat(compatiblewith:considering:).md)
  Retrieves the best-quality audio format that the specified modules can work with, taking into account the natural format of the audio and assets installed on the device.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/speechanalyzer/bestavailableaudioformat(compatiblewith:))*