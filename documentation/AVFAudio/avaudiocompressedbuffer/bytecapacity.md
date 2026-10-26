# byteCapacity

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The number of packets the buffer contains.

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
var byteCapacity: UInt32 { get }
```

```objc
@property (nonatomic, readonly) uint32_t byteCapacity;
```

## See Also

### Getting audio buffer properties
- [var byteLength: UInt32](./bytelength.md)
  The number of valid bytes in the buffer.
- [var data: UnsafeMutableRawPointer](./data.md)
  The audio buffer’s data bytes.
- [var maximumPacketSize: Int](./maximumpacketsize.md)
  The maximum size of a packet, in bytes.
- [var packetCapacity: AVAudioPacketCount](./packetcapacity.md)
  The total number of packets that the buffer can contain.
- [var packetCount: AVAudioPacketCount](./packetcount.md)
  The number of packets currently in the buffer.
- [typealias AVAudioPacketCount](../avaudiopacketcount.md)
  The number of packets of audio data.
- [var packetDescriptions: UnsafeMutablePointer<AudioStreamPacketDescription>?](./packetdescriptions.md)
  The buffer’s array of packet descriptions.
- [var packetDependencies: [AudioStreamPacketDependencyDescription]?](./packetdependencies-3a6ln.md)
  The buffer’s array of packet dependencies.
- [packetDependencies](./packetdependencies-5oae6.md)
  The buffer’s array of packet dependencies.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/bytecapacity)*