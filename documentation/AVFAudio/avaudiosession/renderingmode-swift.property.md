# renderingMode

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Instance Property

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

```objc
@property (readonly) AVAudioSessionRenderingMode renderingMode;
```

## Discussion

The value of this property is [`AVAudioSession.RenderingMode.notApplicable`](./renderingmode-swift.enum/notapplicable.md) in the following cases:

- The currently selected port isn’t of type [`carAudio`](./port/caraudio.md) or, in iOS 18 and later, [`airPlay`](./port/airplay.md).
- Your app uses a playback API other than [`AVPlayer`](../../AVFoundation/avplayer.md) or [`AVSampleBufferAudioRenderer`](../../AVFoundation/avsamplebufferaudiorenderer.md).
- Playback isn’t currently active.
- The audio session is inactive, muted, or not eligible for Now Playing.

## See Also

### Inspecting rendering capabilities
- [AVAudioSession.RenderingMode](./renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [class let renderingModeChangeNotification: NSNotification.Name](./renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](./supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](./renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.
- [class let spatialPlaybackCapabilitiesChangedNotification: NSNotification.Name](./spatialplaybackcapabilitieschangednotification.md)
  A notification the system posts when its spatial playback capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/renderingmode-swift.property)*