# AudioFilePacketTableInfo

**Framework**: Audio Toolbox  
**Kind**: struct

Contains information about the number of valid frames in a file and where they begin and end.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFilePacketTableInfo
```

#### Overview

Some data formats might have packets with contents that are not completely valid, but that represent priming or remainder frames not intended for playback. For example, a file with 100 packets of AAC is nominally 1024 * 100 = 102400 frames of data. However, the first 2112 frames might be priming frames.

A number of remainder frames might be added to pad out to a full packet of 1024 frames. Discard the priming and remainder frames.

The total number of packets in the file times the frames per packet (or counting each packet’s frames individually for a variable frames per packet format) minus `mPrimingFrames`, minus `mRemainderFrames`, should equal `mNumberValidFrames`.

## Topics

### Initializers
- [init()](audiofilepackettableinfo/init.md)
- [init(mNumberValidFrames: Int64, mPrimingFrames: Int32, mRemainderFrames: Int32)](audiofilepackettableinfo/init(mnumbervalidframes:mprimingframes:mremainderframes:).md)
### Instance Properties
- [var mNumberValidFrames: Int64](audiofilepackettableinfo/mnumbervalidframes.md)
  The number of valid frames in the file.
- [var mPrimingFrames: Int32](audiofilepackettableinfo/mprimingframes.md)
  The number of invalid frames at the beginning of the file.
- [var mRemainderFrames: Int32](audiofilepackettableinfo/mremainderframes.md)
  The number of invalid frames at the end of the file.

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
- [struct AudioFramePacketTranslation](audioframepackettranslation.md)
  A structure that specifies frame and packet translations.
- [struct AudioBytePacketTranslation](audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](kaudiofilepropertypackettobyte.md) properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofilepackettableinfo)*