# Audio Format Services

**Framework**: Audio Toolbox

Access information about audio formats and codecs.

#### Overview

This document describes Audio Format Services, a C interface for obtaining information about audio formats and codecs.

## Topics

### Audio Format Services Functions
- [func AudioFormatGetProperty(AudioFormatPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>?, UnsafeMutableRawPointer?) -> OSStatus](audioformatgetproperty(_:_:_:_:_:).md)
  Gets the value of an audio format property.
- [func AudioFormatGetPropertyInfo(AudioFormatPropertyID, UInt32, UnsafeRawPointer?, UnsafeMutablePointer<UInt32>) -> OSStatus](audioformatgetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio format property.
### Data Types
- [struct AudioBalanceFade](audiobalancefade.md)
  Describes audio left/right balance and front/back fade values.
- [struct AudioFormatInfo](audioformatinfo.md)
  A structure that specifies an audio format.
- [struct AudioFormatListItem](../CoreAudioTypes/AudioFormatListItem.md)
- [struct AudioPanningInfo](audiopanninginfo.md)
  Audio panning information.
- [struct ExtendedAudioFormatInfo](extendedaudioformatinfo.md)
  A specifier for the [`kAudioFormatProperty_FormatList`](kaudioformatproperty_formatlist.md) property, including the codec to use.
- [typealias AudioFormatPropertyID](audioformatpropertyid.md)
  A type for four-char codes for audio format property identifiers.
### Constants
- [enum AudioBalanceFadeType](audiobalancefadetype.md)
  Identifiers for audio balance fade types.
- [Audio Format Property Identifiers](1577853-audio-format-property-identifier.md)
  Constants for use with the [`AudioFormatGetPropertyInfo(_:_:_:_:)`](audioformatgetpropertyinfo(_:_:_:_:).md) and [`AudioFormatGetProperty(_:_:_:_:_:)`](audioformatgetproperty(_:_:_:_:_:).md) functions.
- [Audio Codec Component Constants](1494086-audio-codec-component-constants.md)
  Audio codec component types.
- [Audio Codec Manufacturer and Implementation Types](1620448-audio-codec-manufacturer-and-imp.md)
  Identifiers for audio codec manufacturers and implementation types.
- [enum AudioPanningMode](audiopanningmode.md)
  Identifiers for audio panning algorithms.
### Result Codes
- [Audio Format Error Codes](1577851-audio-format-error-codes.md)
- [var kAudioFormatUnspecifiedError: OSStatus](kaudioformatunspecifiederror.md)
  An unspecified error.
- [var kAudioFormatUnsupportedPropertyError: OSStatus](kaudioformatunsupportedpropertyerror.md)
  The specified property is not supported.
- [var kAudioFormatBadPropertySizeError: OSStatus](kaudioformatbadpropertysizeerror.md)
- [var kAudioFormatBadSpecifierSizeError: OSStatus](kaudioformatbadspecifiersizeerror.md)
- [var kAudioFormatUnsupportedDataFormatError: OSStatus](kaudioformatunsupporteddataformaterror.md)
  The playback data format is unsupported (declared in `AudioFormat.h`).
- [var kAudioFormatUnknownFormatError: OSStatus](kaudioformatunknownformaterror.md)
  The specified data format is not a known format.

## See Also

- [Audio File Services](audio-file-services.md)
  Read or write a variety of audio data to or from disk or a memory buffer.
- [Extended Audio File Services](extended-audio-file-services.md)
  Read and write compressed files and linear PCM audio files using a simplified interface.
- [Audio File Stream Services](audio-file-stream-services.md)
  Parse streamed audio files as the data arrives on the user’s computer.
- [Audio File Components](audio-file-components.md)
  Get information about audio file formats, and about files containing audio data.
- [Core Audio File Format](core-audio-file-format.md)
  Parse the structure of Core Audio files.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-format-services)*