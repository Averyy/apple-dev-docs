# init(format:packetCapacity:maximumPacketSize:initializingWith:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a read-only buffer for variable bytes-per-packet formats.

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
init(format: AVAudioFormat, packetCapacity: Int, maximumPacketSize: Int, initializingWith: @_lifetime(data: copy data) @_lifetime(packetDescriptions: copy packetDescriptions) (inout OutputSpan<UInt8>, inout OutputSpan<AudioStreamPacketDescription>) throws -> (packetCount: Int, byteLength: Int)) throws
```

## Discussion

> **Throws**: An error if allocation fails or the closure throws.

## Parameters

- `format`: The compressed audio format (must not be PCM).
- `packetCapacity`: The maximum number of packets the buffer can hold.
- `maximumPacketSize`: The maximum size in bytes of any single packet.
- `initializingWith`: Closure that initializes the buffer and returns packet count and byte length.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiocompressedbuffer/init(format:packetcapacity:maximumpacketsize:initializingwith:))*