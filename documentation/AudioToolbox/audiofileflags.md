# AudioFileFlags

**Framework**: Audio Toolbox  
**Kind**: struct  
**Role**: Structure

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS

## Declaration

```swift
struct AudioFileFlags
```

```c
enum AudioFileFlags : UInt32;
```

## Topics

### Flags
- [static var dontPageAlignAudioData: AudioFileFlags](./audiofileflags/dontpagealignaudiodata.md)
  Typically, the audio data in a file is page aligned. To make reading the file data as fast as possible, you can use page-aligned data to take advantage of optimized code paths in the file system. However, when space is at a premium, you might want to avoid the additional padding required to attain alignment. To do so, set this flag when calling [`AudioFileCreate`](./audiofilecreate.md) or [`AudioFileCreateWithURL(_:_:_:_:_:)`](./audiofilecreatewithurl%28_,_,_,_,_%29.md).
- [static var eraseFile: AudioFileFlags](./audiofileflags/erasefile.md)
### Initializers
- [init(rawValue: UInt32)](./audiofileflags/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Data Types
- [struct AudioBytePacketTranslationFlags](./audiobytepackettranslationflags.md)
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
- [struct AudioBytePacketTranslation](./audiobytepackettranslation.md)
  A data structure used by the [`kAudioFilePropertyByteToPacket`](./kaudiofilepropertybytetopacket.md) and [`kAudioFilePropertyPacketToByte`](./kaudiofilepropertypackettobyte.md) properties.
- [struct AudioFilePacketTableInfo](./audiofilepackettableinfo.md)
  Contains information about the number of valid frames in a file and where they begin and end.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofileflags)*