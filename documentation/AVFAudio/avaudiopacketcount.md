# AVAudioPacketCount

**Framework**: AVFAudio  
**Kind**: typealias  
**Role**: Type Alias

The number of packets of audio data.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias AVAudioPacketCount = UInt32
```

```c
typedef uint32_t AVAudioPacketCount;
```

## See Also

### Getting audio buffer properties
- [var byteCapacity: UInt32](./avaudiocompressedbuffer/bytecapacity.md)
  The number of packets the buffer contains.
- [var byteLength: UInt32](./avaudiocompressedbuffer/bytelength.md)
  The number of valid bytes in the buffer.
- [var data: UnsafeMutableRawPointer](./avaudiocompressedbuffer/data.md)
  The audio buffer’s data bytes.
- [var maximumPacketSize: Int](./avaudiocompressedbuffer/maximumpacketsize.md)
  The maximum size of a packet, in bytes.
- [var packetCapacity: AVAudioPacketCount](./avaudiocompressedbuffer/packetcapacity.md)
  The total number of packets that the buffer can contain.
- [var packetCount: AVAudioPacketCount](./avaudiocompressedbuffer/packetcount.md)
  The number of packets currently in the buffer.
- [var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?](./avaudiocompressedbuffer/packetdescriptions.md)
  The buffer’s array of packet descriptions.
- [var packetDependencies: [AudioStreamPacketDependencyDescription]?](./avaudiocompressedbuffer/packetdependencies-3a6ln.md)
  The buffer’s array of packet dependencies.
- [packetDependencies](./avaudiocompressedbuffer/packetdependencies-5oae6.md)
  The buffer’s array of packet dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiopacketcount)*