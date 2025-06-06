# maximumPacketSize

**Framework**: AVFAudio  
**Kind**: property

The maximum size of a packet, in bytes.

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
var maximumPacketSize: Int { get }
```

## See Also

- [var byteCapacity: UInt32](avaudiocompressedbuffer/bytecapacity.md)
  The number of packets the buffer contains.
- [var byteLength: UInt32](avaudiocompressedbuffer/bytelength.md)
  The number of valid bytes in the buffer.
- [var data: UnsafeMutableRawPointer](avaudiocompressedbuffer/data.md)
  The audio buffer’s data bytes.
- [var packetCapacity: AVAudioPacketCount](avaudiocompressedbuffer/packetcapacity.md)
  The total number of packets that the buffer can contain.
- [var packetCount: AVAudioPacketCount](avaudiocompressedbuffer/packetcount.md)
  The number of packets currently in the buffer.
- [typealias AVAudioPacketCount](avaudiopacketcount.md)
  The number of packets of audio data.
- [var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?](avaudiocompressedbuffer/packetdescriptions.md)
  The buffer’s array of packet descriptions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/maximumpacketsize)*