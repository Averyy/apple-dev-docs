# Core Audio Types

**Framework**: Core Audio Types  
**Kind**: module

Use specialized data types to interact with audio streams, complex buffers, and audiovisual timestamps.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS 1.0+
- watchOS 6.0+

#### Overview

The Core Audio Types framework declares common data types and constants that other Core Audio interfaces use. This framework also includes several convenience functions.

If you’re unfamiliar with the specialized terminology regarding the manipulation of audio data, refer to [`Core Audio Glossary`](https://developer.apple.comhttps://developer.apple.com/library/archive/documentation/MusicAudio/Reference/CoreAudioGlossary/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004453).

## Topics

### Buffers
- [struct AudioBuffer](audiobuffer.md)
  A structure that holds a buffer of audio data.
- [struct AudioBufferList](audiobufferlist.md)
  A structure that stores a variable-length array of audio buffers.
### Channels
- [struct AudioChannelDescription](audiochanneldescription.md)
  A structure that describes a channel of audio data.
- [struct AudioChannelLayout](audiochannellayout.md)
  A structure that specifies a channel layout in a file or in hardware.
### Codecs
- [struct AudioClassDescription](audioclassdescription.md)
  A structure that describes an audio codec.
### Audio Time
- [struct AudioTimeStamp](audiotimestamp.md)
  A structure that represents a timestamp value.
- [struct AudioTimeStampFlags](audiotimestampflags.md)
  A structure that represents flags for a timestamp.
### SMPTE Time
- [struct SMPTETime](smptetime.md)
  A structure that defines an SMPTE time value.
- [struct SMPTETimeFlags](smptetimeflags.md)
  A structure that defines SMPTE time flags.
- [enum SMPTETimeType](smptetimetype.md)
  Constants that define SMPTE time types.
### Values
- [struct AudioValueRange](audiovaluerange.md)
  A structure that represents a continuous range of values.
- [struct AudioValueTranslation](audiovaluetranslation.md)
  A structure that stores buffers to use in translation operations.
### Streams
- [struct AudioStreamBasicDescription](audiostreambasicdescription.md)
  A format specification for an audio stream.
- [struct AudioStreamPacketDescription](audiostreampacketdescription.md)
  A value that describes a packet in a buffer of audio data.
- [typealias AudioFormatFlags](audioformatflags.md)
  A type definition for audio format flags.
- [Audio Format Flags](audio-format-flags.md)
  Commonly used combinations of data format flags for an audio stream description.
- [typealias AudioFormatID](audioformatid.md)
  A type definition for audio format identifiers.
- [Audio Format Identifiers](audio-format-identifiers.md)
  Identifiers for supported audio formats.
- [let kAudioStreamAnyRate: Float64](kaudiostreamanyrate.md)
  A value that indicates that an audio stream can use any sample rate.
- [enum MPEG4ObjectID](mpeg4objectid.md)
  Constants that define the type of MPEG-4 audio data.
### Common Types
- [typealias AVAudioInteger](avaudiointeger.md)
  An integer type for audio operations.
- [typealias AVAudioUInteger](avaudiouinteger.md)
  An unsigned integer type for audio operations.
- [typealias AudioSessionID](audiosessionid.md)
  A unique identifier of an audio session.
- [var kAudioUnitSampleFractionBits: Int32](kaudiounitsamplefractionbits.md)
  The number of fractional bits in fixed-point samples.
- [var COREAUDIOTYPES_VERSION: Int32](coreaudiotypes_version.md)
  A value that represents the Core Audio Types version.
- [typealias AudioSampleType](audiosampletype.md)
  The canonical audio data sample type for input and output.
- [typealias AudioUnitSampleType](audiounitsampletype.md)
  The canonical audio data sample type for audio processing.
- [struct AudioFormatListItem](audioformatlistitem.md)
### Errors
- [var kAudio_ParamError: OSStatus](kaudio_paramerror.md)
  An error in the parameter list of the function.
- [var kAudio_MemFullError: OSStatus](kaudio_memfullerror.md)
  An error that indicates that the heap zone is full.
- [var kAudio_FileNotFoundError: OSStatus](kaudio_filenotfounderror.md)
  An error that indicates the file wasn’t found.
- [var kAudio_UnimplementedError: OSStatus](kaudio_unimplementederror.md)
  An error that indicates the app called an unimplemented system function.
### Reference
- [CoreAudioTypes Enumerations](coreaudiotypes-enumerations.md)
### Variables
- [var kAudioChannelLayoutTag_Ogg_3_0: AudioChannelLayoutTag](kaudiochannellayouttag_ogg_3_0.md)
- [var kAudioChannelLayoutTag_Ogg_4_0: AudioChannelLayoutTag](kaudiochannellayouttag_ogg_4_0.md)
- [var kAudioChannelLayoutTag_Ogg_5_0: AudioChannelLayoutTag](kaudiochannellayouttag_ogg_5_0.md)
- [var kAudioChannelLayoutTag_Ogg_5_1: AudioChannelLayoutTag](kaudiochannellayouttag_ogg_5_1.md)
- [var kAudioChannelLayoutTag_Ogg_6_1: AudioChannelLayoutTag](kaudiochannellayouttag_ogg_6_1.md)
- [var kAudioChannelLayoutTag_Ogg_7_1: AudioChannelLayoutTag](kaudiochannellayouttag_ogg_7_1.md)
- [var kAudioFormatAPAC: AudioFormatID](kaudioformatapac.md)
- [var kAudio_BadFilePathError: OSStatus](kaudio_badfilepatherror.md)
- [var kAudio_FilePermissionError: OSStatus](kaudio_filepermissionerror.md)
- [var kAudio_NoError: OSStatus](kaudio_noerror.md)
- [var kAudio_TooManyFilesOpenError: OSStatus](kaudio_toomanyfilesopenerror.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/CoreAudioTypes)*