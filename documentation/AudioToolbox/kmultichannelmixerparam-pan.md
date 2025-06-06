# kMultiChannelMixerParam_Pan

**Framework**: Audio Toolbox  
**Kind**: var

The panning value for the mixer.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kMultiChannelMixerParam_Pan: AudioUnitParameterID { get }
```

#### Discussion

Global scope. The value should be a number between `-1.0` and `1.0`, where `-1.0` represents far left and `1.0` represents far right. The default value is `0`. Setting [`kAudioUnitProperty_MatrixLevels`](kaudiounitproperty_matrixlevels.md) overrides any value set for `kMultiChannelMixerParam_Pan` and vice versa.

## See Also

- [var kMultiChannelMixerParam_Enable: AudioUnitParameterID](kmultichannelmixerparam_enable.md)
  Enables a channel.
- [var kMultiChannelMixerParam_PostAveragePower: AudioUnitParameterID](kmultichannelmixerparam_postaveragepower.md)
  The average power level of the channel, after the mixer, in decibels.
- [var kMultiChannelMixerParam_PostPeakHoldLevel: AudioUnitParameterID](kmultichannelmixerparam_postpeakholdlevel.md)
  The peak hold level of the channel, after the mixer, in decibels.
- [var kMultiChannelMixerParam_PreAveragePower: AudioUnitParameterID](kmultichannelmixerparam_preaveragepower.md)
  The average power level of the channel, prior to the mixer, in decibels.
- [var kMultiChannelMixerParam_PrePeakHoldLevel: AudioUnitParameterID](kmultichannelmixerparam_prepeakholdlevel.md)
  The peak hold level of the channel, prior to the mixer, in decibels.
- [var kMultiChannelMixerParam_Volume: AudioUnitParameterID](kmultichannelmixerparam_volume.md)
  The linear gain of the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_pan)*