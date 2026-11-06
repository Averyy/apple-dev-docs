# init(copying:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a mutable buffer by copying another compressed buffer’s audio data.

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
convenience init(copying source: AVAudioCompressedBuffer)
```

## Discussion

This initializer allocates a new mutable buffer and copies all compressed audio data.

## Parameters

- `source`: The source compressed buffer to copy from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/init(copying:)-65xzn)*