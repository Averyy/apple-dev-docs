# AudioFileMarkerList

**Framework**: Audio Toolbox  
**Kind**: struct

A list of markers associated with an audio file, including their SMPTE time type, the number of markers, and the markers themselves.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFileMarkerList
```

## Topics

### Initializers
- [init()](audiofilemarkerlist/init.md)
- [init(mSMPTE_TimeType: UInt32, mNumberMarkers: UInt32, mMarkers: AudioFileMarker)](audiofilemarkerlist/init(msmpte_timetype:mnumbermarkers:mmarkers:).md)
### Instance Properties
- [var mMarkers: AudioFileMarker](audiofilemarkerlist/mmarkers.md)
  An array of `mNumberMarkers` elements, each of which is an audio file marker.
- [var mNumberMarkers: UInt32](audiofilemarkerlist/mnumbermarkers.md)
  The number of markers in the list.
- [var mSMPTE_TimeType: UInt32](audiofilemarkerlist/msmpte_timetype.md)
  The SMPTE time type of the whole list of markers in an audio file.

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
- [struct AudioFileMarker](audiofilemarker.md)
  Annotates a position in an audio file.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilemarkerlist)*