# AVAudioSession.RenderingMode

**Framework**: AVFAudio  
**Kind**: enum

Audio session rendering mode identifiers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum RenderingMode
```

## Topics

### Getting the rendering modes
- [AVAudioSession.RenderingMode.monoStereo](avaudiosession/renderingmode-swift.enum/monostereo.md)
  A mode that represents non multi-channel audio.
- [AVAudioSession.RenderingMode.surround](avaudiosession/renderingmode-swift.enum/surround.md)
  A mode that represents general multi-channel audio.
- [AVAudioSession.RenderingMode.spatialAudio](avaudiosession/renderingmode-swift.enum/spatialaudio.md)
  A mode that represents a fallback for when hardware capabilities don’t support Dolby.
- [AVAudioSession.RenderingMode.dolbyAudio](avaudiosession/renderingmode-swift.enum/dolbyaudio.md)
  A mode that represents Dolby audio.
- [AVAudioSession.RenderingMode.dolbyAtmos](avaudiosession/renderingmode-swift.enum/dolbyatmos.md)
  A mode that represents Dolby Atmos.
- [AVAudioSession.RenderingMode.notApplicable](avaudiosession/renderingmode-swift.enum/notapplicable.md)
  A mode that represents there’s no asset in a loading or playing state.
### Initializers
- [init?(rawValue: Int)](avaudiosession/renderingmode-swift.enum/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var renderingMode: AVAudioSession.RenderingMode](avaudiosession/renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [class let renderingModeChangeNotification: NSNotification.Name](avaudiosession/renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](avaudiosession/supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](avaudiosession/renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/renderingmode-swift.enum)*