# init(copying:)

**Framework**: AVFAudio  
**Kind**: init

Creates a mutable buffer by copying another PCM buffer’s audio data.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

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