# Hardware Codec Policy Keys

**Framework**: Audio Toolbox

Indicates how an audio queue should choose between hardware and software implementations of a codec.

#### Overview

If the designated codec implementation is not available, or if a hardware codec is chosen and the audio session category does not permit use of hardware codecs, your attempts to call the [`AudioQueuePrime(_:_:_:)`](audioqueueprime(_:_:_:).md) or [`AudioQueueStart(_:_:)`](audioqueuestart(_:_:).md) functions will fail.

Use the [`kAudioFormatProperty_Encoders`](kaudioformatproperty_encoders.md) or [`kAudioFormatProperty_Decoders`](kaudioformatproperty_decoders.md) properties to determine whether the codec you are interested in using is available in hardware form, software, or both. See the discussion for [`kAudioFormatProperty_HardwareCodecCapabilities`](kaudioformatproperty_hardwarecodeccapabilities.md).

The system does not permit you to change the value associated with the [`kAudioQueueProperty_HardwareCodecPolicy`](kaudioqueueproperty_hardwarecodecpolicy.md) key while the audio queue is primed or running. Changing the value at other times may cause codec settings to be lost.

## Topics

### Constants
- [var kAudioQueueProperty_HardwareCodecPolicy: AudioQueuePropertyID](kaudioqueueproperty_hardwarecodecpolicy.md)
  The preferred codec implementation type—hardware or software—for an audio queue. Possible values for this constant are the remaining constants described in this section.
- [var kAudioQueueHardwareCodecPolicy_Default: UInt32](kaudioqueuehardwarecodecpolicy_default.md)
  If the required codec is available in both hardware and software implementations, the audio queue will use a hardware codec if its audio session category permits; it will use a software codec otherwise. If the required codec is available in only one form, that codec implementation is used.
- [var kAudioQueueHardwareCodecPolicy_UseSoftwareOnly: UInt32](kaudioqueuehardwarecodecpolicy_usesoftwareonly.md)
  The audio queue will use a software codec if one is available.
- [var kAudioQueueHardwareCodecPolicy_UseHardwareOnly: UInt32](kaudioqueuehardwarecodecpolicy_usehardwareonly.md)
  The audio queue will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.
- [var kAudioQueueHardwareCodecPolicy_PreferSoftware: UInt32](kaudioqueuehardwarecodecpolicy_prefersoftware.md)
  The audio queue will use a software codec if one is available; if not, it will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.
- [var kAudioQueueHardwareCodecPolicy_PreferHardware: UInt32](kaudioqueuehardwarecodecpolicy_preferhardware.md)
  The audio queue will use a hardware codec if one is available and if its use permitted by the audio session category that you have set; otherwise, it will use a software codec if one is available.

## See Also

- [typealias AudioQueuePropertyID](audioqueuepropertyid.md)
  Identifiers for audio queue properties.
- [Audio Queue Parameters](1552626-audio-queue-parameters.md)
  Identifiers for audio queue parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1618724-hardware-codec-policy-keys)*