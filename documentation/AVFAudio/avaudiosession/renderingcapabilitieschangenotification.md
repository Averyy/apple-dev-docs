# renderingCapabilitiesChangeNotification

**Framework**: AVFAudio  
**Kind**: property

A notification the system posts when the rendering capabilities change.

**Availability**:
- iOS 17.2+
- iPadOS 17.2+
- Mac Catalyst 17.2+
- tvOS 17.2+

## Declaration

```swift
class let renderingCapabilitiesChangeNotification: NSNotification.Name
```

## See Also

- [var renderingMode: AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.enum.md)
  Audio session rendering mode identifiers.
- [class let renderingModeChangeNotification: NSNotification.Name](avaudiosession/renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](avaudiosession/supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/renderingcapabilitieschangenotification)*