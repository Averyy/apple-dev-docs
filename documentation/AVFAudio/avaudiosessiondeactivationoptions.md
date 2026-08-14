# AVAudioSessionDeactivationOptions

**Framework**: AVFAudio  
**Kind**: struct

Options for deactivating an AVAudioSession

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct AVAudioSessionDeactivationOptions
```

## Topics

### Initializers
- [init(rawValue: UInt)](avaudiosessiondeactivationoptions/init(rawvalue:).md)
### Type Properties
- [static var notifyOthersOnDeactivation: AVAudioSessionDeactivationOptions](avaudiosessiondeactivationoptions/notifyothersondeactivation.md)
  Notify an interrupted app that the interruption has ended and it may resume playback.

## Relationships

### Conforms To
- [BitwiseCopyable](../swift/bitwisecopyable.md)
- [Equatable](../swift/equatable.md)
- [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md)
- [OptionSet](../swift/optionset.md)
- [RawRepresentable](../swift/rawrepresentable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)
- [SetAlgebra](../swift/setalgebra.md)

## See Also

- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](avaudiosession/setactive(_:options:).md)
  Activates or deactivates your app’s audio session using the specified options.
- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](avaudiosession/activate(options:completionhandler:).md)
  Activates an audio session asynchronously.
- [func deactivate(options: AVAudioSessionDeactivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](avaudiosession/deactivate(options:completionhandler:).md)
  Deactivates the audio session asynchronously.
- [struct AVAudioSessionActivationOptions](avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondeactivationoptions)*