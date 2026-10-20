# IOUserAudioChannelLabel

**Framework**: AudioDriverKit  
**Kind**: enum  
**Role**: Enumeration

Constants to set the preferred channel layout on an audio device.

**Availability**:
- DriverKit 21.0+

## Declaration

```c
enum IOUserAudioChannelLabel : uint32_t;
```

#### Discussion

These channel labels attempt to list all labels in common use. Due to the ambiguities in channel labeling by various groups, there may be some overlap or duplication in the labels below. Use the label which most clearly describes what you mean.

## Topics

### Left Channels
- [Left](./iouseraudiochannellabel/left.md)
  The left channel.
- [LeftCenter](./iouseraudiochannellabel/leftcenter.md)
  The left center channel.
- [LeftTopFront](./iouseraudiochannellabel/lefttopfront.md)
  The left top front channel.
- [VerticalHeightLeft](./iouseraudiochannellabel/verticalheightleft.md)
  A synonym for the top-left–front channel.
- [LeftTopMiddle](./iouseraudiochannellabel/lefttopmiddle.md)
  The left top middle channel.
- [LeftTopRear](./iouseraudiochannellabel/lefttoprear.md)
  The left top rear channel.
- [LeftTotal](./iouseraudiochannellabel/lefttotal.md)
  A matrix encode of four left channels.
- [LeftWide](./iouseraudiochannellabel/leftwide.md)
  The left wide channel.
### Right Channels
- [Right](./iouseraudiochannellabel/right.md)
  The right channel.
- [RightCenter](./iouseraudiochannellabel/rightcenter.md)
  The right center channel.
- [RightTopFront](./iouseraudiochannellabel/righttopfront.md)
  The right top front channel.
- [VerticalHeightRight](./iouseraudiochannellabel/verticalheightright.md)
  A synonym for the top-right–front channel.
- [RightTopMiddle](./iouseraudiochannellabel/righttopmiddle.md)
  The right top middle channel.
- [RightTopRear](./iouseraudiochannellabel/righttoprear.md)
  The right top rear channel.
- [RightTotal](./iouseraudiochannellabel/righttotal.md)
  A matrix encode of four right channels.
- [RightWide](./iouseraudiochannellabel/rightwide.md)
  The right wide channel.
### Center Channels
- [Center](./iouseraudiochannellabel/center.md)
  The center channel.
- [CenterTopFront](./iouseraudiochannellabel/centertopfront.md)
  The center top front channel.
- [VerticalHeightCenter](./iouseraudiochannellabel/verticalheightcenter.md)
  A synonym for the top-center–front channel.
- [CenterTopMiddle](./iouseraudiochannellabel/centertopmiddle.md)
  The center top middle channel.
- [CenterTopRear](./iouseraudiochannellabel/centertoprear.md)
  The center top rear channel.
### Back Channels
- [TopBackCenter](./iouseraudiochannellabel/topbackcenter.md)
  The top-rear–center channel.
- [TopCenterSurround](./iouseraudiochannellabel/topcentersurround.md)
  A synonym for the top-rear–center channel.
- [TopBackLeft](./iouseraudiochannellabel/topbackleft.md)
  The top-rear–left channel.
- [TopBackRight](./iouseraudiochannellabel/topbackright.md)
  The top-rear–right channel.
### Surround Channels
- [CenterSurround](./iouseraudiochannellabel/centersurround.md)
  The center surround channel.
- [CenterSurroundDirect](./iouseraudiochannellabel/centersurrounddirect.md)
  The center surround direct channel.
- [LeftSurround](./iouseraudiochannellabel/leftsurround.md)
  The left surround channel.
- [LeftSurroundDirect](./iouseraudiochannellabel/leftsurrounddirect.md)
  The left surround direct channel.
- [RearSurroundLeft](./iouseraudiochannellabel/rearsurroundleft.md)
  The rear left surround channel.
- [RearSurroundRight](./iouseraudiochannellabel/rearsurroundright.md)
  The right rear surround channel.
- [RightSurround](./iouseraudiochannellabel/rightsurround.md)
  The right surround channel.
