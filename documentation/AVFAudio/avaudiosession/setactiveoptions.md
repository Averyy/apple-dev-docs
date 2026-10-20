# AVAudioSession.SetActiveOptions

**Framework**: AVFAudio  
**Kind**: struct  
**Role**: Structure

Options that provide additional information about your app’s audio intentions upon session deactivation.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct SetActiveOptions
```

```c
enum AVAudioSessionSetActiveOptions : NSUInteger;
```

#### Overview

Use this option to request that the system notify an interrupted app that the interruption has ended and it may resume playback. This option is only valid on session deactivation.

## Topics

### Creating an activation option
- [init(rawValue: UInt)](./setactiveoptions/init%28rawvalue%29.md)
  Creates a new instance with the raw value you specify.
### Getting standard  options
- [static var notifyOthersOnDeactivation: AVAudioSession.SetActiveOptions](./setactiveoptions/notifyothersondeactivation.md)
  An option that indicates that the system should notify other apps that you’ve deactivated your app’s audio session.
- [var AVAudioSessionSetActiveFlags_NotifyOthersOnDeactivation: Int](../avaudiosessionsetactiveflags_notifyothersondeactivation.md)
  A flag that indicates that when your audio session deactivates, any audio sessions that your audio session interrupted can reactivate themselves.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [ExpressibleByArrayLiteral](../../Swift/expressiblebyarrayliteral.md)
- [OptionSet](../../Swift/optionset.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)
- [SetAlgebra](../../Swift/setalgebra.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/setactiveoptions)*