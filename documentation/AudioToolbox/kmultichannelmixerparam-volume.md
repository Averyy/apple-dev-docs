# kMultiChannelMixerParam_Volume

**Framework**: Audio Toolbox  
**Kind**: var

The linear gain of the channel.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kMultiChannelMixerParam_Volume: AudioUnitParameterID { get }
```

#### Discussion

Global scope. The value should be a number between `0.0` and `1.0`. The default value is `1.0`.

## See Also

- [var kMultiChannelMixerParam_Enable: AudioUnitParameterID](kmultichannelmixerparam_enable.md)
  Enables a channel.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_volume)*