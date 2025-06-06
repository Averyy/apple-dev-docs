# Audio Queue Hardware Codec Policy

**Framework**: Audio Toolbox

## Topics

### Constants
- [var kAudioQueueHardwareCodecPolicy_Default: UInt32](kaudioqueuehardwarecodecpolicy_default.md)
  If the required codec is available in both hardware and software implementations, the audio queue will use a hardware codec if its audio session category permits; it will use a software codec otherwise. If the required codec is available in only one form, that codec implementation is used.
- [var kAudioQueueHardwareCodecPolicy_PreferHardware: UInt32](kaudioqueuehardwarecodecpolicy_preferhardware.md)
  The audio queue will use a hardware codec if one is available and if its use permitted by the audio session category that you have set; otherwise, it will use a software codec if one is available.
- [var kAudioQueueHardwareCodecPolicy_PreferSoftware: UInt32](kaudioqueuehardwarecodecpolicy_prefersoftware.md)
  The audio queue will use a software codec if one is available; if not, it will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.
- [var kAudioQueueHardwareCodecPolicy_UseHardwareOnly: UInt32](kaudioqueuehardwarecodecpolicy_usehardwareonly.md)
  The audio queue will use a hardware codec if one is available and if its use is permitted by the audio session category that you have set.
- [var kAudioQueueHardwareCodecPolicy_UseSoftwareOnly: UInt32](kaudioqueuehardwarecodecpolicy_usesoftwareonly.md)
  The audio queue will use a software codec if one is available.

## See Also

- [struct AudioQueueProcessingTapFlags](audioqueueprocessingtapflags.md)
- [Anonymous](1552627-anonymous.md)
- [Audio Queue Time Pitch Algorithms](1552630-audio-queue-time-pitch-algorithm.md)
- [Audio Queue Property IDs](1552629-audio-queue-property-ids.md)
- [Audio Queue Property IDs](1618733-audio-queue-property-ids.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiotoolbox/1618727-audio-queue-hardware-codec-polic)*