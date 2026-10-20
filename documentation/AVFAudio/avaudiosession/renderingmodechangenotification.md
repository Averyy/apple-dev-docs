# renderingModeChangeNotification

**Framework**: AVFAudio  
**Kind**: property  
**Role**: Type Property

A notification the system posts when the rendering mode changes.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- tvOS 17.2+

## Declaration

```swift
class let renderingModeChangeNotification: NSNotification.Name
```

```c
extern NSNotificationName const AVAudioSessionRenderingModeChangeNotification;
```

## Topics

### User information keys
- [let AVAudioSessionRenderingModeNewRenderingModeKey: String](../avaudiosessionrenderingmodenewrenderingmodekey.md)
  A key to retrieve an integer value that represents the new resolved rendering mode.

## See Also

### Inspecting rendering capabilities
- [var renderingMode: AVAudioSession.RenderingMode](./renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [AVAudioSession.RenderingMode](./renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](./supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](./renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.
- [class let spatialPlaybackCapabilitiesChangedNotification: NSNotification.Name](./spatialplaybackcapabilitieschangednotification.md)
  A notification the system posts when its spatial playback capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/renderingmodechangenotification)*