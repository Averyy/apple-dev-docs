# AudioFileRegionList

**Framework**: Audio Toolbox  
**Kind**: struct

A list of the audio file regions in a file.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFileRegionList
```

#### Overview

This structure is used by the [`kAudioFilePropertyRegionList`](kaudiofilepropertyregionlist.md) property.

## Topics

### Initializers
- [init()](audiofileregionlist/init.md)
- [init(mSMPTE_TimeType: UInt32, mNumberRegions: UInt32, mRegions: AudioFileRegion)](audiofileregionlist/init(msmpte_timetype:mnumberregions:mregions:).md)
### Instance Properties
- [var mNumberRegions: UInt32](audiofileregionlist/mnumberregions.md)
  The number of regions in the list specified in the  `mRegions` parameter.
- [var mRegions: AudioFileRegion](audiofileregionlist/mregions.md)
  A variable length array of audio file regions.
- [var mSMPTE_TimeType: UInt32](audiofileregionlist/msmpte_timetype.md)
  The SMPTE timing scheme used in the file. See Core Audio’s `CAFFile.h` header file for the values used here. For more information, see .

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
- [struct AudioFileMarkerList](audiofilemarkerlist.md)
  A list of markers associated with an audio file, including their SMPTE time type, the number of markers, and the markers themselves.
- [struct AudioFileRegion](audiofileregion.md)
  An audio file region specifies a segment of audio data.
- [struct AudioFramePacketTranslation](audioframepackettranslation.md)
  A structure that specifies frame and packet translations.
- [struct AudioBytePacketTranslation](audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](kaudiofilepropertypackettobyte.md) properties.
- [struct AudioFilePacketTableInfo](audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileregionlist)*