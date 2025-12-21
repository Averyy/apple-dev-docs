# AVAudioCompressedBuffer

**Framework**: AVFAudio  
**Kind**: class

An object that represents an audio buffer that you use for compressed audio formats.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class AVAudioCompressedBuffer
```

## Topics

### Creating an Audio Buffer
- [init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount)](avaudiocompressedbuffer/init(format:packetcapacity:).md)
  Creates a buffer that contains constant bytes per packet of audio data in a compressed state.
- [init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount, maximumPacketSize: Int)](avaudiocompressedbuffer/init(format:packetcapacity:maximumpacketsize:).md)
  Creates a buffer that contains audio data in a compressed state.
### Getting Audio Buffer Properties
- [var byteCapacity: UInt32](avaudiocompressedbuffer/bytecapacity.md)
  The number of packets the buffer contains.
- [var byteLength: UInt32](avaudiocompressedbuffer/bytelength.md)
  The number of valid bytes in the buffer.
- [var data: UnsafeMutableRawPointer](avaudiocompressedbuffer/data.md)
  The audio buffer’s data bytes.
- [var maximumPacketSize: Int](avaudiocompressedbuffer/maximumpacketsize.md)
  The maximum size of a packet, in bytes.
- [var packetCapacity: AVAudioPacketCount](avaudiocompressedbuffer/packetcapacity.md)
  The total number of packets that the buffer can contain.
- [var packetCount: AVAudioPacketCount](avaudiocompressedbuffer/packetcount.md)
  The number of packets currently in the buffer.
- [typealias AVAudioPacketCount](avaudiopacketcount.md)
  The number of packets of audio data.
- [var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?](avaudiocompressedbuffer/packetdescriptions.md)
  The buffer’s array of packet descriptions.
- [var packetDependencies: [AudioStreamPacketDependencyDescription]?](avaudiocompressedbuffer/packetdependencies-3a6ln.md)
  The buffer’s array of packet dependencies.

## Relationships

### Inherits From
- [AVAudioBuffer](avaudiobuffer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSMutableCopying](../Foundation/NSMutableCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class AVAudioPCMBuffer](avaudiopcmbuffer.md)
  An object that represents an audio buffer you use with PCM audio formats.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer)*