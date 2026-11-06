# packetDescriptionsSpan

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Read-only access to packet descriptions.

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
var packetDescriptionsSpan: Span<AudioStreamPacketDescription>? { get }
```

## Discussion

For variable bytes-per-packet formats, each packet has an associated description containing its offset and size within the buffer.

> ⚠️ **Warning**: This property cannot enforce exclusivity at compile time because `AVAudioCompressedBuffer` is an Objective-C class. The caller must ensure proper synchronization when accessing the buffer concurrently or when the buffer might be modified.

> **Note**: Provides access to valid data only (up to `packetCount`). Returns `nil` for constant bytes-per-packet formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/packetdescriptionsspan)*