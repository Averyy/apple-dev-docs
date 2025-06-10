# init(buffer:)

**Framework**: Speech  
**Kind**: init

Creates an audio input object.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
init(buffer: AVAudioPCMBuffer)
```

#### Discussion

This audio buffer is assumed to start immediately after the previous buffer (or at time-code zero if there is no previous buffer).

## Parameters

- `buffer`: An audio buffer.

## See Also

- [init(buffer: AVAudioPCMBuffer, bufferStartTime: CMTime?)](analyzerinput/init(buffer:bufferstarttime:).md)
  Creates an audio input object for audio that may be discontiguous with previous input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/speech/analyzerinput/init(buffer:))*