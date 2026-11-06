# init(copying:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a read-only buffer by copying compressed audio data from an existing buffer.

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
init(copying buffer: AVAudioCompressedBuffer)
```

## Discussion

This initializer creates a new `AVAudioCompressedBuffer` and copies all compressed audio data, ensuring the original buffer can continue to be used safely.

## Parameters

- `buffer`: The source compressed buffer to copy from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiocompressedbuffer/init(copying:))*