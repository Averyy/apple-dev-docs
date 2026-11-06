# mutableDataSpan

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Mutable access to the compressed audio data.

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
var mutableDataSpan: MutableRawSpan { get }
```

## Discussion

The `MutableRawSpan` is tied to the lifetime of this buffer and provides safe mutable access to the raw compressed bytes.

> ⚠️ **Warning**: This property cannot enforce exclusivity at compile time because `AVAudioCompressedBuffer` is an Objective-C class. The caller must ensure they don’t create overlapping mutable views to the same memory.

> **Note**: Provides access to the entire buffer (up to `byteCapacity`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/mutabledataspan)*