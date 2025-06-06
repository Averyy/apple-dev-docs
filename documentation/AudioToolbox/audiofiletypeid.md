# AudioFileTypeID

**Framework**: Audio Toolbox  
**Kind**: typealias

Operating system constants that indicate the type of file to be written or a hint about what type of file to expect from data provided.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
typealias AudioFileTypeID = UInt32
```

## Topics

### Constants
- [var kAudioFileAIFFType: AudioFileTypeID](kaudiofileaifftype.md)
  An Audio Interchange File Format (AIFF) file.
- [var kAudioFileAIFCType: AudioFileTypeID](kaudiofileaifctype.md)
  An Audio Interchange File Format Compressed (AIFF-C) file.
- [var kAudioFileWAVEType: AudioFileTypeID](kaudiofilewavetype.md)
  A Microsoft WAVE file.
- [var kAudioFileSoundDesigner2Type: AudioFileTypeID](kaudiofilesounddesigner2type.md)
  A Sound Designer II file.
- [var kAudioFileNextType: AudioFileTypeID](kaudiofilenexttype.md)
  A NeXT or Sun Microsystems file.
- [var kAudioFileMP3Type: AudioFileTypeID](kaudiofilemp3type.md)
  An MPEG Audio Layer 3 (`.mp3`) file.
- [var kAudioFileMP2Type: AudioFileTypeID](kaudiofilemp2type.md)
  An MPEG Audio Layer 2 (`.mp2`) file.
- [var kAudioFileMP1Type: AudioFileTypeID](kaudiofilemp1type.md)
  An MPEG Audio Layer 1 (`.mp1`) file.
- [var kAudioFileAC3Type: AudioFileTypeID](kaudiofileac3type.md)
  An AC-3 file.
- [var kAudioFileAAC_ADTSType: AudioFileTypeID](kaudiofileaac_adtstype.md)
  An Advanced Audio Coding (AAC) Audio Data Transport Stream (ADTS) file.
- [var kAudioFileMPEG4Type: AudioFileTypeID](kaudiofilempeg4type.md)
  An MPEG 4 file.
- [var kAudioFileM4AType: AudioFileTypeID](kaudiofilem4atype.md)
  An M4A file.
- [var kAudioFileCAFType: AudioFileTypeID](kaudiofilecaftype.md)
  A Core Audio File Format file.
- [var kAudioFile3GPType: AudioFileTypeID](kaudiofile3gptype.md)
  A 3GPP file, suitable for video content on GSM mobile phones.
- [var kAudioFile3GP2Type: AudioFileTypeID](kaudiofile3gp2type.md)
  A 3GPP2 file, suitable for video content on CDMA mobile phones.
- [var kAudioFileAMRType: AudioFileTypeID](kaudiofileamrtype.md)
  An AMR (Adaptive Multi-Rate) file suitable for compressed speech.

## See Also

- [Audio File Creation Flags](audio_file_creation_flags.md)
  Flags to set when creating an audio file.
- [enum AudioFilePermissions](audiofilepermissions.md)
  Flags for use when opening an audio file.
- [Audio File Loop Direction Constants](1576494-audio-file-loop-direction-consta.md)
  The playback direction of a looped segment of an audio file.
- [Audio File Marker Types](1576492-audio-file-marker-types.md)
  A type of marker within a file used in the `mType` field of the [`AudioFileMarker`](audiofilemarker.md) structure.
- [struct AudioFileRegionFlags](audiofileregionflags.md)
  Flags that specify a playback direction for an audio file region structure.
- [Audio File Packet Translation Flags](audio_file_packet_translation_flags.md)
  Flags specified in a packet translation structure.
- [Info String Keys](info-string-keys.md)
  Key values of properties to get and set using Audio File Services functions and provide a common way to get the same information out of several different kinds of files.
- [Audio File Properties](1576499-audio-file-properties.md)
  Properties used by the functions described in getting and setting pieces of data in audio files. See Working with Global Information for details.
- [Audio File Global Info Properties](1576495-audio-file-global-info-propertie.md)
  Access these properties using the functions described in Working with Global Information.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audiofiletypeid)*