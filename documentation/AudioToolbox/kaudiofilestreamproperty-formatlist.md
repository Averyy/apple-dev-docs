# kAudioFileStreamProperty_FormatList

**Framework**: Audio Toolbox  
**Kind**: var

To support formats such as AAC with SBR where an encoded data stream can be decoded to multiple destination formats, this property returns an array of `AudioFormatListItem` structures (declared in `AudioFormat.h`)—one for each of the destination formats. The default behavior is to return an `AudioFormatListItem` structure that has the same `AudioStreamBasicDescription` structure as that returned by the [`kAudioFileStreamProperty_DataFormat`](kaudiofilestreamproperty_dataformat.md) property.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioFileStreamProperty_FormatList: AudioFileStreamPropertyID { get }
```

## See Also

- [var kAudioFileStreamProperty_ReadyToProducePackets: AudioFileStreamPropertyID](kaudiofilestreamproperty_readytoproducepackets.md)
- [var kAudioFileStreamProperty_FileFormat: AudioFileStreamPropertyID](kaudiofilestreamproperty_fileformat.md)
  A four-character code that identifies the audio data format.
- [var kAudioFileStreamProperty_DataFormat: AudioFileStreamPropertyID](kaudiofilestreamproperty_dataformat.md)
  An `AudioStreamBasicDescription` structure describing the format of the audio data in the stream.
- [var kAudioFileStreamProperty_MagicCookieData: AudioFileStreamPropertyID](kaudiofilestreamproperty_magiccookiedata.md)
  A pointer (`void *`) to a magic cookie. For audio file types that require a magic cookie before packets can be written to a file, you should get this property value before calling the [`AudioFileWriteBytes(_:_:_:_:_:)`](audiofilewritebytes(_:_:_:_:_:).md) or [`AudioFileWritePackets(_:_:_:_:_:_:_:)`](audiofilewritepackets(_:_:_:_:_:_:_:).md) functions.
- [var kAudioFileStreamProperty_AudioDataByteCount: AudioFileStreamPropertyID](kaudiofilestreamproperty_audiodatabytecount.md)
  A `UInt64` value indicating the number of bytes of audio data in the streamed file. This property is valid only if the number of bytes for the entire stream is known from the data parsed in the header. For some kinds of streams this property may have no value.
- [var kAudioFileStreamProperty_AudioDataPacketCount: AudioFileStreamPropertyID](kaudiofilestreamproperty_audiodatapacketcount.md)
  A `UInt64` value indicating the number of packets of audio data in the streamed file.
- [var kAudioFileStreamProperty_MaximumPacketSize: AudioFileStreamPropertyID](kaudiofilestreamproperty_maximumpacketsize.md)
  A `UInt32` value indicating the maximum packet size of the data in the streamed file.
- [var kAudioFileStreamProperty_DataOffset: AudioFileStreamPropertyID](kaudiofilestreamproperty_dataoffset.md)
  An `SInt64` value indicating the byte offset in the streamed file at which the audio data starts.
- [var kAudioFileStreamProperty_ChannelLayout: AudioFileStreamPropertyID](kaudiofilestreamproperty_channellayout.md)
  An `AudioChannelLayout` structure.
- [var kAudioFileStreamProperty_PacketToFrame: AudioFileStreamPropertyID](kaudiofilestreamproperty_packettoframe.md)
  Obtains the frame number corresponding to a packet number.
- [var kAudioFileStreamProperty_FrameToPacket: AudioFileStreamPropertyID](kaudiofilestreamproperty_frametopacket.md)
  Obtains the packet number corresponding to a frame number.
- [var kAudioFileStreamProperty_PacketToByte: AudioFileStreamPropertyID](kaudiofilestreamproperty_packettobyte.md)
  Obtains the byte number corresponding to a packet number. Pass an `AudioBytePacketTranslation` structure with the `mPacket` field filled in, and a value is returned in the `mByte` field. The `mByteOffsetInPacket` field of the `AudioBytePacketTranslation` structure is ignored. If the `mByte` value is an estimate, then the `kBytePacketTranslationFlag_IsEstimate` value will be set in the `mFlags` field.
- [var kAudioFileStreamProperty_ByteToPacket: AudioFileStreamPropertyID](kaudiofilestreamproperty_bytetopacket.md)
  Obtains the packet number corresponding to a byte number. Pass an `AudioBytePacketTranslation` structure with the `mByte` field filled in, and values are returned in the `mPacket` and `mByteOffsetInPacket` fields. If the `mPacket` value is an estimate, then the `kBytePacketTranslationFlag_IsEstimate` value will be set in the `mFlags` field.
- [var kAudioFileStreamProperty_PacketTableInfo: AudioFileStreamPropertyID](kaudiofilestreamproperty_packettableinfo.md)
  An `AudioFilePacketTableInfo` structure.
- [var kAudioFileStreamProperty_PacketSizeUpperBound: AudioFileStreamPropertyID](kaudiofilestreamproperty_packetsizeupperbound.md)
  A `UInt32` value indicating the theoretical maximum packet size in the streamed file. This value is useful for determining minimum buffer sizes, for example.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiofilestreamproperty_formatlist)*