# init(copying:)

**Framework**: AVFAudio  
**Kind**: init

Creates a mutable buffer by copying another PCM buffer’s audio data.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- tvOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
convenience init(copying source: AVAudioPCMBuffer)
```

#### Discussion

This initializer allocates a new mutable buffer and copies all audio data channel by channel.

## Parameters

- `source`: The source PCM buffer to copy from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(copying:)-68es5)*