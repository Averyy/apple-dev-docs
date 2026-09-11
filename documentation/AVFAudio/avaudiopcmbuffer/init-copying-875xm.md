# init(copying:)

**Framework**: AVFAudio  
**Kind**: init

Creates a mutable buffer by copying a read-only buffer’s audio data.

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
convenience init(copying readOnlyBuffer: AVReadOnlyAudioPCMBuffer)
```

#### Discussion

This initializer allocates a new mutable buffer and copies all audio data from the read-only buffer.

## Parameters

- `readOnlyBuffer`: The read-only buffer to copy from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopcmbuffer/init(copying:)-875xm)*