- [RightSurroundDirect](./iouseraudiochannellabel/rightsurrounddirect.md)
  The right surround direct channel.
### Low-Frequency Effects Channels
- [LFE2](./iouseraudiochannellabel/lfe2.md)
  The low-frequency effects 2 (LFE2) channel.
- [LFEScreen](./iouseraudiochannellabel/lfescreen.md)
  The low-frequency effects (LFE) screen channel.
### Monaural Channels
- [Mono](./iouseraudiochannellabel/mono.md)
  The mono channel.
### Alternate Content Channels
- [ClickTrack](./iouseraudiochannellabel/clicktrack.md)
  The click track channel.
- [DialogCentricMix](./iouseraudiochannellabel/dialogcentricmix.md)
  The dialog-centric mix channel.
- [ForeignLanguage](./iouseraudiochannellabel/foreignlanguage.md)
  The foreign language channel.
- [HearingImpaired](./iouseraudiochannellabel/hearingimpaired.md)
  The audio for the hearing-impaired channel.
- [Haptic](./iouseraudiochannellabel/haptic.md)
  The haptic effects channel.
- [Narration](./iouseraudiochannellabel/narration.md)
  The narration channel.
### Mid/Side Recording
- [MS_Mid](./iouseraudiochannellabel/ms_mid.md)
  The Mid/Side recording mid channel.
- [MS_Side](./iouseraudiochannellabel/ms_side.md)
  The Mid/Side recording side channel.
### X/Y Recording Channels
- [XY_X](./iouseraudiochannellabel/xy_x.md)
  The X/Y recording X channel.
- [XY_Y](./iouseraudiochannellabel/xy_y.md)
  The X/Y recording Y channel.
### First-Order Ambisonic Channels
- [Ambisonic_W](./iouseraudiochannellabel/ambisonic_w.md)
  The ambisonic W channel.
- [Ambisonic_X](./iouseraudiochannellabel/ambisonic_x.md)
  The ambisonic X channel.
- [Ambisonic_Y](./iouseraudiochannellabel/ambisonic_y.md)
  The ambisonic Y channel.
- [Ambisonic_Z](./iouseraudiochannellabel/ambisonic_z.md)
  The ambisonic Z channel.
### Binaural Recording
- [BinauralLeft](./iouseraudiochannellabel/binauralleft.md)
  The binaural left channel.
- [BinauralRight](./iouseraudiochannellabel/binauralright.md)
  The binaural right channel.
### Headphone Channels
- [HeadphonesLeft](./iouseraudiochannellabel/headphonesleft.md)
  The left headphone channel.
- [HeadphonesRight](./iouseraudiochannellabel/headphonesright.md)
  The right headphone channel.
### Unnumbered Discrete Channels
- [Discrete](./iouseraudiochannellabel/discrete.md)
  A generic discrete channel.
### Numbered Discrete Channels
- [Discrete_0](./iouseraudiochannellabel/discrete_0.md)
  Numbered discrete channel 0.
- [Discrete_1](./iouseraudiochannellabel/discrete_1.md)
  Numbered discrete channel 1.
- [Discrete_2](./iouseraudiochannellabel/discrete_2.md)
  Numbered discrete channel 2.
- [Discrete_3](./iouseraudiochannellabel/discrete_3.md)
  Numbered discrete channel 3.
- [Discrete_4](./iouseraudiochannellabel/discrete_4.md)
  Numbered discrete channel 4.
- [Discrete_5](./iouseraudiochannellabel/discrete_5.md)
  Numbered discrete channel 5.
- [Discrete_6](./iouseraudiochannellabel/discrete_6.md)
  Numbered discrete channel 6.
- [Discrete_7](./iouseraudiochannellabel/discrete_7.md)
  Numbered discrete channel 7.
- [Discrete_8](./iouseraudiochannellabel/discrete_8.md)
  Numbered discrete channel 8.
- [Discrete_9](./iouseraudiochannellabel/discrete_9.md)
  Numbered discrete channel 9.
- [Discrete_10](./iouseraudiochannellabel/discrete_10.md)
  Numbered discrete channel 10.
