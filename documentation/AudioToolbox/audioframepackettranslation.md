# AudioFramePacketTranslation

**Framework**: Audio Toolbox  
**Kind**: struct

A structure that specifies frame and packet translations.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFramePacketTranslation
```

#### Overview

A data structure used by the [`kAudioFilePropertyPacketToFrame`](kaudiofilepropertypackettoframe.md) and [`kAudioFilePropertyFrameToPacket`](kaudiofilepropertyframetopacket.md) properties.

## Topics

### Initializers
- [init()](audioframepackettranslation/init.md)
- [init(mFrame: Int64, mPacket: Int64, mFrameOffsetInPacket: UInt32)](audioframepackettranslation/init(mframe:mpacket:mframeoffsetinpacket:).md)
### Instance Properties
- [var mFrame: Int64](audioframepackettranslation/mframe.md)
  A frame number.
- [var mFrameOffsetInPacket: UInt32](audioframepackettranslation/mframeoffsetinpacket.md)
  A frame offset in a packet.
- [var mPacket: Int64](audioframepackettranslation/mpacket.md)
  A packet number.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct AudioBytePacketTranslationFlags](audiobytepackettranslationflags.md)
- [struct AudioFileFlags](audiofileflags.md)
- [struct AudioFileRegionFlags](audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [struct AudioFileStreamParseFlags](audiofilestreamparseflags.md)
- [struct AudioFileStreamPropertyFlags](audiofilestreampropertyflags.md)
- [struct AudioFileStreamSeekFlags](audiofilestreamseekflags.md)
- [typealias AudioFileID](audiofileid.md)
  An opaque data type that represents an audio file object.
- [typealias AudioFilePropertyID](audiofilepropertyid.md)
  An audio file property identifier.
- [struct AudioFile_SMPTE_Time](audiofile_smpte_time.md)
  A data structure for describing SMPTE (Society of Motion Picture and Television Engineers) time.
- [struct AudioFileMarker](audiofilemarker.md)
  Annotates a position in an audio file.
- [struct AudioFileMarkerList](audiofilemarkerlist.md)
  A list of markers associated with an audio file, including their SMPTE time type, the number of markers, and the markers themselves.
- [struct AudioFileRegion](audiofileregion.md)
  An audio file region specifies a segment of audio data.
- [struct AudioFileRegionList](audiofileregionlist.md)
  A list of the audio file regions in a file.
- [struct AudioBytePacketTranslation](audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](kaudiofilepropertypackettobyte.md) properties.
- [struct AudioFilePacketTableInfo](audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioframepackettranslation)*