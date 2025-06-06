# AudioFileRegionFlags

**Framework**: Audio Toolbox  
**Kind**: struct

Flags that specify a playback direction for an audio file region structure.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFileRegionFlags
```

#### Overview

You can set one or more of these flags. For example, if both `kAudioFileRegionFlag_LoopEnable` and `kAudioFileRegionFlag_PlayForward` are set, the region plays as a forward loop. If only  `kAudioFileRegionFlag_PlayForward` is set, the region is played forward once. if both `kAudioFileRegionFlag_PlayForward` and `kAudioFileRegionFlag_PlayBackward` are set, the region plays forward then backward, then forward.

## Topics

### Constants
- [static var loopEnable: AudioFileRegionFlags](audiofileregionflags/loopenable.md)
  If set, the region is looped. You must set one or both of the remaining flags must also be set for the region to be looped.
- [static var playBackward: AudioFileRegionFlags](audiofileregionflags/playbackward.md)
  If set, the region is played backward.
- [static var playForward: AudioFileRegionFlags](audiofileregionflags/playforward.md)
  If set, the region is played forward.
### Initializers
- [init(rawValue: UInt32)](audiofileregionflags/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [struct AudioBytePacketTranslationFlags](audiobytepackettranslationflags.md)
- [struct AudioFileFlags](audiofileflags.md)
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
- [struct AudioFramePacketTranslation](audioframepackettranslation.md)
  A structure that specifies frame and packet translations.
- [struct AudioBytePacketTranslation](audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](kaudiofilepropertypackettobyte.md) properties.
- [struct AudioFilePacketTableInfo](audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileregionflags)*