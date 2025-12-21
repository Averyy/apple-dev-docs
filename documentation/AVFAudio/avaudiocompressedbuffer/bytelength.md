# byteLength

**Framework**: AVFAudio  
**Kind**: property

The number of valid bytes in the buffer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var byteLength: UInt32 { get set }
```

#### Discussion

You can change this value as part of an operation that modifies the contents.

## See Also

- [var byteCapacity: UInt32](avaudiocompressedbuffer/bytecapacity.md)
  The number of packets the buffer contains.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/bytelength)*