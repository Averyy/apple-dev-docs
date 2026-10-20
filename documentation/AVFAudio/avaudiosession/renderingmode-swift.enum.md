# AVAudioSession.RenderingMode

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Audio session rendering mode identifiers.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum RenderingMode
```

```c
enum AVAudioSessionRenderingMode : NSInteger;
```

## Topics

### Creating a rendering mode
- [init?(rawValue: Int)](./renderingmode-swift.enum/init%28rawvalue%29.md)
### Getting the rendering modes
- [AVAudioSession.RenderingMode.monoStereo](./renderingmode-swift.enum/monostereo.md)
  A mode that represents non multi-channel audio.
- [AVAudioSession.RenderingMode.surround](./renderingmode-swift.enum/surround.md)
  A mode that represents general multi-channel audio.
- [AVAudioSession.RenderingMode.spatialAudio](./renderingmode-swift.enum/spatialaudio.md)
  A mode that represents a fallback for when hardware capabilities don’t support Dolby.
- [AVAudioSession.RenderingMode.dolbyAudio](./renderingmode-swift.enum/dolbyaudio.md)
  A mode that represents Dolby audio.
- [AVAudioSession.RenderingMode.dolbyAtmos](./renderingmode-swift.enum/dolbyatmos.md)
  A mode that represents Dolby Atmos.
- [AVAudioSession.RenderingMode.notApplicable](./renderingmode-swift.enum/notapplicable.md)
  A mode that represents there’s no asset in a loading or playing state.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Inspecting rendering capabilities
- [var renderingMode: AVAudioSession.RenderingMode](./renderingmode-swift.property.md)
  The current audio session’s rendering mode.
- [class let renderingModeChangeNotification: NSNotification.Name](./renderingmodechangenotification.md)
  A notification the system posts when the rendering mode changes.
- [var supportedOutputChannelLayouts: [AVAudioChannelLayout]](./supportedoutputchannellayouts.md)
  The array of channel layouts that the current route supports.
- [class let renderingCapabilitiesChangeNotification: NSNotification.Name](./renderingcapabilitieschangenotification.md)
  A notification the system posts when the rendering capabilities change.
- [class let spatialPlaybackCapabilitiesChangedNotification: NSNotification.Name](./spatialplaybackcapabilitieschangednotification.md)
  A notification the system posts when its spatial playback capabilities change.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/renderingmode-swift.enum)*