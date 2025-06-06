# IOUserAudioChannelLabel

**Framework**: AudioDriverKit  
**Kind**: enum

Constants to set the preferred channel layout on an audio device.

**Availability**:
- DriverKit 21.0+

## Declaration

```swift
enum IOUserAudioChannelLabel : uint32_t;
```

#### Discussion

These channel labels attempt to list all labels in common use. Due to the ambiguities in channel labeling by various groups, there may be some overlap or duplication in the labels below. Use the label which most clearly describes what you mean.

## Topics

### Left Channels
- [Left](audiodriverkit/iouseraudiochannellabel/left.md)
  The left channel.
- [LeftCenter](audiodriverkit/iouseraudiochannellabel/leftcenter.md)
  The left center channel.
- [LeftTopFront](audiodriverkit/iouseraudiochannellabel/lefttopfront.md)
  The left top front channel.
- [VerticalHeightLeft](audiodriverkit/iouseraudiochannellabel/verticalheightleft.md)
  A synonym for the top-left–front channel.
- [LeftTopMiddle](audiodriverkit/iouseraudiochannellabel/lefttopmiddle.md)
  The left top middle channel.
- [LeftTopRear](audiodriverkit/iouseraudiochannellabel/lefttoprear.md)
  The left top rear channel.
- [LeftTotal](audiodriverkit/iouseraudiochannellabel/lefttotal.md)
  A matrix encode of four left channels.
- [LeftWide](audiodriverkit/iouseraudiochannellabel/leftwide.md)
  The left wide channel.
### Right Channels
- [Right](audiodriverkit/iouseraudiochannellabel/right.md)
  The right channel.
- [RightCenter](audiodriverkit/iouseraudiochannellabel/rightcenter.md)
  The right center channel.
- [RightTopFront](audiodriverkit/iouseraudiochannellabel/righttopfront.md)
  The right top front channel.
- [VerticalHeightRight](audiodriverkit/iouseraudiochannellabel/verticalheightright.md)
  A synonym for the top-right–front channel.
- [RightTopMiddle](audiodriverkit/iouseraudiochannellabel/righttopmiddle.md)
  The right top middle channel.
- [RightTopRear](audiodriverkit/iouseraudiochannellabel/righttoprear.md)
  The right top rear channel.
- [RightTotal](audiodriverkit/iouseraudiochannellabel/righttotal.md)
  A matrix encode of four right channels.
- [RightWide](audiodriverkit/iouseraudiochannellabel/rightwide.md)
  The right wide channel.
### Center Channels
- [Center](audiodriverkit/iouseraudiochannellabel/center.md)
  The center channel.
- [CenterTopFront](audiodriverkit/iouseraudiochannellabel/centertopfront.md)
  The center top front channel.
- [VerticalHeightCenter](audiodriverkit/iouseraudiochannellabel/verticalheightcenter.md)
  A synonym for the top-center–front channel.
- [CenterTopMiddle](audiodriverkit/iouseraudiochannellabel/centertopmiddle.md)
  The center top middle channel.
- [CenterTopRear](audiodriverkit/iouseraudiochannellabel/centertoprear.md)
  The center top rear channel.
### Back Channels
- [TopBackCenter](audiodriverkit/iouseraudiochannellabel/topbackcenter.md)
  The top-rear–center channel.
- [TopCenterSurround](audiodriverkit/iouseraudiochannellabel/topcentersurround.md)
  A synonym for the top-rear–center channel.
- [TopBackLeft](audiodriverkit/iouseraudiochannellabel/topbackleft.md)
  The top-rear–left channel.
- [TopBackRight](audiodriverkit/iouseraudiochannellabel/topbackright.md)
  The top-rear–right channel.
### Surround Channels
- [CenterSurround](audiodriverkit/iouseraudiochannellabel/centersurround.md)
  The center surround channel.
- [CenterSurroundDirect](audiodriverkit/iouseraudiochannellabel/centersurrounddirect.md)
  The center surround direct channel.
- [LeftSurround](audiodriverkit/iouseraudiochannellabel/leftsurround.md)
  The left surround channel.
- [LeftSurroundDirect](audiodriverkit/iouseraudiochannellabel/leftsurrounddirect.md)
  The left surround direct channel.
- [RearSurroundLeft](audiodriverkit/iouseraudiochannellabel/rearsurroundleft.md)
  The rear left surround channel.
- [RearSurroundRight](audiodriverkit/iouseraudiochannellabel/rearsurroundright.md)
  The right rear surround channel.
