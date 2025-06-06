# AudioFileRegion

**Framework**: Audio Toolbox  
**Kind**: struct

An audio file region specifies a segment of audio data.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFileRegion
```

#### Overview

Typically, a region consists of at least two markers designating the beginning and end of the segment. Other markers might define additional meta information such as sync point.

## Topics

### Initializers
- [init(mRegionID: UInt32, mName: Unmanaged<CFString>, mFlags: AudioFileRegionFlags, mNumberMarkers: UInt32, mMarkers: AudioFileMarker)](audiofileregion/init(mregionid:mname:mflags:mnumbermarkers:mmarkers:).md)
### Instance Properties
- [var mFlags: AudioFileRegionFlags](audiofileregion/mflags.md)
  Audio File Services region flags.
- [var mMarkers: AudioFileMarker](audiofileregion/mmarkers.md)
  An array of `mNumberMarkers` elements describing where the data in the region starts.
- [var mName: Unmanaged<CFString>](audiofileregion/mname.md)
  The name of the region.
- [var mNumberMarkers: UInt32](audiofileregion/mnumbermarkers.md)
  The number of markers in the array specified in the  `mMarkers` parameter.
- [var mRegionID: UInt32](audiofileregion/mregionid.md)
  A unique ID associated with the audio file region.

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
- [struct AudioFileRegionList](audiofileregionlist.md)
  A list of the audio file regions in a file.
- [struct AudioFramePacketTranslation](audioframepackettranslation.md)
  A structure that specifies frame and packet translations.
- [struct AudioBytePacketTranslation](audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](kaudiofilepropertypackettobyte.md) properties.
- [struct AudioFilePacketTableInfo](audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileregion)*