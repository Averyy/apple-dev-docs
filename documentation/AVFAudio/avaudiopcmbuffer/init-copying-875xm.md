# init(copying:)

**Framework**: AVFAudio  
**Kind**: init

Creates a mutable buffer by copying a read-only buffer’s audio data.

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
convenience init(copying readOnlyBuffer: AVReadOnlyAudioPCMBuffer)
```

#### Discussion

This initializer allocates a new mutable buffer and copies all audio data from the read-only buffer.

## Parameters

- `readOnlyBuffer`: The read-only buffer to copy from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(copying:)-875xm)*