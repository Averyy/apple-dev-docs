# mFramesPerPacket

**Framework**: Core Audio Types  
**Kind**: property

The number of frames in a packet of audio data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var mFramesPerPacket: UInt32
```

#### Discussion

For uncompressed audio, the value is 1. For variable bit-rate formats, the value is a larger fixed number, such as 1024 for AAC. For formats with a variable number of frames per packet, such as Ogg Vorbis, set this field to `0`.

## See Also

- [var mFormatID: AudioFormatID](audiostreambasicdescription/mformatid.md)
  An identifier specifying the general audio data format in the stream.
- [var mFormatFlags: AudioFormatFlags](audiostreambasicdescription/mformatflags.md)
  Format-specific flags to specify details of the format.
- [var mSampleRate: Float64](audiostreambasicdescription/msamplerate.md)
  The number of frames per second of the data in the stream, when playing the stream at normal speed.
- [var mBitsPerChannel: UInt32](audiostreambasicdescription/mbitsperchannel.md)
  The number of bits for one audio sample.
- [var mBytesPerFrame: UInt32](audiostreambasicdescription/mbytesperframe.md)
  The number of bytes from the start of one frame to the start of the next frame in an audio buffer.
- [var mChannelsPerFrame: UInt32](audiostreambasicdescription/mchannelsperframe.md)
  The number of channels in each frame of audio data.
- [var mBytesPerPacket: UInt32](audiostreambasicdescription/mbytesperpacket.md)
  The number of bytes in a packet of audio data.
- [var mReserved: UInt32](audiostreambasicdescription/mreserved.md)
  The amount to pad the structure to force an even 8-byte alignment.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiostreambasicdescription/mframesperpacket)*