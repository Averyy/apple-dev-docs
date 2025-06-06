# IOUserAudioStreamBasicDescription

**Framework**: AudioDriverKit  
**Kind**: struct

A structure that encapsulates all of the information for describing the basic format properties of a stream of audio data.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
struct IOUserAudioStreamBasicDescription;
```

#### Discussion

This structure contains the information needed to describe any constant bit rate format that has channels that are the same size. For variable bit rate data and for constant bit rate data where the channels have unequal sizes, the type requires more data than this type provides. However, where applicable, the framework fills out the appropriate fields correctly for these kinds of formats using separate properties for the additional data.

In all fields, a value of `0` indicates that the field is either unknown, not applicable, or otherwise is inapproprate for the format. The [`mFormatFlags`](audiodriverkit/iouseraudiostreambasicdescription/mformatflags.md) field is an exception to this, where `0` is still a valid value for most formats.

In audio data a frame is one sample across all channels. In non-interleaved audio, the per frame fields identify one channel. In interleaved audio, the per-frame fields identify the set of `n` channels. In uncompressed audio, a packet is one frame, (`mFramesPerPacket == 1`). In compressed audio, a packet is an indivisible chunk of compressed data, for example an AAC packet contains 1024 sample frames.

## Topics

### Accessing the Sample Rate
- [mSampleRate](audiodriverkit/iouseraudiostreambasicdescription/msamplerate.md)
  The number of sample frames per second of the data in the stream.
### Identifying the Format
- [mFormatID](audiodriverkit/iouseraudiostreambasicdescription/mformatid.md)
  The audio format identifier indicating the general kind of data in the stream.
- [IOUserAudioFormatID](audiodriverkit/iouseraudioformatid.md)
  An enumeration of four character codes used to identify distinct audio data formats.
- [mFormatFlags](audiodriverkit/iouseraudiostreambasicdescription/mformatflags.md)
  Audio format flags for the stream’s format.
- [IOUserAudioFormatFlags](audiodriverkit/iouseraudioformatflags.md)
  Flag values that provide more information about the format used by an audio stream basic description.
### Accessing Packet and Frame Layout
- [mBytesPerPacket](audiodriverkit/iouseraudiostreambasicdescription/mbytesperpacket.md)
  The byte count in each packet of data.
- [mFramesPerPacket](audiodriverkit/iouseraudiostreambasicdescription/mframesperpacket.md)
  The number of sample frames in each packet of data.
- [mBytesPerFrame](audiodriverkit/iouseraudiostreambasicdescription/mbytesperframe.md)
  The byte count in each frame of data.
- [mChannelsPerFrame](audiodriverkit/iouseraudiostreambasicdescription/mchannelsperframe.md)
  The number of channels in each frame of data.
- [mBitsPerChannel](audiodriverkit/iouseraudiostreambasicdescription/mbitsperchannel.md)
  The number of bits of sample data for each channel in a frame of data.
### Infrequently Used Properties
- [mReserved](audiodriverkit/iouseraudiostreambasicdescription/mreserved.md)
  An unused field reserved for future use.

## See Also

- [SetCurrentStreamFormat](iouseraudiostream/setcurrentstreamformat.md)
  Sets the current stream format to a given audio stream basic description.
- [GetCurrentStreamFormat](iouseraudiostream/getcurrentstreamformat.md)
  Returns the current stream format, as an audio stream basic description.
- [SetAvailableStreamFormats](iouseraudiostream/setavailablestreamformats.md)
  Sets the available stream formats to an array of audio stream basic descriptions.
- [GetAvailableStreamFormats](iouseraudiostream/getavailablestreamformats.md)
  Returns the available stream formats as an array of audio stream basic descriptions.
- [GetNumberAvailableStreamFormats](iouseraudiostream/getnumberavailablestreamformats.md)
  Returns the number of available stream formats.
- [GetStreamDirection](iouseraudiostream/getstreamdirection.md)
  Gets the direction of the stream: input or output.
- [IOUserAudioStreamDirection](audiodriverkit/iouseraudiostreamdirection.md)
  A type representing the direction of audio flow.
- [SetStreamIsActive](iouseraudiostream/setstreamisactive.md)
  Sets a Boolean value that indicates whether the stream is active and doing I/O.
- [GetStreamIsActive](iouseraudiostream/getstreamisactive.md)
  Gets a value that indicates whether the stream is active and doing I/O.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiostreambasicdescription)*