- [Discrete_11](./iouseraudiochannellabel/discrete_11.md)
  Numbered discrete channel 11.
- [Discrete_12](./iouseraudiochannellabel/discrete_12.md)
  Numbered discrete channel 12.
- [Discrete_13](./iouseraudiochannellabel/discrete_13.md)
  Numbered discrete channel 13.
- [Discrete_14](./iouseraudiochannellabel/discrete_14.md)
  Numbered discrete channel 14.
- [Discrete_15](./iouseraudiochannellabel/discrete_15.md)
  Numbered discrete channel 15.
- [Discrete_65535](./iouseraudiochannellabel/discrete_65535.md)
  The maximum numbered discrete channel.
### Generic High Order Ambisonics ACN Channel
- [HOA_ACN](./iouseraudiochannellabel/hoa_acn.md)
  A generic high order ambisonics (HOA) Ambisonic Channel Number (ACN).
### Numbered High Order Ambisonics ACN Channels
- [HOA_ACN_0](./iouseraudiochannellabel/hoa_acn_0.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 0.
- [HOA_ACN_1](./iouseraudiochannellabel/hoa_acn_1.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 1.
- [HOA_ACN_2](./iouseraudiochannellabel/hoa_acn_2.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 2.
- [HOA_ACN_3](./iouseraudiochannellabel/hoa_acn_3.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 3.
- [HOA_ACN_4](./iouseraudiochannellabel/hoa_acn_4.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 4.
- [HOA_ACN_5](./iouseraudiochannellabel/hoa_acn_5.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 5.
- [HOA_ACN_6](./iouseraudiochannellabel/hoa_acn_6.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 6.
- [HOA_ACN_7](./iouseraudiochannellabel/hoa_acn_7.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 7.
- [HOA_ACN_8](./iouseraudiochannellabel/hoa_acn_8.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 8.
- [HOA_ACN_9](./iouseraudiochannellabel/hoa_acn_9.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 9.
- [HOA_ACN_10](./iouseraudiochannellabel/hoa_acn_10.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 10
- [HOA_ACN_11](./iouseraudiochannellabel/hoa_acn_11.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 11.
- [HOA_ACN_12](./iouseraudiochannellabel/hoa_acn_12.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 12.
- [HOA_ACN_13](./iouseraudiochannellabel/hoa_acn_13.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 13.
- [HOA_ACN_14](./iouseraudiochannellabel/hoa_acn_14.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 14.
- [HOA_ACN_15](./iouseraudiochannellabel/hoa_acn_15.md)
  Numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN) 15.
- [HOA_ACN_65024](./iouseraudiochannellabel/hoa_acn_65024.md)
  The maximum numbered high order ambisonics (HOA) Ambisonic Channel Number (ACN).
### Special Values
- [Unused](./iouseraudiochannellabel/unused.md)
  An unknown or otherwise unspecified channel use.
- [UseCoordinates](./iouseraudiochannellabel/usecoordinates.md)
  A channel that uses coodinates to describe its position.
### Reserved Values
- [BeginReserved](./iouseraudiochannellabel/beginreserved.md)
  The beginning of the range of channel values reserved for internal use.
- [EndReserved](./iouseraudiochannellabel/endreserved.md)
### Enumeration Cases
- [Unknown](./iouseraudiochannellabel/unknown.md)
  unknown or unspecified other use

## See Also

### Working with Channel Layouts
- [SetPreferredChannelsForStereo](../iouseraudiodevice/setpreferredchannelsforstereo.md)
  Sets the channel indices for the prefered stereo pair.
- [GetPreferredChannelsForStereo](../iouseraudiodevice/getpreferredchannelsforstereo.md)
  Returns the channel indices for the prefered stereo pair.
- [SetPreferredInputChannelLayout](../iouseraudiodevice/setpreferredinputchannellayout.md)
  Sets the input channel layout, using an array of audio channel label values.
- [SetPreferredOutputChannelLayout](../iouseraudiodevice/setpreferredoutputchannellayout.md)
  Sets the output channel layout, using an array of audio channel label values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/audiodriverkit/audiodriverkit/iouseraudiochannellabel)*