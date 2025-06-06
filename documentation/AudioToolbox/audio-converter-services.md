# Audio Converter Services

**Framework**: Audio Toolbox

Convert between linear PCM audio formats, and between linear PCM and compressed formats.

#### Overview

Audio converter objects convert between various linear PCM audio formats. They can also convert between linear PCM and compressed formats. Supported transformations include the following:

- PCM bit depth
- PCM sample rate
- PCM floating point to and from PCM integer
- PCM interleaved to and from PCM deinterleaved
- PCM to and from compressed formats

A single audio converter may perform more than one of the listed transformations.

## Topics

### Managing Audio Converter Objects
- [func AudioConverterNew(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternew(_:_:_:).md)
  Creates a new audio converter object based on specified audio formats.
- [func AudioConverterNewSpecific(UnsafePointer<AudioStreamBasicDescription>, UnsafePointer<AudioStreamBasicDescription>, UInt32, UnsafePointer<AudioClassDescription>, UnsafeMutablePointer<AudioConverterRef?>) -> OSStatus](audioconverternewspecific(_:_:_:_:_:).md)
  Creates a new audio converter object using a specified codec.
- [func AudioConverterReset(AudioConverterRef) -> OSStatus](audioconverterreset(_:).md)
  Resets an audio converter object, clearing and flushing its buffers.
- [func AudioConverterDispose(AudioConverterRef) -> OSStatus](audioconverterdispose(_:).md)
  Disposes of an audio converter object.
### Configuring Audio Converter Properties
- [func AudioConverterGetProperty(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audioconvertergetproperty(_:_:_:_:).md)
  Gets an audio converter property value.
- [func AudioConverterGetPropertyInfo(AudioConverterRef, AudioConverterPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audioconvertergetpropertyinfo(_:_:_:_:).md)
  Gets information about an audio converter property.
- [func AudioConverterSetProperty(AudioConverterRef, AudioConverterPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audioconvertersetproperty(_:_:_:_:).md)
  Sets the value of an audio converter object property.
### Performing Conversions
- [Encoding and decoding audio](encoding-and-decoding-audio.md)
  Convert audio formats to efficiently manage data and quality.
- [func AudioConverterConvertBuffer(AudioConverterRef, UInt32, UnsafeRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audioconverterconvertbuffer(_:_:_:_:_:).md)
  Converts audio data from one linear PCM format to another.
- [func AudioConverterFillComplexBuffer(AudioConverterRef, AudioConverterComplexInputDataProc, UnsafeMutableRawPointer?, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<AudioStreamPacketDescription>?) -> OSStatus](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md)
  Converts audio data supplied by a callback function, supporting non-interleaved and packetized formats.
- [func AudioConverterConvertComplexBuffer(AudioConverterRef, UInt32, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<AudioBufferList>) -> OSStatus](audioconverterconvertcomplexbuffer(_:_:_:_:).md)
  Converts audio data from one linear PCM format to another, where both use the same sample rate.
### Callbacks
- [typealias AudioConverterComplexInputDataProc](audioconvertercomplexinputdataproc.md)
  Supplies input data to the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function.
- [typealias AudioConverterInputDataProc](audioconverterinputdataproc.md)
  Deprecated. Use [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) instead.
### Data Types
- [struct AudioConverterPrimeInfo](audioconverterprimeinfo.md)
  Specifies priming information for an audio converter.
- [typealias AudioConverterRef](audioconverterref.md)
  A reference to an audio converter object.
- [typealias AudioConverterPropertyID](audioconverterpropertyid.md)
  An audio converter property identifier.
### Constants
- [Audio Converter Properties](1559928-audio-converter-properties.md)
  Audio converter properties, used with the [`AudioConverterGetPropertyInfo(_:_:_:_:)`](audioconvertergetpropertyinfo(_:_:_:_:).md), [`AudioConverterGetProperty(_:_:_:_:)`](audioconvertergetproperty(_:_:_:_:).md), and [`AudioConverterSetProperty(_:_:_:_:)`](audioconvertersetproperty(_:_:_:_:).md) functions.
- [Converter Priming Constants](1559927-converter-priming-constants.md)
  Constants used with the [`kAudioConverterPrimeMethod`](kaudioconverterprimemethod.md) property.
- [Sample Rate Conversion Quality Identifiers](1559924-sample-rate-conversion-quality-i.md)
  Specifiers for sample rate conversion quality, used for the [`kAudioConverterSampleRateConverterQuality`](kaudioconvertersamplerateconverterquality.md) property.
- [Sample Rate Conversion Complexity Identifiers](1559923-sample-rate-conversion-complexit.md)
  Specifiers for the sample rate conversion algorithm, used for the [`kAudioConverterSampleRateConverterComplexity`](kaudioconvertersamplerateconvertercomplexity.md) property.
### Enumerations
- [Converter Audio Unit Properties](1533972-converter_audio_unit_properties.md)
  Properties for the Apple AUConverter audio unit.
- [Converter Audio Unit Subtypes](1584145-converter_audio_unit_subtypes.md)
  Audio data format converter audio unit subtypes for audio units provided by Apple.
- [Audio Converter Dithering Algorithms](1559931-audio-converter-dithering-algori.md)
- [Audio Converter Properties (macOS)](1559925-audio-converter-properties-macos.md)
- [Audio Converter Errors](1559930-audio-converter-errors.md)
### Result Codes
- [var kAudioConverterErr_FormatNotSupported: OSStatus](kaudioconvertererr_formatnotsupported.md)
- [var kAudioConverterErr_OperationNotSupported: OSStatus](kaudioconvertererr_operationnotsupported.md)
- [var kAudioConverterErr_PropertyNotSupported: OSStatus](kaudioconvertererr_propertynotsupported.md)
- [var kAudioConverterErr_InvalidInputSize: OSStatus](kaudioconvertererr_invalidinputsize.md)
- [var kAudioConverterErr_InvalidOutputSize: OSStatus](kaudioconvertererr_invalidoutputsize.md)
  The byte size is not an integer multiple of the frame size.
- [var kAudioConverterErr_UnspecifiedError: OSStatus](kaudioconvertererr_unspecifiederror.md)
- [var kAudioConverterErr_BadPropertySizeError: OSStatus](kaudioconvertererr_badpropertysizeerror.md)
- [var kAudioConverterErr_RequiresPacketDescriptionsError: OSStatus](kaudioconvertererr_requirespacketdescriptionserror.md)
- [var kAudioConverterErr_InputSampleRateOutOfRange: OSStatus](kaudioconvertererr_inputsamplerateoutofrange.md)
- [var kAudioConverterErr_OutputSampleRateOutOfRange: OSStatus](kaudioconvertererr_outputsamplerateoutofrange.md)
- [var kAudioConverterErr_HardwareInUse: OSStatus](kaudioconvertererr_hardwareinuse.md)
  Returned from the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function if the underlying hardware codec has become unavailable, probably due to an audio interruption.
- [var kAudioConverterErr_NoHardwarePermission: OSStatus](kaudioconvertererr_nohardwarepermission.md)
  Returned from the [`AudioConverterNew(_:_:_:)`](audioconverternew(_:_:_:).md) function if the new converter would use a hardware codec which the application does not have permission to use.

## See Also

- [Analyzing audio performance with Instruments](analyzing-audio-performance-with-instruments.md)
  Ensure a smooth and immersive audio experience in your apps using Audio System Trace.
- [Audio Session Support](audio-session-support.md)
  Describe the properties that you associate with audio sessions and audio routes.
- [Audio Toolbox Debugging](audio-toolbox-debugging.md)
  Obtain the internal state of Core Audio objects during the development and debugging of your code.
- [Workgroup Management](workgroup-management.md)
  Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Audio Codec](audio-codec.md)
  Translate audio data from one format to another.
- [Clock Utilities](clock-utilities.md)
  Manage time-related information associated with audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-converter-services)*