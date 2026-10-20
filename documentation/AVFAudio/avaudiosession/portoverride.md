# AVAudioSession.PortOverride

**Framework**: AVFAudio  
**Kind**: enum  
**Role**: Enumeration

Constants for use with the [`overrideOutputAudioPort(_:)`](./overrideoutputaudioport%28_%29.md) method.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
enum PortOverride
```

```c
enum AVAudioSessionPortOverride : NSUInteger;
```

## Topics

### Creating a port override
- [init?(rawValue: UInt)](./portoverride/init%28rawvalue%29.md)
### Choosing a port override
- [AVAudioSession.PortOverride.none](./portoverride/none.md)
  A value that indicates not to override the output audio port.
- [AVAudioSession.PortOverride.speaker](./portoverride/speaker.md)
  A value that indicates to override the current inputs and outputs, and route audio to the built-in speaker and microphone.

## Relationships

### Conforms To
- [BitwiseCopyable](../../Swift/bitwisecopyable.md)
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [RawRepresentable](../../Swift/rawrepresentable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/portoverride)*