- [RightSurround](audiodriverkit/iouseraudiochannellabel/rightsurround.md)
  The right surround channel.
- [RightSurroundDirect](audiodriverkit/iouseraudiochannellabel/rightsurrounddirect.md)
  The right surround direct channel.
### Low-Frequency Effects Channels
- [LFE2](audiodriverkit/iouseraudiochannellabel/lfe2.md)
  The low-frequency effects 2 (LFE2) channel.
- [LFEScreen](audiodriverkit/iouseraudiochannellabel/lfescreen.md)
  The low-frequency effects (LFE) screen channel.
### Monaural Channels
- [Mono](audiodriverkit/iouseraudiochannellabel/mono.md)
  The mono channel.
### Alternate Content Channels
- [ClickTrack](audiodriverkit/iouseraudiochannellabel/clicktrack.md)
  The click track channel.
- [DialogCentricMix](audiodriverkit/iouseraudiochannellabel/dialogcentricmix.md)
  The dialog-centric mix channel.
- [ForeignLanguage](audiodriverkit/iouseraudiochannellabel/foreignlanguage.md)
  The foreign language channel.
- [HearingImpaired](audiodriverkit/iouseraudiochannellabel/hearingimpaired.md)
  The audio for the hearing-impaired channel.
- [Haptic](audiodriverkit/iouseraudiochannellabel/haptic.md)
  The haptic effects channel.
- [Narration](audiodriverkit/iouseraudiochannellabel/narration.md)
  The narration channel.
### Mid/Side Recording
- [MS_Mid](audiodriverkit/iouseraudiochannellabel/ms_mid.md)
  The Mid/Side recording mid channel.
- [MS_Side](audiodriverkit/iouseraudiochannellabel/ms_side.md)
  The Mid/Side recording side channel.
### X/Y Recording Channels
- [XY_X](audiodriverkit/iouseraudiochannellabel/xy_x.md)
  The X/Y recording X channel.
- [XY_Y](audiodriverkit/iouseraudiochannellabel/xy_y.md)
  The X/Y recording Y channel.
### First-Order Ambisonic Channels
- [Ambisonic_W](audiodriverkit/iouseraudiochannellabel/ambisonic_w.md)
  The ambisonic W channel.
- [Ambisonic_X](audiodriverkit/iouseraudiochannellabel/ambisonic_x.md)
  The ambisonic X channel.
- [Ambisonic_Y](audiodriverkit/iouseraudiochannellabel/ambisonic_y.md)
  The ambisonic Y channel.
- [Ambisonic_Z](audiodriverkit/iouseraudiochannellabel/ambisonic_z.md)
  The ambisonic Z channel.
### Binaural Recording
- [BinauralLeft](audiodriverkit/iouseraudiochannellabel/binauralleft.md)
  The binaural left channel.
- [BinauralRight](audiodriverkit/iouseraudiochannellabel/binauralright.md)
  The binaural right channel.
### Headphone Channels
- [HeadphonesLeft](audiodriverkit/iouseraudiochannellabel/headphonesleft.md)
  The left headphone channel.
- [HeadphonesRight](audiodriverkit/iouseraudiochannellabel/headphonesright.md)
  The right headphone channel.
### Unnumbered Discrete Channels
- [Discrete](audiodriverkit/iouseraudiochannellabel/discrete.md)
  A generic discrete channel.
### Numbered Discrete Channels
- [Discrete_0](audiodriverkit/iouseraudiochannellabel/discrete_0.md)
  Numbered discrete channel 0.
- [Discrete_1](audiodriverkit/iouseraudiochannellabel/discrete_1.md)
  Numbered discrete channel 1.
- [Discrete_2](audiodriverkit/iouseraudiochannellabel/discrete_2.md)
  Numbered discrete channel 2.
- [Discrete_3](audiodriverkit/iouseraudiochannellabel/discrete_3.md)
  Numbered discrete channel 3.
- [Discrete_4](audiodriverkit/iouseraudiochannellabel/discrete_4.md)
  Numbered discrete channel 4.
- [Discrete_5](audiodriverkit/iouseraudiochannellabel/discrete_5.md)
  Numbered discrete channel 5.
- [Discrete_6](audiodriverkit/iouseraudiochannellabel/discrete_6.md)
  Numbered discrete channel 6.
- [Discrete_7](audiodriverkit/iouseraudiochannellabel/discrete_7.md)
  Numbered discrete channel 7.
