# init(copying:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a mutable buffer by copying a read-only buffer’s compressed audio data.

**Availability**:
- iOS 27.3+ (Beta)
- iPadOS 27.3+ (Beta)
- Mac Catalyst 27.3+ (Beta)
- macOS 27.3+ (Beta)
- tvOS 27.3+ (Beta)
- visionOS 27.3+ (Beta)
- watchOS 27.3+ (Beta)

## Declaration

```swift
convenience init(copying readOnlyBuffer: AVReadOnlyAudioCompressedBuffer)
```

## Discussion

This initializer allocates a new mutable buffer and copies all compressed audio data from the read-only buffer.

## Parameters

- `readOnlyBuffer`: The read-only buffer to copy from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/init(copying:)-6ztfu)*