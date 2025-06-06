# renderingMode

**Framework**: AVFAudio  
**Kind**: property

The current audio session’s rendering mode.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- tvOS 17.2+

## Declaration

```swift
var renderingMode: AVAudioSession.RenderingMode { get }
```

#### Discussion

The value of this property is [`AVAudioSession.RenderingMode.notApplicable`](avaudiosession/renderingmode-swift.enum/notapplicable.md) in the following cases:

- The currently selected port isn’t of type [`carAudio`](avaudiosession/port/caraudio.md) or, in iOS 18 and later, [`airPlay`](avaudiosession/port/airplay.md).
- Your app uses a playback API other than [`AVPlayer`](https://developer.apple.com/documentation/AVFoundation/AVPlayer) or [`AVSampleBufferAudioRenderer`](https://developer.apple.com/documentation/AVFoundation/AVSampleBufferAudioRenderer).
- Playback isn’t currently active.
- The audio session is inactive, muted, or not eligible for Now Playing.

## See Also

- [AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [class let renderingModeChangeNotification: NSNotification.Name](avaudiosession/renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](avaudiosession/supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/renderingmode-swift.property)*