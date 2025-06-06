# AudioIndependentPacketTranslation

**Framework**: Audio Toolbox  
**Kind**: struct

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
struct AudioIndependentPacketTranslation
```

## Topics

### Initializers
- [init()](audioindependentpackettranslation/init.md)
- [init(mPacket: Int64, mIndependentlyDecodablePacket: Int64)](audioindependentpackettranslation/init(mpacket:mindependentlydecodablepacket:).md)
### Instance Properties
- [var mIndependentlyDecodablePacket: Int64](audioindependentpackettranslation/mindependentlydecodablepacket.md)
- [var mPacket: Int64](audioindependentpackettranslation/mpacket.md)

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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audioindependentpackettranslation)*