# init(format:packetCapacity:maximumPacketSize:)

**Framework**: AVFAudio  
**Kind**: init

Creates a buffer that contains audio data in a compressed state.

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
init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount, maximumPacketSize: Int)
```

#### Return Value

A new [`AVAudioCompressedBuffer`](avaudiocompressedbuffer.md) instance.

#### Discussion

You can obtain the maximum packet size from the [`maximumOutputPacketSize`](avaudioconverter/maximumoutputpacketsize.md) property of an [`AVAudioConverter`](avaudioconverter.md) you configure for encoding this format.

The method raises an exception if the format is PCM.

## Parameters

- `format`: The format of the audio the buffer contains.
- `packetCapacity`: The capacity of the buffer, in packets.
- `maximumPacketSize`: The maximum size in bytes of a packet in a compressed state.

## See Also

- [init(format: AVAudioFormat, packetCapacity: AVAudioPacketCount)](avaudiocompressedbuffer/init(format:packetcapacity:).md)
  Creates a buffer that contains constant bytes per packet of audio data in a compressed state.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiocompressedbuffer/init(format:packetcapacity:maximumpacketsize:))*