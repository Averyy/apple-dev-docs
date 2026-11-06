# AVReadOnlyAudioCompressedBuffer

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

A read-only, Sendable audio buffer for safe concurrent access to compressed audio data.

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
struct AVReadOnlyAudioCompressedBuffer
```

## Topics

### Initializers
- [init(copying: AVAudioCompressedBuffer)](./avreadonlyaudiocompressedbuffer/init%28copying%29.md)
  Creates a read-only buffer by copying compressed audio data from an existing buffer.
- [init(format: AVAudioFormat, packetCapacity: Int, initializingWith: (inout OutputSpan<UInt8>) throws -> Int) throws](./avreadonlyaudiocompressedbuffer/init%28format,packetcapacity,initializingwith%29.md)
  Creates a read-only buffer for constant bytes-per-packet formats.
- [init(format: AVAudioFormat, packetCapacity: Int, maximumPacketSize: Int, initializingWith: (inout OutputSpan<UInt8>, inout OutputSpan<AudioStreamPacketDescription>) throws -> (packetCount: Int, byteLength: Int)) throws](./avreadonlyaudiocompressedbuffer/init%28format,packetcapacity,maximumpacketsize,initializingwith%29.md)
  Creates a read-only buffer for variable bytes-per-packet formats.
- [init(unsafeRetaining: sending AVAudioCompressedBuffer)](./avreadonlyaudiocompressedbuffer/init%28unsaferetaining%29.md)
  Creates a read-only buffer by retaining the existing compressed buffer without copying.
### Instance Properties
- [var byteCapacity: Int](./avreadonlyaudiocompressedbuffer/bytecapacity.md)
- [var byteLength: Int](./avreadonlyaudiocompressedbuffer/bytelength.md)
- [var data: RawSpan](./avreadonlyaudiocompressedbuffer/data.md)
  Read-only access to the compressed audio data.
- [var format: AVAudioFormat](./avreadonlyaudiocompressedbuffer/format.md)
- [var maximumPacketSize: Int](./avreadonlyaudiocompressedbuffer/maximumpacketsize.md)
- [var packetCapacity: Int](./avreadonlyaudiocompressedbuffer/packetcapacity.md)
- [var packetCount: Int](./avreadonlyaudiocompressedbuffer/packetcount.md)
- [var packetDependencies: Span<AudioStreamPacketDependencyDescription>?](./avreadonlyaudiocompressedbuffer/packetdependencies.md)
  Read-only access to packet dependencies.
- [var packetDescriptions: Span<AudioStreamPacketDescription>?](./avreadonlyaudiocompressedbuffer/packetdescriptions.md)
  Read-only access to packet descriptions.

## Relationships

### Conforms To
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avreadonlyaudiocompressedbuffer)*