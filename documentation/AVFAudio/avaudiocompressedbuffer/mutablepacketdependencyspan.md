# mutablePacketDependencySpan

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Mutable access to packet dependencies.

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
var mutablePacketDependencySpan: MutableSpan<AudioStreamPacketDependencyDescription>? { get }
```

## Discussion

If the format doesn’t employ packet dependencies, this will be `nil`.

> ⚠️ **Warning**: This property cannot enforce exclusivity at compile time because `AVAudioCompressedBuffer` is an Objective-C class. The caller must ensure they don’t create overlapping mutable views to the same memory.

> **Note**: Provides access to the entire buffer (up to `packetCapacity`).


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/mutablepacketdependencyspan)*