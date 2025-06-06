# kMultiChannelMixerParam_PostAveragePower

**Framework**: Audio Toolbox  
**Kind**: var

The average power level of the channel, after the mixer, in decibels.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kMultiChannelMixerParam_PostAveragePower: AudioUnitParameterID { get }
```

#### Discussion

Input and output scope. This is a read-only property. Use the value of this constant to read the left channel and its value+1 to read the right channel.

## See Also

- [var kMultiChannelMixerParam_Enable: AudioUnitParameterID](kmultichannelmixerparam_enable.md)
  Enables a channel.
- [var kMultiChannelMixerParam_Pan: AudioUnitParameterID](kmultichannelmixerparam_pan.md)
  The panning value for the mixer.
- [var kMultiChannelMixerParam_PostPeakHoldLevel: AudioUnitParameterID](kmultichannelmixerparam_postpeakholdlevel.md)
  The peak hold level of the channel, after the mixer, in decibels.
- [var kMultiChannelMixerParam_PreAveragePower: AudioUnitParameterID](kmultichannelmixerparam_preaveragepower.md)
  The average power level of the channel, prior to the mixer, in decibels.
- [var kMultiChannelMixerParam_PrePeakHoldLevel: AudioUnitParameterID](kmultichannelmixerparam_prepeakholdlevel.md)
  The peak hold level of the channel, prior to the mixer, in decibels.
- [var kMultiChannelMixerParam_Volume: AudioUnitParameterID](kmultichannelmixerparam_volume.md)
  The linear gain of the channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kmultichannelmixerparam_postaveragepower)*