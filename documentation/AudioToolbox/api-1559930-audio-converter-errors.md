# Audio Converter Errors

**Framework**: Audio Toolbox

## Topics

### Constants
- [var kAudioConverterErr_BadPropertySizeError: OSStatus](kaudioconvertererr_badpropertysizeerror.md)
- [var kAudioConverterErr_FormatNotSupported: OSStatus](kaudioconvertererr_formatnotsupported.md)
- [var kAudioConverterErr_HardwareInUse: OSStatus](kaudioconvertererr_hardwareinuse.md)
  Returned from the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function if the underlying hardware codec has become unavailable, probably due to an audio interruption.
- [var kAudioConverterErr_InputSampleRateOutOfRange: OSStatus](kaudioconvertererr_inputsamplerateoutofrange.md)
- [var kAudioConverterErr_InvalidInputSize: OSStatus](kaudioconvertererr_invalidinputsize.md)
- [var kAudioConverterErr_InvalidOutputSize: OSStatus](kaudioconvertererr_invalidoutputsize.md)
  The byte size is not an integer multiple of the frame size.
- [var kAudioConverterErr_NoHardwarePermission: OSStatus](kaudioconvertererr_nohardwarepermission.md)
  Returned from the [`AudioConverterNew(_:_:_:)`](audioconverternew(_:_:_:).md) function if the new converter would use a hardware codec which the application does not have permission to use.
- [var kAudioConverterErr_OperationNotSupported: OSStatus](kaudioconvertererr_operationnotsupported.md)
- [var kAudioConverterErr_OutputSampleRateOutOfRange: OSStatus](kaudioconvertererr_outputsamplerateoutofrange.md)
- [var kAudioConverterErr_PropertyNotSupported: OSStatus](kaudioconvertererr_propertynotsupported.md)
- [var kAudioConverterErr_RequiresPacketDescriptionsError: OSStatus](kaudioconvertererr_requirespacketdescriptionserror.md)
- [var kAudioConverterErr_UnspecifiedError: OSStatus](kaudioconvertererr_unspecifiederror.md)

## See Also

- [Converter Audio Unit Properties](1533972-converter_audio_unit_properties.md)
  Properties for the Apple AUConverter audio unit.
- [Converter Audio Unit Subtypes](1584145-converter_audio_unit_subtypes.md)
  Audio data format converter audio unit subtypes for audio units provided by Apple.
- [Audio Converter Dithering Algorithms](1559931-audio-converter-dithering-algori.md)
- [Audio Converter Properties (macOS)](1559925-audio-converter-properties-macos.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1559930-audio-converter-errors)*