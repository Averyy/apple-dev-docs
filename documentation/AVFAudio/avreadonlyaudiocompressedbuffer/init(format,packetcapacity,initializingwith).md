# init(format:packetCapacity:initializingWith:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a read-only buffer for constant bytes-per-packet formats.

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
init(format: AVAudioFormat, packetCapacity: Int, initializingWith: @_lifetime(data: copy data) (inout OutputSpan<UInt8>) throws -> Int) throws
```

## Discussion

> **Throws**: An error if allocation fails or the closure throws.

## Parameters

- `format`: The compressed audio format with constant bytes-per-packet (must not be PCM).
- `packetCapacity`: The maximum number of packets the buffer can hold.
- `initializingWith`: Closure that initializes the buffer and returns packet count.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiocompressedbuffer/init(format:packetcapacity:initializingwith:))*