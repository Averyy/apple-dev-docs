# data

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
var data: RawSpan { get }
```

## Discussion

The `RawSpan` is tied to the lifetime of this buffer and provides safe access to the raw compressed bytes.

> **Note**: The span contains `byteLength` bytes of valid data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiocompressedbuffer/data)*