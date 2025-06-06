# kAudioConverterErr_HardwareInUse

**Framework**: Audio Toolbox  
**Kind**: var

Returned from the [`AudioConverterFillComplexBuffer(_:_:_:_:_:_:)`](audioconverterfillcomplexbuffer(_:_:_:_:_:_:).md) function if the underlying hardware codec has become unavailable, probably due to an audio interruption.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioConverterErr_HardwareInUse: OSStatus { get }
```

#### Discussion

On receiving this error, your application must stop calling `AudioConverterFillComplexBuffer`. You can check the value of the [`kAudioConverterPropertyCanResumeFromInterruption`](kaudioconverterpropertycanresumefrominterruption.md) property to determine if the converter you are using can resume processing after an interruption. If so, then wait for an interruption-ended call from Audio Session Services, reactivate the audio session, and finally resume using the codec.

If the converter cannot resume processing after an interruption, then on interruption you must abandon the conversion, re-instantiate the converter, and perform the conversion again.

## See Also

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
- [var kAudioConverterErr_NoHardwarePermission: OSStatus](kaudioconvertererr_nohardwarepermission.md)
  Returned from the [`AudioConverterNew(_:_:_:)`](audioconverternew(_:_:_:).md) function if the new converter would use a hardware codec which the application does not have permission to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioconvertererr_hardwareinuse)*