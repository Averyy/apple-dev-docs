# AVAudioSession.PortOverride.none

**Framework**: AVFAudio  
**Kind**: case  
**Role**: Case

A value that indicates not to override the output audio port.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- tvOS
- visionOS
- watchOS

## Declaration

```swift
case none
```

```c
AVAudioSessionPortOverrideNone
```

#### Discussion

Use this option to route audio to the system default outputs for the current category and mode.

## See Also

### Choosing a port override
- [AVAudioSession.PortOverride.speaker](./speaker.md)
  A value that indicates to override the current inputs and outputs, and route audio to the built-in speaker and microphone.


---

*[View on Apple Developer](https://developer.apple.com/documentation/avfaudio/avaudiosession/portoverride/none)*