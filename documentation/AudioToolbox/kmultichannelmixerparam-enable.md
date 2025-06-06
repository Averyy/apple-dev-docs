# kMultiChannelMixerParam_Enable

**Framework**: Audio Toolbox  
**Kind**: var

Enables a channel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kMultiChannelMixerParam_Enable: AudioUnitParameterID { get }
```

#### Discussion

Global scope. The value is a boolean: use `0` to disable the channel or `1` to enable the channel. The default value is `1`.

## See Also

- [var kMultiChannelMixerParam_Pan: AudioUnitParameterID](kmultichannelmixerparam_pan.md)
  The panning value for the mixer.
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

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_enable)*