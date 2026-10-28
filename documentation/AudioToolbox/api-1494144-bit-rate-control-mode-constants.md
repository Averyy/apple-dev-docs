# Bit Rate Control Mode Constants

**Framework**: Audio Toolbox  
**Role**: API Collection

Bit rate control modes to be used with `kAudioCodecPropertyBitRateControlMode`.

## Overview

These modes are applicable only to encoders that can produce variable packet sizes, such as AAC.

## Topics

### Constants
- [var kAudioCodecBitRateControlMode_Constant: UInt32](./kaudiocodecbitratecontrolmode_constant.md)
- [var kAudioCodecBitRateControlMode_LongTermAverage: UInt32](./kaudiocodecbitratecontrolmode_longtermaverage.md)
- [var kAudioCodecBitRateControlMode_Variable: UInt32](./kaudiocodecbitratecontrolmode_variable.md)
- [var kAudioCodecBitRateControlMode_VariableConstrained: UInt32](./kaudiocodecbitratecontrolmode_variableconstrained.md)

## See Also

### Enumerations
- [Output Status Constants](./api-1494122-output-status-constants.md)
  Status values returned from the [`AudioCodecProduceOutputPackets(_:_:_:_:_:_:)`](./audiocodecproduceoutputpackets%28_,_,_,_,_,_%29.md) function.
- [Program Target Levels](./api-1494116-program-target-levels.md)
- [Dynamic Range Control Modes](./api-1494094-dynamic-range-control-modes.md)
- [Global Codec Properties](./api-1494121-global-codec-properties.md)
  These read-only properties disclose the capabilities of the codec and remain the same for all instances of the codec.
- [Instance Codec Properties](./api-1494111-instance-codec-properties.md)
  Properties that can be set or read on an instance of the audio codec.
- [Audio Codec Priming Method Constants](./api-1494154-audio-codec-priming-method-const.md)
  Values used with `kAudioCodecPropertyPrimeMethod`.
- [Audio Codec Quality Constants](./api-1494130-audio-codec-quality-constants.md)
  Sound quality settings to be used with the property `kAudioCodecPropertyQualitySetting`.
- [Audio Codec Routine Selectors](./api-1494074-audio-codec-routine-selectors.md)
  Selectors used by the Component Manager to call routines implemented by the codec and exposed to developers through the Audio Codec Services API. These selectors are for use by codec developers; if you are calling Audio Codec Services functions, you don’t need to use these constants.
- [Audio Codec Delays](./api-1494127-audio-codec-delays.md)
- [Audio Codec Delay Modes](./api-1494050-audio-codec-delay-modes.md)
- [Audio Codec Properties](./api-1494068-audio-codec-properties.md)
- [Audio Codec Errors](./api-1494076-audio-codec-errors.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1494144-bit-rate-control-mode-constants)*