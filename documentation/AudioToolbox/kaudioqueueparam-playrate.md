# kAudioQueueParam_PlayRate

**Framework**: Audio Toolbox  
**Kind**: var

The playback rate for the audio queue, in the range `0.5` through `2.0`. A value of `1.0` (the default) specifies that the audio queue should play at its normal rate.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
var kAudioQueueParam_PlayRate: AudioQueueParameterID { get }
```

#### Discussion

This parameter is usable only if the time-pitch processor is enabled.

## See Also

- [var kAudioQueueParam_Volume: AudioQueueParameterID](kaudioqueueparam_volume.md)
  The playback volume for the audio queue, ranging from `0.0` through `1.0` on a linear scale. A value of `0.0` indicates silence; a value of `1.0` (the default) indicates full volume for the audio queue instance.
- [var kAudioQueueParam_Pitch: AudioQueueParameterID](kaudioqueueparam_pitch.md)
  The number of cents to pitch-shift the audio queue’s playback, in the range `-2400` through `2400` cents (where 1200 cents corresponds to one musical octave.)
- [var kAudioQueueParam_VolumeRampTime: AudioQueueParameterID](kaudioqueueparam_volumeramptime.md)
  The number of seconds over which a volume change is ramped.
- [var kAudioQueueParam_Pan: AudioQueueParameterID](kaudioqueueparam_pan.md)
  The stereo panning position of a source. For a monophonic source, panning is determined as follows:


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/kaudioqueueparam_playrate)*