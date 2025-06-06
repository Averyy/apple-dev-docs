# renderingModeChangeNotification

**Framework**: AVFAudio  
**Kind**: property

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

## Topics

### User information keys
- [let AVAudioSessionRenderingModeNewRenderingModeKey: String](avaudiosessionrenderingmodenewrenderingmodekey.md)
  A key to retrieve an integer value that represents the new resolved rendering mode.

## See Also

- [var renderingMode: AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](avaudiosession/supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/renderingmodechangenotification)*