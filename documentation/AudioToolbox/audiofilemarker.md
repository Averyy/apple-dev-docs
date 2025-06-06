# AudioFileMarker

**Framework**: Audio Toolbox  
**Kind**: struct

Annotates a position in an audio file.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFileMarker
```

## Topics

### Initializers
- [init()](audiofilemarker/init.md)
- [init(mFramePosition: Float64, mName: Unmanaged<CFString>?, mMarkerID: Int32, mSMPTETime: AudioFile_SMPTE_Time, mType: UInt32, mReserved: UInt16, mChannel: UInt16)](audiofilemarker/init(mframeposition:mname:mmarkerid:msmptetime:mtype:mreserved:mchannel:).md)
### Instance Properties
- [var mChannel: UInt16](audiofilemarker/mchannel.md)
  The channel number referred to by the marker. Set to `0` if the marker applies to all channels.
- [var mFramePosition: Float64](audiofilemarker/mframeposition.md)
  The frame in the file, counting from the start of the audio data.
- [var mMarkerID: Int32](audiofilemarker/mmarkerid.md)
  A unique ID for the marker.
- [var mName: Unmanaged<CFString>?](audiofilemarker/mname.md)
  The name of the marker.
- [var mReserved: UInt16](audiofilemarker/mreserved.md)
  A reserved field. Set to `0`.
- [var mSMPTETime: AudioFile_SMPTE_Time](audiofilemarker/msmptetime.md)
  The SMPTE time for this marker.
- [var mType: UInt32](audiofilemarker/mtype.md)
  The marker type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

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
- [struct AudioFileMarkerList](audiofilemarkerlist.md)
  A list of markers associated with an audio file, including their SMPTE time type, the number of markers, and the markers themselves.
- [struct AudioFileRegion](audiofileregion.md)
  An audio file region specifies a segment of audio data.
- [struct AudioFileRegionList](audiofileregionlist.md)
  A list of the audio file regions in a file.
- [struct AudioFramePacketTranslation](audioframepackettranslation.md)
  A structure that specifies frame and packet translations.
- [struct AudioBytePacketTranslation](audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](kaudiofilepropertypackettobyte.md) properties.
- [struct AudioFilePacketTableInfo](audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilemarker)*