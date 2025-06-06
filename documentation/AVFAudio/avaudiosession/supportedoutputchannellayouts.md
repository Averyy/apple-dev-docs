# supportedOutputChannelLayouts

**Framework**: AVFAudio  
**Kind**: property

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

#### Discussion

The possible channel layouts for this property are:

- [`kAudioChannelLayoutTag_Stereo`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_Stereo)
- [`kAudioChannelLayoutTag_AAC_5_1`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_AAC_5_1)
- [`kAudioChannelLayoutTag_MPEG_7_1_C`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_MPEG_7_1_C)
- [`kAudioChannelLayoutTag_Atmos_5_1_2`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_Atmos_5_1_2)
- [`kAudioChannelLayoutTag_Atmos_5_1_4`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_Atmos_5_1_4)
- [`kAudioChannelLayoutTag_Atmos_7_1_2`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_Atmos_7_1_2)
- [`kAudioChannelLayoutTag_Atmos_7_1_4`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_Atmos_7_1_4)
- [`kAudioChannelLayoutTag_Atmos_9_1_6`](https://developer.apple.com/documentation/CoreAudioTypes/kAudioChannelLayoutTag_Atmos_9_1_6)

This value returns an empty array when the audio session is inactive, ineligible for Now Playing, or the port type isn’t [`carAudio`](avaudiosession/port/caraudio.md) or, in iOS 18 or later, [`airPlay`](avaudiosession/port/airplay.md).

Use [`renderingCapabilitiesChangeNotification`](avaudiosession/renderingcapabilitieschangenotification.md) to listen for updates from the system.

## See Also

- [var renderingMode: AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [class let renderingModeChangeNotification: NSNotification.Name](avaudiosession/renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/supportedoutputchannellayouts)*