# kAudioChannelLayoutTag_TMH_10_2_full

**Framework**: Core Audio Types  
**Kind**: var

An extended TMH 10.2 multiple-channel surround-based layout, recommended for use by audio units.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- macOS 10.3+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
var kAudioChannelLayoutTag_TMH_10_2_full: AudioChannelLayoutTag { get }
```

#### Discussion

This tag is equivalant to [`kAudioChannelLayoutTag_TMH_10_2_std`](kaudiochannellayouttag_tmh_10_2_std.md) plus additional channels. Your channel layout must be in the following order:

- Left
- Right
- Center
- Vertical height center
- Left surround direct
- Right surround direct
- Left surround
- Right surround
- Vertical height left
- Vertical height right
- Left wide
- Right wide
- Center surround direct
- Center surround
- Low-frequency effects 1
- Low-frequency effects 2
- Left center
- Right center
- HI
- VI
- Haptic

## See Also

- [var kAudioChannelLayoutTag_AudioUnit_5_0: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_5_0.md)
  A 5-channel surround-based layout, recommended for use by audio units.
- [var kAudioChannelLayoutTag_AudioUnit_6_0: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_6_0.md)
  A 6-channel surround-based layout, recommended for use by audio units.
- [var kAudioChannelLayoutTag_AudioUnit_7_0: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_7_0.md)
  A 7-channel surround-based layout, recommended for use by audio units.
- [var kAudioChannelLayoutTag_AudioUnit_7_0_Front: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_7_0_front.md)
  An alternate 7-channel surround-based layout, for use by audio units.
- [var kAudioChannelLayoutTag_AudioUnit_5_1: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_5_1.md)
  A 5.1-channel surround-based layout, recommended for use by audio units.
- [var kAudioChannelLayoutTag_AudioUnit_6_1: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_6_1.md)
  A 6.1-channel surround-based layout, recommended for use by audio units.
- [var kAudioChannelLayoutTag_AudioUnit_7_1: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_7_1.md)
  A 7.1-channel surround-based layout, recommended for use by audio units.
- [var kAudioChannelLayoutTag_AudioUnit_7_1_Front: AudioChannelLayoutTag](kaudiochannellayouttag_audiounit_7_1_front.md)
  A 7.1-channel surround-based layout, recommended for use by audio units.
- [var kAudioChannelLayoutTag_TMH_10_2_std: AudioChannelLayoutTag](kaudiochannellayouttag_tmh_10_2_std.md)
  A TMH 10.2 multiple-channel surround-based layout .


---

*[View on Apple Developer](https://developer.apple.com/documentation/coreaudiotypes/kaudiochannellayouttag_tmh_10_2_full)*