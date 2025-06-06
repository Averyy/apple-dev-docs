# Audio Codec

**Framework**: Audio Toolbox

Translate audio data from one format to another.

## Topics

### Initializing an Audio Codec
- [func AudioCodecInitialize(AudioCodec, UnsafePointer<AudioStreamBasicDescription>?, UnsafePointer<AudioStreamBasicDescription>?, UnsafeRawPointer?, UInt32) -> OSStatus](audiocodecinitialize(_:_:_:_:_:).md)
  Sets up the specified codec to perform a data format translation.
- [func AudioCodecReset(AudioCodec) -> OSStatus](audiocodecreset(_:).md)
  Flushes all the audio data in the codec and clears the input buffer.
- [func AudioCodecUninitialize(AudioCodec) -> OSStatus](audiocodecuninitialize(_:).md)
  Moves the codec from the initialized state back to the uninitialized state.
### Configuring Buffers
- [func AudioCodecAppendInputBufferList(AudioCodec, UnsafePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocodecappendinputbufferlist(_:_:_:_:_:).md)
- [func AudioCodecProduceOutputBufferList(AudioCodec, UnsafeMutablePointer<AudioBufferList>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocodecproduceoutputbufferlist(_:_:_:_:_:).md)
### Accessing the Data
- [func AudioCodecAppendInputData(AudioCodec, UnsafeRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafePointer<AudioStreamPacketDescription>?) -> OSStatus](audiocodecappendinputdata(_:_:_:_:_:).md)
  Appends audio data to the codec’s input buffer.
- [func AudioCodecProduceOutputPackets(AudioCodec, UnsafeMutableRawPointer, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<UInt32>, UnsafeMutablePointer<AudioStreamPacketDescription>?, UnsafeMutablePointer<UInt32>) -> OSStatus](audiocodecproduceoutputpackets(_:_:_:_:_:_:).md)
  Retrieves output data from a codec.
### Accessing Codec Properties
- [func AudioCodecGetProperty(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>, UnsafeMutableRawPointer) -> OSStatus](audiocodecgetproperty(_:_:_:_:).md)
  Retrieves the value of a codec property.
- [func AudioCodecGetPropertyInfo(AudioCodec, AudioCodecPropertyID, UnsafeMutablePointer<UInt32>?, UnsafeMutablePointer<DarwinBoolean>?) -> OSStatus](audiocodecgetpropertyinfo(_:_:_:_:).md)
  Retrieves information about a codec property.
- [func AudioCodecSetProperty(AudioCodec, AudioCodecPropertyID, UInt32, UnsafeRawPointer) -> OSStatus](audiocodecsetproperty(_:_:_:_:).md)
  Sets the value of a codec property.
### Codec Types
- [struct AudioCodecMagicCookieInfo](audiocodecmagiccookieinfo.md)
  A structure holding magic cookie information needed by some codecs.
- [struct AudioCodecPrimeInfo](audiocodecprimeinfo.md)
  A structure specifying the number of leading and trailing empty frames to be inserted.
- [typealias AudioCodec](audiocodec.md)
  An instance of a Component Manager component.
- [typealias AudioCodecAppendInputBufferListProc](audiocodecappendinputbufferlistproc.md)
- [typealias AudioCodecAppendInputDataProc](audiocodecappendinputdataproc.md)
- [typealias AudioCodecGetPropertyInfoProc](audiocodecgetpropertyinfoproc.md)
- [typealias AudioCodecGetPropertyProc](audiocodecgetpropertyproc.md)
- [typealias AudioCodecInitializeProc](audiocodecinitializeproc.md)
- [typealias AudioCodecProduceOutputBufferListProc](audiocodecproduceoutputbufferlistproc.md)
- [typealias AudioCodecProduceOutputPacketsProc](audiocodecproduceoutputpacketsproc.md)
- [typealias AudioCodecPropertyID](audiocodecpropertyid.md)
  An integer identifying an audio codec property.
- [typealias AudioCodecResetProc](audiocodecresetproc.md)
- [typealias AudioCodecSetPropertyProc](audiocodecsetpropertyproc.md)
- [typealias AudioCodecUninitializeProc](audiocodecuninitializeproc.md)
### Audio Settings
- [struct AudioSettingsFlags](audiosettingsflags.md)
- [var kAudioSettings_AvailableValues: String](kaudiosettings_availablevalues.md)
- [var kAudioSettings_CurrentValue: String](kaudiosettings_currentvalue.md)
- [var kAudioSettings_Hint: String](kaudiosettings_hint.md)
- [var kAudioSettings_LimitedValues: String](kaudiosettings_limitedvalues.md)
- [var kAudioSettings_Parameters: String](kaudiosettings_parameters.md)
- [var kAudioSettings_SettingKey: String](kaudiosettings_settingkey.md)
- [var kAudioSettings_SettingName: String](kaudiosettings_settingname.md)
- [var kAudioSettings_Summary: String](kaudiosettings_summary.md)
- [var kAudioSettings_TopLevelKey: String](kaudiosettings_toplevelkey.md)
- [var kAudioSettings_Unit: String](kaudiosettings_unit.md)
- [var kAudioSettings_ValueType: String](kaudiosettings_valuetype.md)
- [var kAudioSettings_Version: String](kaudiosettings_version.md)
### Enumerations
- [Output Status Constants](1494122-output-status-constants.md)
  Status values returned from the [`AudioCodecProduceOutputPackets(_:_:_:_:_:_:)`](audiocodecproduceoutputpackets(_:_:_:_:_:_:).md) function.
- [Program Target Levels](1494116-program-target-levels.md)
- [Dynamic Range Control Modes](1494094-dynamic-range-control-modes.md)
- [Bit Rate Control Mode Constants](1494144-bit-rate-control-mode-constants.md)
  Bit rate control modes to be used with `kAudioCodecPropertyBitRateControlMode`.
- [Global Codec Properties](1494121-global-codec-properties.md)
  These read-only properties disclose the capabilities of the codec and remain the same for all instances of the codec.
- [Instance Codec Properties](1494111-instance-codec-properties.md)
  Properties that can be set or read on an instance of the audio codec.
- [Audio Codec Priming Method Constants](1494154-audio-codec-priming-method-const.md)
  Values used with `kAudioCodecPropertyPrimeMethod`.
- [Audio Codec Quality Constants](1494130-audio-codec-quality-constants.md)
  Sound quality settings to be used with the property `kAudioCodecPropertyQualitySetting`.
- [Audio Codec Routine Selectors](1494074-audio-codec-routine-selectors.md)
  Selectors used by the Component Manager to call routines implemented by the codec and exposed to developers through the Audio Codec Services API. These selectors are for use by codec developers; if you are calling Audio Codec Services functions, you don’t need to use these constants.
- [Audio Codec Delays](1494127-audio-codec-delays.md)
- [Audio Codec Delay Modes](1494050-audio-codec-delay-modes.md)
- [Audio Codec Properties](1494068-audio-codec-properties.md)
- [Audio Codec Errors](1494076-audio-codec-errors.md)

## See Also

- [Analyzing audio performance with Instruments](analyzing-audio-performance-with-instruments.md)
  Ensure a smooth and immersive audio experience in your apps using Audio System Trace.
- [Audio Converter Services](audio-converter-services.md)
  Convert between linear PCM audio formats, and between linear PCM and compressed formats.
- [Audio Session Support](audio-session-support.md)
  Describe the properties that you associate with audio sessions and audio routes.
- [Audio Toolbox Debugging](audio-toolbox-debugging.md)
  Obtain the internal state of Core Audio objects during the development and debugging of your code.
- [Workgroup Management](workgroup-management.md)
  Coordinate the activity of custom real-time audio threads with those of the system and other processes.
- [Clock Utilities](clock-utilities.md)
  Manage time-related information associated with audio playback.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/audio-codec)*