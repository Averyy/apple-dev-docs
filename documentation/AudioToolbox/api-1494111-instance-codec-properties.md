# Instance Codec Properties

**Framework**: Audio Toolbox

Properties that can be set or read on an instance of the audio codec.

#### Overview

These properties are used with the [`AudioCodecGetProperty(_:_:_:_:)`](audiocodecgetproperty(_:_:_:_:).md) and [`AudioCodecSetProperty(_:_:_:_:)`](audiocodecsetproperty(_:_:_:_:).md) functions.

These properties are dependent on the codec’s current state. A property may be read/write or read only, depending on the data format of the codec.

These properties may have different values depending on whether the codec is in the initialized state. You can set writable properties only when the codec is not initialized. All properties can be read at any time the codec is open.

## Topics

### Constants
- [var kAudioCodecPropertyAdjustLocalQuality: AudioCodecPropertyID](kaudiocodecpropertyadjustlocalquality.md)
- [var kAudioCodecPropertyApplicableBitRateRange: AudioCodecPropertyID](kaudiocodecpropertyapplicablebitraterange.md)
- [var kAudioCodecPropertyApplicableInputSampleRates: AudioCodecPropertyID](kaudiocodecpropertyapplicableinputsamplerates.md)
- [var kAudioCodecPropertyApplicableOutputSampleRates: AudioCodecPropertyID](kaudiocodecpropertyapplicableoutputsamplerates.md)
- [var kAudioCodecPropertyBitRateControlMode: AudioCodecPropertyID](kaudiocodecpropertybitratecontrolmode.md)
- [var kAudioCodecPropertyCurrentInputChannelLayout: AudioCodecPropertyID](kaudiocodecpropertycurrentinputchannellayout.md)
- [var kAudioCodecPropertyCurrentInputFormat: AudioCodecPropertyID](kaudiocodecpropertycurrentinputformat.md)
- [var kAudioCodecPropertyCurrentInputSampleRate: AudioCodecPropertyID](kaudiocodecpropertycurrentinputsamplerate.md)
- [var kAudioCodecPropertyCurrentOutputChannelLayout: AudioCodecPropertyID](kaudiocodecpropertycurrentoutputchannellayout.md)
- [var kAudioCodecPropertyCurrentOutputFormat: AudioCodecPropertyID](kaudiocodecpropertycurrentoutputformat.md)
- [var kAudioCodecPropertyCurrentOutputSampleRate: AudioCodecPropertyID](kaudiocodecpropertycurrentoutputsamplerate.md)
- [var kAudioCodecPropertyCurrentTargetBitRate: AudioCodecPropertyID](kaudiocodecpropertycurrenttargetbitrate.md)
- [var kAudioCodecPropertyDelayMode: AudioCodecPropertyID](kaudiocodecpropertydelaymode.md)
- [var kAudioCodecPropertyDynamicRangeControlMode: AudioCodecPropertyID](kaudiocodecpropertydynamicrangecontrolmode.md)
- [var kAudioCodecPropertyFormatList: AudioCodecPropertyID](kaudiocodecpropertyformatlist.md)
- [var kAudioCodecPropertyHasVariablePacketByteSizes: AudioCodecPropertyID](kaudiocodecpropertyhasvariablepacketbytesizes.md)
- [var kAudioCodecPropertyInputBufferSize: AudioCodecPropertyID](kaudiocodecpropertyinputbuffersize.md)
- [var kAudioCodecPropertyIsInitialized: AudioCodecPropertyID](kaudiocodecpropertyisinitialized.md)
- [var kAudioCodecPropertyMagicCookie: AudioCodecPropertyID](kaudiocodecpropertymagiccookie.md)
- [var kAudioCodecPropertyMaximumPacketByteSize: AudioCodecPropertyID](kaudiocodecpropertymaximumpacketbytesize.md)
- [var kAudioCodecPropertyPacketFrameSize: AudioCodecPropertyID](kaudiocodecpropertypacketframesize.md)
- [var kAudioCodecPropertyPacketSizeLimitForVBR: AudioCodecPropertyID](kaudiocodecpropertypacketsizelimitforvbr.md)
- [var kAudioCodecPropertyPaddedZeros: AudioCodecPropertyID](kaudiocodecpropertypaddedzeros.md)
- [var kAudioCodecPropertyPrimeInfo: AudioCodecPropertyID](kaudiocodecpropertyprimeinfo.md)
- [var kAudioCodecPropertyPrimeMethod: AudioCodecPropertyID](kaudiocodecpropertyprimemethod.md)
- [var kAudioCodecPropertyProgramTargetLevel: AudioCodecPropertyID](kaudiocodecpropertyprogramtargetlevel.md)
- [var kAudioCodecPropertyProgramTargetLevelConstant: AudioCodecPropertyID](kaudiocodecpropertyprogramtargetlevelconstant.md)
- [var kAudioCodecPropertyQualitySetting: AudioCodecPropertyID](kaudiocodecpropertyqualitysetting.md)
- [var kAudioCodecPropertyRecommendedBitRateRange: AudioCodecPropertyID](kaudiocodecpropertyrecommendedbitraterange.md)
- [var kAudioCodecPropertySettings: AudioCodecPropertyID](kaudiocodecpropertysettings.md)
- [var kAudioCodecPropertySoundQualityForVBR: AudioCodecPropertyID](kaudiocodecpropertysoundqualityforvbr.md)
- [var kAudioCodecPropertyUsedInputBufferSize: AudioCodecPropertyID](kaudiocodecpropertyusedinputbuffersize.md)
- [var kAudioCodecPropertyAdjustCompressionProfile: AudioCodecPropertyID](kaudiocodecpropertyadjustcompressionprofile.md)
- [var kAudioCodecPropertyAdjustTargetLevel: AudioCodecPropertyID](kaudiocodecpropertyadjusttargetlevel.md)
- [var kAudioCodecPropertyAdjustTargetLevelConstant: AudioCodecPropertyID](kaudiocodecpropertyadjusttargetlevelconstant.md)
- [var kAudioCodecPropertyBitRateForVBR: AudioCodecPropertyID](kaudiocodecpropertybitrateforvbr.md)
- [var kAudioCodecPropertyEmploysDependentPackets: AudioCodecPropertyID](kaudiocodecpropertyemploysdependentpackets.md)

## See Also

- [Output Status Constants](1494122-output-status-constants.md)
  Status values returned from the [`AudioCodecProduceOutputPackets(_:_:_:_:_:_:)`](audiocodecproduceoutputpackets(_:_:_:_:_:_:).md) function.
- [Program Target Levels](1494116-program-target-levels.md)
- [Dynamic Range Control Modes](1494094-dynamic-range-control-modes.md)
- [Bit Rate Control Mode Constants](1494144-bit-rate-control-mode-constants.md)
  Bit rate control modes to be used with `kAudioCodecPropertyBitRateControlMode`.
- [Global Codec Properties](1494121-global-codec-properties.md)
  These read-only properties disclose the capabilities of the codec and remain the same for all instances of the codec.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1494111-instance-codec-properties)*