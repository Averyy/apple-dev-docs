# init(unsafeRetaining:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a read-only buffer by retaining the existing compressed buffer without copying.

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
init(unsafeRetaining buffer: sending AVAudioCompressedBuffer)
```

## Discussion

> ⚠️ **Warning**: The caller must ensure the original buffer is not modified while this read-only buffer is in use. Violating this contract results in undefined behavior.

## Parameters

- `buffer`: The compressed buffer to retain (not copied).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiocompressedbuffer/init(unsaferetaining:))*