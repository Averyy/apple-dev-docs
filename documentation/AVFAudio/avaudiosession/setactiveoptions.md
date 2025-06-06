# AVAudioSession.SetActiveOptions

**Framework**: AVFAudio  
**Kind**: struct

Options that provide additional information about your app’s audio intentions upon session deactivation.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SetActiveOptions
```

#### Overview

Use this option to request that the system notify an interrupted app that the interruption has ended and it may resume playback. This option is only valid on session deactivation.

## Topics

### Creating an Activation Option
- [init(rawValue: UInt)](avaudiosession/setactiveoptions/init(rawvalue:).md)
  Creates a new instance with the raw value you specify.
### Getting Standard  Options
- [static var notifyOthersOnDeactivation: AVAudioSession.SetActiveOptions](avaudiosession/setactiveoptions/notifyothersondeactivation.md)
  An option that indicates that the system should notify other apps that you’ve deactivated your app’s audio session.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactiveoptions)*