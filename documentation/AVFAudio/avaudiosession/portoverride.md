# AVAudioSession.PortOverride

**Framework**: AVFAudio  
**Kind**: enum

Constants for use with the [`overrideOutputAudioPort(_:)`](avaudiosession/overrideoutputaudioport(_:).md) method.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
enum PortOverride
```

## Topics

### Port Override Types
- [AVAudioSession.PortOverride.none](avaudiosession/portoverride/none.md)
  A value that indicates not to override the output audio port.
- [AVAudioSession.PortOverride.speaker](avaudiosession/portoverride/speaker.md)
  A value that indicates to override the current inputs and outputs, and route audio to the built-in speaker and microphone.
### Initializers
- [init?(rawValue: UInt)](avaudiosession/portoverride/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/portoverride)*