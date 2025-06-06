# kAudioFilePropertyID3Tag

**Framework**: Audio Toolbox  
**Kind**: var

A `void*` value pointing to memory set up by your application to contain a fully formatted ID3 tag.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioFilePropertyID3Tag: AudioFilePropertyID { get }
```

#### Discussion

When setting, this property must be set before calling the [`AudioFileWritePackets(_:_:_:_:_:_:_:)`](audiofilewritepackets(_:_:_:_:_:_:_:).md) function. This property is gettable and settable when using ID3 version 2. It is gettable only for version ID3 version 1. A sound file’s ID3 tag itself is not manipulated when getting or setting this property.

## See Also

- [var kAudioFilePropertyFileFormat: AudioFilePropertyID](kaudiofilepropertyfileformat.md)
  The format of the audio data file.
- [var kAudioFilePropertyDataFormat: AudioFilePropertyID](kaudiofilepropertydataformat.md)
  An audio stream basic description containing the format of the audio data.
- [var kAudioFilePropertyFormatList: AudioFilePropertyID](kaudiofilepropertyformatlist.md)
  To support formats such as AAC SBR in which an encoded data stream can be decoded to multiple destination formats, this property’s value is an array of audio format list item values (declared in `AudioFormat.h`) of those formats. Typically, this is an audio format list item with the same audio stream basic description in the `kAudioFilePropertyDataFormat` property.
- [var kAudioFilePropertyIsOptimized: AudioFilePropertyID](kaudiofilepropertyisoptimized.md)
  Indicates whether a designated audio file has been optimized, that is, ready to start having sound data written to it. A value of `0` indicates the file needs to be optimized. A value of `1` indicates the file is currently optimized.
- [var kAudioFilePropertyMagicCookieData: AudioFilePropertyID](kaudiofilepropertymagiccookiedata.md)
  A pointer to memory set up by the caller. Some file types require that a magic cookie be provided before packets can be written to an audio file. Set this property before you call [`AudioFileWriteBytes(_:_:_:_:_:)`](audiofilewritebytes(_:_:_:_:_:).md) or [`AudioFileWritePackets(_:_:_:_:_:_:_:)`](audiofilewritepackets(_:_:_:_:_:_:_:).md) if a magic cookie exists.
- [var kAudioFilePropertyAudioDataByteCount: AudioFilePropertyID](kaudiofilepropertyaudiodatabytecount.md)
  Indicates the number of bytes of audio data in the designated file.
- [var kAudioFilePropertyAudioDataPacketCount: AudioFilePropertyID](kaudiofilepropertyaudiodatapacketcount.md)
  Indicates the number of packets of audio data in the designated file.
- [var kAudioFilePropertyMaximumPacketSize: AudioFilePropertyID](kaudiofilepropertymaximumpacketsize.md)
  Indicates the maximum size of a packet for the data in the designated file.
- [var kAudioFilePropertyDataOffset: AudioFilePropertyID](kaudiofilepropertydataoffset.md)
  Indicates the byte offset in the file of the designated audio data.
- [var kAudioFilePropertyChannelLayout: AudioFilePropertyID](kaudiofilepropertychannellayout.md)
  An audio channel layout structure.
- [var kAudioFilePropertyDeferSizeUpdates: AudioFilePropertyID](kaudiofilepropertydefersizeupdates.md)
  The default value (`0`) always updates header. If set to `1`, updating the files sizes in the header is not performed every time data is written. Instead, the updating is deferred until the file has been read, optimized, or closed. This process is more efficient, but not as safe. If an application crashes before the size has been updated, the file might not be readable.
- [var kAudioFilePropertyDataFormatName: AudioFilePropertyID](kaudiofilepropertydataformatname.md)
  This constant is deprecated in macOS 10.5 and later. Do not use. Instead, use `kAudioFormatProperty_FormatName` (declared in the `AudioFormat.h` header file).
- [var kAudioFilePropertyMarkerList: AudioFilePropertyID](kaudiofilepropertymarkerlist.md)
  A list of audio file markers defined in the file.
- [var kAudioFilePropertyRegionList: AudioFilePropertyID](kaudiofilepropertyregionlist.md)
  The list of audio file region values defined in the file.
- [var kAudioFilePropertyPacketToFrame: AudioFilePropertyID](kaudiofilepropertypackettoframe.md)
  Passes an audio frame packet translation structure with the `mPacket` field filled out and returns the `mFrame` field. The `mFrameOffsetInPacket` field is ignored.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudiofilepropertyid3tag)*