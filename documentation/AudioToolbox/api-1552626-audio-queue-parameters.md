# Audio Queue Parameters

**Framework**: Audio Toolbox

Identifiers for audio queue parameters.

#### Overview

These parameters apply only to playback audio queues. You can set a playback audio queue parameter in one of two ways:

- Set the value to take effect immediately using the [`AudioQueueSetParameter(_:_:_:)`](audioqueuesetparameter(_:_:_:).md) function.
- Schedule a value to take effect when a particular audio queue buffer plays. You supply the parameter when you enqueue the buffer. The new value is applied to the audio queue that owns the buffer when that buffer is rendered.

The [`AudioQueueGetParameter(_:_:_:)`](audioqueuegetparameter(_:_:_:).md) function always returns the current value of the parameter for an audio queue.

## Topics

### Constants
- [var kAudioQueueParam_Volume: AudioQueueParameterID](kaudioqueueparam_volume.md)
  The playback volume for the audio queue, ranging from `0.0` through `1.0` on a linear scale. A value of `0.0` indicates silence; a value of `1.0` (the default) indicates full volume for the audio queue instance.
- [var kAudioQueueParam_PlayRate: AudioQueueParameterID](kaudioqueueparam_playrate.md)
  The playback rate for the audio queue, in the range `0.5` through `2.0`. A value of `1.0` (the default) specifies that the audio queue should play at its normal rate.
- [var kAudioQueueParam_Pitch: AudioQueueParameterID](kaudioqueueparam_pitch.md)
  The number of cents to pitch-shift the audio queue’s playback, in the range `-2400` through `2400` cents (where 1200 cents corresponds to one musical octave.)
- [var kAudioQueueParam_VolumeRampTime: AudioQueueParameterID](kaudioqueueparam_volumeramptime.md)
  The number of seconds over which a volume change is ramped.
- [var kAudioQueueParam_Pan: AudioQueueParameterID](kaudioqueueparam_pan.md)
  The stereo panning position of a source. For a monophonic source, panning is determined as follows:

## See Also

- [typealias AudioQueuePropertyID](audioqueuepropertyid.md)
  Identifiers for audio queue properties.
- [Hardware Codec Policy Keys](1618724-hardware-codec-policy-keys.md)
  Indicates how an audio queue should choose between hardware and software implementations of a codec.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1552626-audio-queue-parameters)*