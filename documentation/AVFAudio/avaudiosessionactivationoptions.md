# AVAudioSessionActivationOptions

**Framework**: AVFAudio  
**Kind**: struct

Constants that describe the options to pass when activating the audio session.

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
struct AVAudioSessionActivationOptions
```

## Topics

### Getting Standard Activation Options
- [init(rawValue: UInt)](avaudiosessionactivationoptions/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [func setActive(Bool, options: AVAudioSession.SetActiveOptions) throws](avaudiosession/setactive(_:options:).md)
  Activates or deactivates your app’s audio session using the specified options.
- [func activate(options: AVAudioSessionActivationOptions, completionHandler: (Bool, (any Error)?) -> Void)](avaudiosession/activate(options:completionhandler:).md)
  Activates an audio session asynchronously on watchOS.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosessionactivationoptions)*