- [Discrete_8](audiodriverkit/iouseraudiochannellabel/discrete_8.md)
  Numbered discrete channel 8.
- [Discrete_9](audiodriverkit/iouseraudiochannellabel/discrete_9.md)
  Numbered discrete channel 9.
- [Discrete_10](audiodriverkit/iouseraudiochannellabel/discrete_10.md)
  Numbered discrete channel 10.
- [Discrete_11](audiodriverkit/iouseraudiochannellabel/discrete_11.md)
  Numbered discrete channel 11.
- [Discrete_12](audiodriverkit/iouseraudiochannellabel/discrete_12.md)
  Numbered discrete channel 12.
- [Discrete_13](audiodriverkit/iouseraudiochannellabel/discrete_13.md)
  Numbered discrete channel 13.
- [Discrete_14](audiodriverkit/iouseraudiochannellabel/discrete_14.md)
  Numbered discrete channel 14.
- [Discrete_15](audiodriverkit/iouseraudiochannellabel/discrete_15.md)
  Numbered discrete channel 15.
- [Discrete_65535](audiodriverkit/iouseraudiochannellabel/discrete_65535.md)
  The maximum numbered discrete channel.
### Generic High Order Ambisonics ACN Channel
- [HOA_ACN](audiodriverkit/iouseraudiochannellabel/hoa_acn.md)
  A generic high order ambisonics (HOA) Ambisonic Channel Number (ACN).
### Numbered High Order Ambisonics ACN Channels
- [HOA_ACN_0](audiodriverkit/iouseraudiochannellabel/hoa_acn_0.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 0.
- [HOA_ACN_1](audiodriverkit/iouseraudiochannellabel/hoa_acn_1.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 1.
- [HOA_ACN_2](audiodriverkit/iouseraudiochannellabel/hoa_acn_2.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 2.
- [HOA_ACN_3](audiodriverkit/iouseraudiochannellabel/hoa_acn_3.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 3.
- [HOA_ACN_4](audiodriverkit/iouseraudiochannellabel/hoa_acn_4.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 4.
- [HOA_ACN_5](audiodriverkit/iouseraudiochannellabel/hoa_acn_5.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 5.
- [HOA_ACN_6](audiodriverkit/iouseraudiochannellabel/hoa_acn_6.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 6.
- [HOA_ACN_7](audiodriverkit/iouseraudiochannellabel/hoa_acn_7.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 7.
- [HOA_ACN_8](audiodriverkit/iouseraudiochannellabel/hoa_acn_8.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 8.
- [HOA_ACN_9](audiodriverkit/iouseraudiochannellabel/hoa_acn_9.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 9.
- [HOA_ACN_10](audiodriverkit/iouseraudiochannellabel/hoa_acn_10.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 10
- [HOA_ACN_11](audiodriverkit/iouseraudiochannellabel/hoa_acn_11.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 11.
- [HOA_ACN_12](audiodriverkit/iouseraudiochannellabel/hoa_acn_12.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 12.
- [HOA_ACN_13](audiodriverkit/iouseraudiochannellabel/hoa_acn_13.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 13.
- [HOA_ACN_14](audiodriverkit/iouseraudiochannellabel/hoa_acn_14.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 14.
- [HOA_ACN_15](audiodriverkit/iouseraudiochannellabel/hoa_acn_15.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 15.
- [HOA_ACN_65024](audiodriverkit/iouseraudiochannellabel/hoa_acn_65024.md)
  The maximum numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN).
### Special Values
- [Unused](audiodriverkit/iouseraudiochannellabel/unused.md)
  An unknown or otherwise unspecified channel use.
- [UseCoordinates](audiodriverkit/iouseraudiochannellabel/usecoordinates.md)
  A channel that uses coodinates to describe its position.
### Reserved Values
- [BeginReserved](audiodriverkit/iouseraudiochannellabel/beginreserved.md)
  The beginning of the range of channel values reserved for internal use.
- [EndReserved](audiodriverkit/iouseraudiochannellabel/endreserved.md)
### Enumeration Cases
- [Unknown](audiodriverkit/iouseraudiochannellabel/unknown.md)
  unknown or unspecified other use

## See Also

- [SetPreferredChannelsForStereo](iouseraudiodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the prefered stereo pair.
- [GetPreferredChannelsForStereo](iouseraudiodevice/getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredInputChannelLayout](iouseraudiodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout, using an array of audio channel label values.
- [SetPreferredOutputChannelLayout](iouseraudiodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiochannellabel)*