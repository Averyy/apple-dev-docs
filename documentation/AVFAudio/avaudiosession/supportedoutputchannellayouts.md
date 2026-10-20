# supportedOutputChannelLayouts

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

The array of channel layouts that the current route supports.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- tvOS 17.2+

## Declaration

```swift
var supportedOutputChannelLayouts: [AVAudioChannelLayout] { get }
```

```objc
@property (readonly) NSArray<AVAudioChannelLayout *> * supportedOutputChannelLayouts;
```

#### Discussion

The possible channel layouts for this property are:

- [`kAudioChannelLayoutTag_Stereo`](../../CoreAudioTypes/kaudiochannellayouttag_stereo.md)
- [`kAudioChannelLayoutTag_AAC_5_1`](../../CoreAudioTypes/kaudiochannellayouttag_aac_5_1.md)
- [`kAudioChannelLayoutTag_MPEG_7_1_C`](../../CoreAudioTypes/kaudiochannellayouttag_mpeg_7_1_c.md)
- [`kAudioChannelLayoutTag_Atmos_5_1_2`](../../CoreAudioTypes/kaudiochannellayouttag_atmos_5_1_2.md)
- [`kAudioChannelLayoutTag_Atmos_5_1_4`](../../CoreAudioTypes/kaudiochannellayouttag_atmos_5_1_4.md)
- [`kAudioChannelLayoutTag_Atmos_7_1_2`](../../CoreAudioTypes/kaudiochannellayouttag_atmos_7_1_2.md)
- [`kAudioChannelLayoutTag_Atmos_7_1_4`](../../CoreAudioTypes/kaudiochannellayouttag_atmos_7_1_4.md)
- [`kAudioChannelLayoutTag_Atmos_9_1_6`](../../CoreAudioTypes/kaudiochannellayouttag_atmos_9_1_6.md)

This value returns an empty array when the audio session is inactive, ineligible for Now Playing, or the port type isn’t [`carAudio`](./port/caraudio.md) or, in iOS 18 or later, [`airPlay`](./port/airplay.md).

Use [`renderingCapabilitiesChangeNotification`](./renderingcapabilitieschangenotification.md) to listen for updates from the system.

## See Also

### Inspecting rendering capabilities
- [var renderingMode: AVAudioSession.RenderingMode](./renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [AVAudioSession.RenderingMode](./renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [class let renderingModeChangeNotification: NSNotification.Name](./renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](./renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.
- [class let spatialPlaybackCapabilitiesChangedNotification: NSNotification.Name](./spatialplaybackcapabilitieschangednotification.md)
  A notification the system posts when its spatial playback capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/supportedoutputchannellayouts)*