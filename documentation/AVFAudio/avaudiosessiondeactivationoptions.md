# AVAudioSessionDeactivationOptions

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

Options for deactivating an AVAudioSession

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct AVAudioSessionDeactivationOptions
```

```c
enum AVAudioSessionDeactivationOptions : NSUInteger;
```

## Topics

### Creating a deactivation option
- [init(rawValue: UInt)](./avaudiosessiondeactivationoptions/init%28rawvalue%29.md)
  Creates a deactivation-options set from a raw bitmask.
### Getting standard deactivation options
- [static var notifyOthersOnDeactivation: AVAudioSessionDeactivationOptions](./avaudiosessiondeactivationoptions/notifyothersondeactivation.md)
  Notify an interrupted app that the interruption has ended and it may resume playback.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../Swift/optionset.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)
- [SetAlgebra](../Swift/setalgebra.md)

## See Also

### Activating and deactivating the session
- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](./avaudiosession/setactive%28_,options%29.md)
  Activates or deactivates your app’s audio session using the specified options.
- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](./avaudiosession/activate%28options,completionhandler%29.md)
  Activates an audio session asynchronously.
- [func deactivate(options: AVAudioSessionDeactivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](./avaudiosession/deactivate%28options,completionhandler%29.md)
  Deactivates the audio session asynchronously.
- [struct AVAudioSessionActivationOptions](./avaudiosessionactivationoptions.md)
  Constants that describe the options to pass when activating the audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessiondeactivationoptions)*