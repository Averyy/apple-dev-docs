# AVAudioSessionActivationOptions

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

Constants that describe the options to pass when activating the audio session.

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
struct AVAudioSessionActivationOptions
```

```c
enum AVAudioSessionActivationOptions : NSUInteger;
```

## Topics

### Creating an activation option
- [init(rawValue: UInt)](./avaudiosessionactivationoptions/init%28rawvalue%29.md)
  Creates an activation-options set from a raw bitmask.
### Getting standard activation options
- [AVAudioSessionActivationOptionNone](./avaudiosessionactivationoptions/avaudiosessionactivationoptionnone.md)

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
- [struct AVAudioSessionDeactivationOptions](./avaudiosessiondeactivationoptions.md)
  Options for deactivating an AVAudioSession
- [- setActive:error:](./avaudiosession/setactive_error_.md)
  Activates or deactivates your app’s audio session.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionactivationoptions)*