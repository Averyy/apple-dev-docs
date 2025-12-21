# packetDependencies

**Framework**: AVFAudio  
**Kind**: property

The buffer’s array of packet dependencies.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst ?+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var packetDependencies: [AudioStreamPacketDependencyDescription]? { get }
```

#### Discussion

If the audio format doesn’t use packet dependencies, this value is `nil`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/packetdependencies-3a6ln)*