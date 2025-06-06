# AudioStreamPacketDescription

**Framework**: Core Audio Types  
**Kind**: struct

A value that describes a packet in a buffer of audio data.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.2+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
struct AudioStreamPacketDescription
```

#### Overview

For data formats where the packet size isn’t constant, such as variable bit rate data and data where the channels have unequal sizes, use this structure to supplement the information in the [`AudioStreamBasicDescription`](audiostreambasicdescription.md) structure.

## Topics

### Inspecting an audio stream packet description
- [var mDataByteSize: UInt32](audiostreampacketdescription/mdatabytesize.md)
  The number of bytes in the packet.
- [var mStartOffset: Int64](audiostreampacketdescription/mstartoffset.md)
  The number of bytes from the start of the buffer to the beginning of the packet.
- [var mVariableFramesInPacket: UInt32](audiostreampacketdescription/mvariableframesinpacket.md)
  The number of sample frames of data in the packet.
### Creating an audio stream packet descripiton
- [init()](audiostreampacketdescription/init.md)
  Creates an audio stream basic description.
- [init(mStartOffset: Int64, mVariableFramesInPacket: UInt32, mDataByteSize: UInt32)](audiostreampacketdescription/init(mstartoffset:mvariableframesinpacket:mdatabytesize:).md)
  Creates an audio stream basic description with the start offset, and the number of sample frames and bytes in the packet that you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioStreamBasicDescription](audiostreambasicdescription.md)
  A format specification for an audio stream.
- [typealias AudioFormatFlags](audioformatflags.md)
  A type definition for audio format flags.
- [Audio Format Flags](audio-format-flags.md)
  Commonly used combinations of data format flags for an audio stream description.
- [typealias AudioFormatID](audioformatid.md)
  A type definition for audio format identifiers.
- [Audio Format Identifiers](audio-format-identifiers.md)
  Identifiers for supported audio formats.
- [let kAudioStreamAnyRate: Float64](kaudiostreamanyrate.md)
  A value that indicates that an audio stream can use any sample rate.
- [enum MPEG4ObjectID](mpeg4objectid.md)
  Constants that define the type of MPEG-4 audio data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/audiostreampacketdescription)*