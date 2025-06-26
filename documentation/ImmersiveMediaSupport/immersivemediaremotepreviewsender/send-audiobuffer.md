# send(audioBuffer:)

**Framework**: Immersive Media Support  
**Kind**: method

Sends an audio frame to all connected receivers.

**Availability**:
- macOS 26.0+ (Beta)

## Declaration

```swift
func send(audioBuffer: CMSampleBuffer) async throws
```

#### Discussion

> **Note**: This function will throw if anything fails while sending the audio data, for example, if the audio sample buffer has an invalid format or data.

## Parameters

- `audioBuffer`: The audio buffer to be sent to the receivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/immersivemediasupport/immersivemediaremotepreviewsender/send(audiobuffer:))*