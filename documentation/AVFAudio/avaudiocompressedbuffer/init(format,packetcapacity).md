# init(format:packetCapacity:)

**Framework**: AVFAudio  
**Kind**: init  
**Role**: Initializer

Creates a buffer that contains constant bytes per packet of audio data in a compressed state.

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
init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount)
```

```objc
- (instancetype) initWithFormat:(AVAudioFormat *) format packetCapacity:(AVAudioPacketCount) packetCapacity;
```

#### Return Value

A new [`AVAudioCompressedBuffer`](../avaudiocompressedbuffer.md) instance.

#### Discussion

This fails if the format is PCM or if the format has variable bytes per packet (for example, `format.streamDescription->mBytesPerPacket == 0`).

## Parameters

- `format`: The format of the audio the buffer contains.
- `packetCapacity`: The capacity of the buffer, in packets.

## See Also

### Creating an audio buffer
- [init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount, maximumPacketSize: Int)](./init%28format,packetcapacity,maximumpacketsize%29.md)
  Creates a buffer that contains audio data in a compressed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/init(format:packetcapacity:))*