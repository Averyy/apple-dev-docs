# AudioBytePacketTranslation

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

A data structure used by the [`kAudioFilePropertyByteToPacket`](./kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](./kaudiofilepropertypackettobyte.md) properties.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AudioBytePacketTranslation
```

```c
struct AudioBytePacketTranslation;
```

## Topics

### Initializers
- [init()](./audiobytepackettranslation/init%28%29.md)
- [init(mByte: Int64, mPacket: Int64, mByteOffsetInPacket: UInt32, mFlags: AudioBytePacketTranslationFlags)](./audiobytepackettranslation/init%28mbyte,mpacket,mbyteoffsetinpacket,mflags%29.md)
### Instance Properties
- [var mByte: Int64](./audiobytepackettranslation/mbyte.md)
  A byte number.
- [var mByteOffsetInPacket: UInt32](./audiobytepackettranslation/mbyteoffsetinpacket.md)
  A byte offset in a packet.
- [var mFlags: AudioBytePacketTranslationFlags](./audiobytepackettranslation/mflags.md)
  A translation flag value.
- [var mPacket: Int64](./audiobytepackettranslation/mpacket.md)
  A packet number.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Data Types
- [struct AudioBytePacketTranslationFlags](./audiobytepackettranslationflags.md)
- [struct AudioFileFlags](./audiofileflags.md)
- [struct AudioFileRegionFlags](./audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [struct AudioFileStreamParseFlags](./audiofilestreamparseflags.md)
- [struct AudioFileStreamPropertyFlags](./audiofilestreampropertyflags.md)
- [struct AudioFileStreamSeekFlags](./audiofilestreamseekflags.md)
- [typealias AudioFileID](./audiofileid.md)
  An opaque data type that represents an audio file object.
- [typealias AudioFilePropertyID](./audiofilepropertyid.md)
  An audio file property identifier.
- [struct AudioFile_SMPTE_Time](./audiofile_smpte_time.md)
  A data structure for describing SMPTE (Society of Motion Picture and Television Engineers) time.
- [struct AudioFileMarker](./audiofilemarker.md)
  Annotates a position in an audio file.
- [struct AudioFileMarkerList](./audiofilemarkerlist.md)
  A list of markers associated with an audio file, including their SMPTE time type, the number of markers, and the markers themselves.
- [struct AudioFileRegion](./audiofileregion.md)
  An audio file region specifies a segment of audio data.
- [struct AudioFileRegionList](./audiofileregionlist.md)
  A list of the audio file regions in a file.
- [struct AudioFramePacketTranslation](./audioframepackettranslation.md)
  A structure that specifies frame and packet translations.
- [struct AudioFilePacketTableInfo](./audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.
- [AudioFileFDFTable](./audiofilefdftable.md)
- [AudioFileFDFTableExtended](./audiofilefdftableextended.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiobytepackettranslation)*