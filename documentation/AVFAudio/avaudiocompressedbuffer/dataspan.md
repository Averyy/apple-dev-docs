# dataSpan

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Read-only access to the compressed audio data.

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
var dataSpan: RawSpan { get }
```

## Discussion

The `RawSpan` is tied to the lifetime of this buffer and provides safe read-only access to the raw compressed bytes.

> ⚠️ **Warning**: This property cannot enforce exclusivity at compile time because `AVAudioCompressedBuffer` is an Objective-C class. The caller must ensure proper synchronization when accessing the buffer concurrently or when the buffer might be modified.

> **Note**: Provides access to valid data only (up to `byteLength`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/dataspan)*