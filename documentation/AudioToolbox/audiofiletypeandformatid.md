# AudioFileTypeAndFormatID

**Framework**: Audio Toolbox  
**Kind**: struct

A specifier for the constant[`kAudioFileGlobalInfo_AvailableStreamDescriptionsForFormat`](kaudiofileglobalinfo_availablestreamdescriptionsforformat.md).

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioFileTypeAndFormatID
```

#### Overview

This structure specifies a desired audio file type and data format ID so you can obtain a list of stream descriptions of available formats.

## Topics

### Initializers
- [init()](audiofiletypeandformatid/init.md)
- [init(mFileType: AudioFileTypeID, mFormatID: UInt32)](audiofiletypeandformatid/init(mfiletype:mformatid:).md)
### Instance Properties
- [var mFileType: AudioFileTypeID](audiofiletypeandformatid/mfiletype.md)
  A four-character code for the file type.
- [var mFormatID: UInt32](audiofiletypeandformatid/mformatid.md)
  A four-character code for the format ID such as `kAudioFormatLinearPCM`, `kAudioFormatMPEG4AAC`, and so forth. (See the `AudioFormat.h` header file for declarations.)

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofiletypeandformatid)*