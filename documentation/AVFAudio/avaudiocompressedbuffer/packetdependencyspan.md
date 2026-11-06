# packetDependencySpan

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

Read-only access to packet dependencies.

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
var packetDependencySpan: Span<AudioStreamPacketDependencyDescription>? { get }
```

## Discussion

If the format doesn’t employ packet dependencies, this will be `nil`.

> ⚠️ **Warning**: This property cannot enforce exclusivity at compile time because `AVAudioCompressedBuffer` is an Objective-C class. The caller must ensure proper synchronization when accessing the buffer concurrently or when the buffer might be modified.

> **Note**: Provides access to valid data only (up to `packetCount`). This property replaces the deprecated `packetDependencies` property.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/packetdependencyspan)*