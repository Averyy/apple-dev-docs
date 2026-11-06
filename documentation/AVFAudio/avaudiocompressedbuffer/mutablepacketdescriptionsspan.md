# mutablePacketDescriptionsSpan

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Mutable access to packet descriptions.

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
var mutablePacketDescriptionsSpan: MutableSpan<AudioStreamPacketDescription>? { get }
```

## Discussion

For variable bytes-per-packet formats, each packet has an associated description containing its offset and size within the buffer.

> ⚠️ **Warning**: This property cannot enforce exclusivity at compile time because `AVAudioCompressedBuffer` is an Objective-C class. The caller must ensure they don’t create overlapping mutable views to the same memory.

> **Note**: Provides access to the entire buffer (up to `packetCapacity`). Returns `nil` for constant bytes-per-packet formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/mutablepacketdescriptionsspan)*